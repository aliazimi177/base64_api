import base64
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import Base64Serializer


@api_view(['POST'])
def base64_encode_decode(request):
    serializer = Base64Serializer(data=request.data)
    if serializer.is_valid():
        text = serializer.validated_data.get('text')
        base64_string = serializer.validated_data.get('base64')
        
        if text:
            encoded = base64.b64encode(text.encode()).decode()
            return Response({'base64': encoded})
        elif base64_string:
            decoded = base64.b64decode(base64_string).decode()
            return Response({'text': decoded})
    return Response(serializer.errors, status=400)

