from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from models.experience import Experiences


class CareerCoach:
    def __init__(self, instructions: str, output_parser=None) -> None:
        self.instructions = instructions
        self.output_parser = output_parser
        format_instructions = (
            self.output_parser.get_format_instructions() if output_parser else ""
        )

        prompt = PromptTemplate.from_template(
            instructions, partial_variables={"format_instructions": format_instructions}
        )
        self.chain = LLMChain(
            llm=ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-16k"), prompt=prompt
        )

    def proceed(self, docs):
        return self.chain.run(docs)


def extract_experiences(resume):
    instructions = """ You are a Resume specialist. Your area of expertise revolves around analyzing a resume in order to extract any relevant informations about all job experience it contains.
        You excel in extracting experience information from a resume.
        Here are the informations you want to extract :
        Job Title: [Extracted Job Title]
        Company Name: [Extracted Company Name]
        Location: [Extracted Location]
        Start Date: [Extracted Start Date]
        End Date: [Extracted End Date]
        Description: [Extracted Job Description]
        Skills: [Extracted Skills]
        References: [Extracted References]
        Order or Priority: [Extracted Order or Priority]
        Current Job: [Extracted Current Job Status]
        Type of Employment: [Extracted Employment Type]
        Salary or Compensation: [Extracted Salary/Compensation]
        Supervisor or Manager: [Extracted Supervisor/Manager]
        Company Website: [Extracted Company Website]
        Industry: [Extracted Industry/Sector]
        Achievements: [Extracted Achievements]
        Responsibilities: [Extracted Responsibilities]
        If you can't find a specific informations to extract just dont do it. 

        Return a list of Experience when finish.
        
        \n{format_instructions}

        {resume}
        """
    output_parser = PydanticOutputParser(pydantic_object=Experiences)
    coach = CareerCoach(instructions=instructions, output_parser=output_parser)
    response = coach.proceed(docs=resume)

    return output_parser.parse(response)
