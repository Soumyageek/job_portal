from django.forms import ModelForm

from .models import Job, Applicant


class CreateJobForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(CreateJobForm, self).__init__(*args, **kwargs)

        self.fields['job_title'].label = "Title (Designation)"
        self.fields['job_description'].label = "About the Job Profile"
        self.fields['job_location'].label = 'Location'
        self.fields['type'].label = 'Job Type'
        self.fields['job_category'].label = 'Job Category'
        self.fields['last_date'].label = 'Last Date to Apply'
        self.fields['company_name'].label = 'Company Name'
        self.fields['company_description'].label = 'About the Company'
        self.fields['job_website'].label = 'Company Website'
        self.fields['job_salary'].label = 'Salary'

        self.fields['job_title'].widget.attrs.update(
            {
                'placeholder': 'Enter the Job Title/Position',
            }
        )
        self.fields['job_description'].widget.attrs.update(
            {
                'placeholder': 'Enter the Job Description',
            }
        )
        self.fields['job_location'].widget.attrs.update(
            {
                'placeholder': 'Enter the Job Location',
            }
        )
        self.fields['type'].widget.attrs.update(
            {
                'placeholder': 'Enter the Job Type',
            }
        )
        self.fields['job_category'].widget.attrs.update(
            {
                'placeholder': 'Enter the Job Category',
            }
        )
        self.fields['last_date'].widget.attrs.update(
            {
                'placeholder': 'Enter the Last Date (MM/DD/YYYY)',
            }
        )
        self.fields['company_name'].widget.attrs.update(
            {
                'placeholder': "Enter the Company's Name",
            }
        )
        self.fields['company_description'].widget.attrs.update(
            {
                'placeholder': 'Enter the Company Description',
            }
        )
        self.fields['job_website'].widget.attrs.update(
            {
                'placeholder': 'Enter the Company Website/URL',
            }
        )

    class Meta:
        model = Job
        exclude = ('user',)
        fields = ['job_title','job_description','job_location','type',
                  'job_category','last_date','company_name','company_description','job_website','job_salary']

    # def save(self, user, commit=True):
    #     job = super(CreateJobForm, self).save(commit=False)
    #     job.user = self.request.user
    #     if commit:
    #         job.save()
    #     return job


class ApplyJobForm(ModelForm):
    class Meta:
        model = Applicant
        fields = ('user','job')