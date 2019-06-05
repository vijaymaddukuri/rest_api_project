from auc.baseusecase import BaseUseCase


class GetSpeakerSound(BaseUseCase):
    """
    Description: Gets the audio sound from the speaker
    """
    def get_speaker_sound(self):
        """
        Description: To get the audio sound from speaker
        """
        self.server_url = self.ctx_in['server_url']
        self.audio_sound = self.ctx_in.session.get(self.server_url)

    def run_test(self):
        """
        Description: Execute the above procedure to get audio sound
        """
        self.get_speaker_sound()

    def _validate_context(self):
        """
        Description: Validate the inputs passed to this function
        """
        if self.ctx_in:
            self.server_url = self.ctx_in['server_url']

    def _finalize_context(self):
        """
        :return: Returns the audio sound
        """
        setattr(self.ctx_out, 'audio_sound', self.audio_sound)