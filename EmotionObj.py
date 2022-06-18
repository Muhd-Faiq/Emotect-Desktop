class EmotionObj(object):
    def __init__(self):
        self._happy = None
        self._angry = None
        self._neutral = None
        self._sad = None
        self._disgust = None
        self._surprise = None
        self._fear = None

    ####happy start#####
    @property
    def happy(self):
        """I'm the 'happy' property."""
        # print("getter of happy called")
        return self._happy

    @happy.setter
    def happy(self, value):
        # print("setter of happy called")
        self._happy = value

    @happy.deleter
    def happy(self):
        # print("deleter of happy called")
        del self._happy

    ####happy end#####
    
    ####angry start#####
    @property
    def angry(self):
        """I'm the 'angry' property."""
        # print("getter of angry called")
        return self._angry

    @angry.setter
    def angry(self, value):
        # print("setter of angry called")
        self._angry = value

    @angry.deleter
    def angry(self):
        # print("deleter of angry called")
        del self._angry

    ####angry end#####

    ####neutral start#####
    @property
    def neutral(self):
        """I'm the 'neutral' property."""
        # print("getter of neutral called")
        return self._neutral

    @neutral.setter
    def neutral(self, value):
        # print("setter of neutral called")
        self._neutral = value

    @neutral.deleter
    def neutral(self):
        # print("deleter of neutral called")
        del self._neutral

    ####neutral end#####

    ####sad start#####
    @property
    def sad(self):
        """I'm the 'sad' property."""
        # print("getter of sad called")
        return self._sad

    @sad.setter
    def sad(self, value):
        # print("setter of sad called")
        self._sad = value

    @sad.deleter
    def sad(self):
        # print("deleter of sad called")
        del self._sad

    ####sad end#####

    ####disgust start#####
    @property
    def disgust(self):
        """I'm the 'disgust' property."""
        # print("getter of disgust called")
        return self._disgust

    @disgust.setter
    def disgust(self, value):
        # print("setter of disgust called")
        self._disgust = value

    @disgust.deleter
    def disgust(self):
        # print("deleter of disgust called")
        del self._disgust

    ####disgust end#####

    ####surprise start#####
    @property
    def surprise(self):
        """I'm the 'surprise' property."""
        # print("getter of surprise called")
        return self._surprise

    @surprise.setter
    def surprise(self, value):
        # print("setter of surprise called")
        self._surprise = value

    @surprise.deleter
    def surprise(self):
        # print("deleter of surprise called")
        del self._surprise

    ####surprise end#####

    ####fear start#####
    @property
    def fear(self):
        """I'm the 'fear' property."""
        # print("getter of fear called")
        return self._fear

    @fear.setter
    def fear(self, value):
        # print("setter of fear called")
        self._fear = value

    @fear.deleter
    def fear(self):
        # print("deleter of fear called")
        del self._fear

    ####fear end#####