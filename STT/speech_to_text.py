import speech_recognition as sr


class SpeechToText:
    def __init__(self, logger):
        self.logger = logger
        self.r = sr.Recognizer()

    def convert_to_text(self, path):
        self.logger.info(f"Beginning text extraction for {path}")
        with sr.AudioFile(path) as source:
            audio = self.r.record(source)

            text = self.r.recognize_google(audio)
            self.logger.info("Completed text extraction")
            return text

