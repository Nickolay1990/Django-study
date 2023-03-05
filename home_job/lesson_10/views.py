from django.urls import reverse_lazy
from django.views.generic import FormView
from django.http import HttpResponse

from lesson_10.models import GamesBase, Cityes
from lesson_10.serializers import GamesBaseSerializer, CitySerializer
from lesson_10.permissins import IsAdminOrReadOnly, IsCreaterOrReadOnly
from lesson_10.forms import CityesForm

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, \
    IsAuthenticated
from rest_framework.response import Response


class GamesApiList(generics.ListCreateAPIView):
    queryset = GamesBase.objects.all()
    serializer_class = GamesBaseSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class GamesApiUpdate(generics.RetrieveUpdateAPIView):
    queryset = GamesBase.objects.all()
    serializer_class = GamesBaseSerializer
    permission_classes = (IsAuthenticated,)


class GamesApiDestroy(generics.RetrieveDestroyAPIView):
    queryset = GamesBase.objects.all()
    serializer_class = GamesBaseSerializer
    permission_classes = (IsAdminOrReadOnly,)


class GamesApiRetrieveId(generics.RetrieveAPIView):
    queryset = GamesBase.objects.all()
    serializer_class = GamesBaseSerializer
    permission_classes = (IsAuthenticated,)


class GamesApiRetrieveName(generics.RetrieveAPIView):
    queryset = GamesBase.objects.all()
    serializer_class = GamesBaseSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, name):
        if name:
            try:
                query = GamesBase.objects.filter(name=name)
                serializer = GamesBaseSerializer(query, many=True)
                return Response(serializer.data)
            except:
                return Response({'error': 'game not found'})


class CityesFormView(FormView):
    form_class = CityesForm
    template_name = 'cityes.html'
    success_url = reverse_lazy('cityes')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class GetTime(generics.GenericAPIView):
    serializer_class = CitySerializer

    def get(self, request, city):
        if city:
            try:
                query = Cityes.objects.get(city=city)
                serializer = CitySerializer(query)
                return Response(serializer.data)
            except:
                return Response({'error': 'city not found'})
