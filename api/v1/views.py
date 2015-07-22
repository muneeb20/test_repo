from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from api.v1.serializers import StringListSerializer
import ast


class SortStringListView(GenericAPIView):
    """
        Enter List of String to sort
        Only 1 format accepted
        ['abc', 'bcd']
        Input Value = {"string_list": ['abc', 'bcd']}
        Return Value = Sorted list of dictionary same like input
    """
    serializer_class = StringListSerializer

    def post(self, request, format=None):
        ret = {}
        return_status = status.HTTP_200_OK
        try:
            model = request.DATA
            serializer = StringListSerializer(data=model)
            if serializer.is_valid():
                string_list = model.get('string_list')
                if not isinstance(string_list, list):
                    string_list = ast.literal_eval(str(string_list))
                sorted_string_list = sorted(string_list, key=lambda x: x[:2])
                ret["success"] = True
                ret["string_list"] = sorted_string_list
            else:
                ret["success"] = False
                ret["msg"] = 'Invalid Data Provided'
                return_status = status.HTTP_400_BAD_REQUEST
        except Exception as e:
            ret["success"] = False
            ret["msg"] = 'Please contact System Admin.'
            return_status = status.HTTP_400_BAD_REQUEST
        return Response(ret, return_status)