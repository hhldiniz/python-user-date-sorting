class Message:
    def __init__(self, user, m_type, subtype, ts, text):
        self.user = user
        self.m_type = m_type
        self.subtype = subtype
        self.ts = ts
        self.text = text
