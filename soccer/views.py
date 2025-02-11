from django.shortcuts import render

# class DisciplineViewSet(ModelViewSet):
#     serializer_class = DisciplineSerializer
#     # permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         # Filtra las disciplinas por el user_id en la URL
#         user_id = self.kwargs.get('user_id')
#         return Discipline.objects.filter(user_id=user_id)

#     def perform_create(self, serializer):
#         # Asocia automáticamente la disciplina al usuario especificado en la URL
#         user_id = self.kwargs.get('user_id')
#         serializer.save(user_id=user_id)


# class MatchViewSet(ModelViewSet):
#     queryset = Match.objects.all()
#     permission_classes = [IsAuthenticated]

#     def get_serializer_class(self):
#         # Usa un serializer diferente para los detalles de un partido
#         if self.action == 'retrieve':
#             return MatchDetailSerializer
#         return MatchSerializer

#     def perform_create(self, serializer):
#         # Asocia automáticamente el partido con el usuario autenticado
#         serializer.save(creator=self.request.user)


# class PlayerSlotViewSet(ModelViewSet):
#     queryset = PlayerSlot.objects.all()
#     serializer_class = PlayerSlotSerializer
#     permission_classes = [IsAuthenticated]

#     def perform_update(self, serializer):
#         serializer.save(player=self.request.user)

#     @action(detail=False, methods=['get'], url_path='match/(?P<match_id>[^/.]+)')
#     def slots_by_match(self, request, match_id=None):
#         slots = PlayerSlot.objects.filter(match_id=match_id)
#         serializer = self.get_serializer(slots, many=True)
#         return Response(serializer.data)

