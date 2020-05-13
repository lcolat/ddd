class CreateInterview:
    def create(self, request):
        recruiter = recruiterRepository.findAvailable(request.getTimeInterviewTime())
        newInterview = interviewRepository.create(request.getCandidate(), request.getTimeInterviewTime, recruiter)
