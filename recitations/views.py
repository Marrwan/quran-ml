from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RecitationSerializer
from recitations.modelz.speech_recognition import transcribe_audio
from recitations.modelz.tajweed_detection import detect_errors


class RecitationView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RecitationSerializer(data=request.data)
        if serializer.is_valid():
            audio_file = serializer.validated_data['audio']
            transcript = transcribe_audio(audio_file)
            errors = detect_errors(transcript)
            return Response({'transcript': transcript, 'errors': errors}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
