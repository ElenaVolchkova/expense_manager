from requests import Response
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from owner.models import Owner
from transaction.models import Transaction
from .permissions import IsOwnerOrReadOnly

from .serializers import TransactionSerializer
from .service import TransactionFilter



class TransactionAPIList(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (DjangoFilterBackend, )
    filterset_class = TransactionFilter
    #
    def update_balance(self, request):
        print(request)
        data = request.data
        if request.method == "POST":
            owner_id = data.get('owner', None)
            owner = Owner.objects.get(pk=owner_id)
            transaction_amount = data.get('amount', None)
            category = data.get('category', None)
            if category == 2:
                owner.balance = float(owner.balance) + float(transaction_amount)
                owner.save(update_fields=["balance"])
            else:
                owner.balance = float(owner.balance) - float(transaction_amount)
                owner.save(update_fields=["balance"])

    def post(self, request, *args, **kwargs):
        serializer = TransactionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        self.update_balance(request)
        return self.create(request, *args, **kwargs)



class TransactionAPIUpdate(generics.UpdateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class TransactionAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = (IsOwnerOrReadOnly,)



# class TransactionAPIView(APIView):
#     def get(self, request):
#         lst = Transaction.objects.all().values()
#         return Response({'transaction': TransactionSerializer(lst, many=True).data})
#
#     def post(self, request):
#         serializer = TransactionSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'transaction': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#
#         try:
#             instance = Transaction.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})
#
#         serializer = TransactionSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'transaction': serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
#
#         try:
#             instance = Transaction.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})
#
#         instance.delete()
#         return Response({'transaction': "delete transaction " + str(pk)})
