class TextAnalyzer:

    def analyze(self, podcast, bad_list, less_bad_list):

        bds_percent = self.bds_percent(podcast, bad_list, less_bad_list)
        is_bds = self.is_bds(bds_percent)
        bds_threat_level = self.threat_level(bds_percent)

        return {"bds_percent": bds_percent,
                "is_bds": is_bds,
                "bds_threat_level": bds_threat_level}

    @staticmethod
    def bds_percent(podcast, bad_list, less_bad_list):
        total_word_count = 0
        podcast_lower = podcast.lower()

        for word in bad_list:
            total_word_count += podcast_lower.count(word) * 2

        for word in less_bad_list:
            total_word_count += podcast_lower.count(word)

        return (total_word_count / len(podcast_lower.split(" "))) * 100

    @staticmethod
    def is_bds(percent):
        if percent > 5.0:
            return True
        return False

    @staticmethod
    def threat_level(percent):
        if percent < 5.0:
            return None
        elif 5.0 < percent < 30.0:
            return "Medium"
        else:
            return "High"


