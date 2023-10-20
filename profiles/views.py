from rest_framework import viewsets
from .models import Profile
from .serializers import ProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    # ForeignKey - OneToOne
    queryset = Profile.objects.select_related('author').all()
    # ManyToMany -> prefetch_related
    serializer_class = ProfileSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        print(queryset.query)
        return queryset
