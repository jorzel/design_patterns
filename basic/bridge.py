class EmailExport(object):
    """Implementation-specific"""
    
    def export(self, profile):
        print('Export data to mail box')


class AtsExport(object):
    """Implementation-specific"""

    def export(self, profile):
        print('Export data to ats system')


class Candidate(object):
    """Implementation-independent"""

    def __init__(self, status, profile, export_method):
        self.status = status
        self.profile = profile
        self._export_method = export_method
    
    def set_status(self, status):
        self.status = status
    
    def export(self):
        self._export_method.export(self.profile)

exports = [EmailExport(), AtsExport()]

for export in exports:
    candidate = Candidate('pending', {}, export)
    candidate.export()
