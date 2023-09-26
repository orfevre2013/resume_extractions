
from typing import List, Optional
from datetime import date
from pydantic import BaseModel, Field,  validator

class Experience(BaseModel):
    job_title : Optional[str]  = Field(description="the job title or name")
    company_name : Optional[str]  = Field(description="the company name")
    location : Optional[str]  = Field(description="the company location")
    start_date : Optional[str]  = Field(description="Start date of the job")
    end_date : Optional[str]  = Field(description="End date of the job (nullable for ongoing jobs)")
    description : Optional[str]  = Field(description="Job description")
    skills : Optional[str]  = Field(description="Skills used or gained in the role")
    references : Optional[str]  = Field(description="references or contact information")
    order_or_priority : Optional[str]  = Field(description="Order or priority of the job")
    is_current_job : bool = Field(description="Indicates if it's the current job")
    type_of_employment : Optional[str]  = Field(description="Type of employment (e.g., full-time)")
    salary_or_compensation : Optional[str]  = Field(description="Salary or compensation")
    supervisor_manager : Optional[str]  = Field(description="Supervisor or manager's name")
    company_website : Optional[str]  = Field(description="Company's website")
    industry: Optional[str]  = Field(description="Industry or sector")
    achievements : Optional[str]  = Field(description="Notable achievements")
    responsibilities : Optional[str]  = Field(description="Detailed responsibilities")

    @validator("*", pre=True, always=True)
    def set_to_none_if_na(cls, value):
        # If the value is 'NA', set it to None
        if value == 'N/A':
            return None
        return value

    @validator("end_date", pre=True, always=True)
    def parse_end_date(cls, value):
        if isinstance(value, Optional[str] ):
            # Attempt to parse the Optional[str] ing into a date format
            try:
                return date.fromisoformat(value)
            except ValueError:
                # Handle parsing error by returning None (or raising an error)
                return None
        return value
    
    @validator("start_date", pre=True, always=True)
    def parse_start_date(cls, value):
        if isinstance(value, Optional[str] ):
            # Attempt to parse the Optional[str] ing into a date format
            try:
                return date.fromisoformat(value)
            except ValueError:
                # Handle parsing error by returning None (or raising an error)
                return None
        return value


class Experiences(BaseModel):
    experiences: List[Experience]