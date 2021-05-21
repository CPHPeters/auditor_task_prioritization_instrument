import random
import itertools

from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Christian Peters and Bart Dierynck'

doc = """
Developed Bart Dierynck and Christian Peters, Tilburg University. For questions you can contact Christian Peters
(c.p.h.peters@tilburguniversity.edu).
"""


class Constants(BaseConstants):
    name_in_url = 'taskdiscretion_eng'
    players_per_group = None
    num_rounds = 1
    StandardChoices=[
        [1, 'Disagree strongly'],
        [2, 'Disagree moderately'],
        [3, 'Disagree slightly'],
        [4, 'Neither agree nor disagree'],
        [5, 'Agree slightly'],
        [6, 'Agree moderately'],
        [7, 'Agree strongly'],
    ]
    even = [2,4] #LOW PO
    odd = [1,3] #HIGH PO


class Subsession(BaseSubsession):

    def creating_session(self):
        number = itertools.cycle([1, 2, 3, 4])
        for player in self.get_players():
            player.treat = next(number)

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()

    def get_timeout_seconds(self):
        return self.participant.vars['expirytime'] - time.time()

    # Player Variables
    treat = models.IntegerField()
    accept_conditions = models.BooleanField(blank=False, widget = widgets.CheckboxInput)
    feeder2000first = models.BooleanField()
    task_choice = models.BooleanField() # True = Feeder, False = Robofer
    orderDemographics = models.BooleanField()
    inspectinfo = models.IntegerField(blank=True, initial=0)
    screenshot_training = models.IntegerField(blank=True, initial=0)
    random = models.IntegerField()
    screenshot_feeder = models.IntegerField(blank=True, initial=0)
    screenshot_robofer = models.IntegerField(blank=True, initial=0)
    summary_figure = models.IntegerField(blank=True, initial=0)

    # Comprehension Questions

    understanding = models.IntegerField(
        label = "Please select the statement that is most appropriate for the situation:",
        choices = [
            [1, 'CMG Machines owns two patent and grants exclusive rights to use and exploit the machines to Agrifirm, in return CMG Machines receives royalty payments.'],
            [2, 'Agrifirm owns two patents  and grants exclusive rights to use and exploit the machines to CMG Machines, in return Agrifirm receives royalty payments.'],
            [3, 'Agrifirm acquired CMG Machines and is therefore able to capitalize the patents.']
        ],
        widget = widgets.RadioSelect
    )

    cq1 = models.IntegerField(
        label = "A decrease in the discount rate used by Agrifirm:",
        choices=[
            [1, 'Increases the present value of the cash flows.'],
            [2, 'Decreases the present value of the cash flows.'],
            [3, 'Does not affect the present value of the cash flows.']
        ],
        widget = widgets.RadioSelect
    )
    cq2 = models.IntegerField(
        label = "A decrease in the royalty rate used by Agrifirm:",
        choices = [
            [1, 'Increases the present value of the cash flows.'],
            [2, 'Decreases the present value of the cash flows.'],
            [3, 'Does not affect the present value of the cash flows.']
        ],
        widget = widgets.RadioSelect
    )

    # PO (Training)

    name_PO = models.StringField(label="Please fill in your first name:", blank=False)

    # Documentation

    documentatie = models.TextField(label="", blank=False)

    # Judgment Variables
    difficulty_slider = models.FloatField(
        widget=widgets.SliderInput(attrs={'step': '1', 'style': 'width:500px'}, show_value=True),
        min=-100,
        initial=0,
        max=100,
    )

    #Task Outcomes

    mistakes_robofer = models.TextField(label="Fill in the cells (e.g., B2) in which you think Agrifirm has made a mistake:", blank=True)
    robofer_estimate = models.FloatField(label="Fill in the fair value amount, that you think accurately represents the value of the patents, given the parameters:", blank=True)
    mistakes_feeder = models.TextField(label="Fill in the cells (e.g., B2) in which you think Agrifirm has made a mistake:", blank=True)
    feeder_estimate = models.FloatField(label="Fill in the fair value amount, that you think accurately represents the value of the patents, given the parameters:", blank=True)

    # Manipulation Checks

    time_consideration = models.IntegerField(
        label = "When I had to decide which task to do first, the estimated time needed for the task impacted my decision.",
        choices = Constants.StandardChoices
    )

    learning_effect = models.IntegerField(
        label = "When I had to decide which task to do first, the expected learning effects have impacted my decision.",
        choices = Constants.StandardChoices
    )

    choice_method_1 = models.IntegerField(
        label = "When I had to decide which task to do first, I took into consideration that I wanted to finish at least one task within the 8 minutes.",
        choices = Constants.StandardChoices
    )

    choice_method_2 = models.IntegerField(
        label = "When I had to decide which task to do first, I assumed that I could finish both tasks within 8 minutes.",
        choices =Constants.StandardChoices
    )

    pom_1_1 = models.IntegerField(
        label = "In this audit team, control over the tasks is seen as important.",
        choices = Constants.StandardChoices
    )

    pom_1_2 = models.IntegerField(
        label = "In this audit team, you do not have control over the way in which the tasks are conducted.",
        choices = Constants.StandardChoices
    )

    pom_1_3 = models.IntegerField(
        label = "In this audit team, you can use the insights from previous tasks in deciding how to conduct future audit tasks.",
        choices = Constants.StandardChoices
    )

    pom_1_4 = models.IntegerField(
        label = "When I made myself familiar with the tasks, I experienced time pressure.",
        choices = Constants.StandardChoices
    )

    pom_2_1 = models.IntegerField(
        label = "When I documented why the patents had to be valued using the fair value method, I did not have much control over the way in which this was done.",
        choices = Constants.StandardChoices
    )

    pom_2_2 = models.IntegerField(
        label = "I feel a high degree of personal involvement with the documentation that was written.",
        choices = Constants.StandardChoices
    )

    pom_2_3 = models.IntegerField(
        label = "If someone would give me a compliment for the documentation that was written, it would feel as a personal compliment.",
        choices = Constants.StandardChoices
    )

    pom_2_4 = models.IntegerField(
        label = "Whe I documented why the patents had to be valued using the fair value method, I felt involved with this documentation.",
        choices = Constants.StandardChoices
    )

    pom_3_1 = models.IntegerField(
        label = "When I conducted the audit tasks, I had the feeling that I could decide myself how to conduct them.",
        choices = Constants.StandardChoices
    )

    pom_3_2 = models.IntegerField(
        label = "When I conducted the audit tasks, I felt a high degree of personal involvement by the work that I did.",
        choices = Constants.StandardChoices
    )

    pom_3_3 = models.IntegerField(
        label = "If someone would give me a compliment for the audit tasks that were done, this would feel as a personal compliment.",
        choices = Constants.StandardChoices
    )

    pom_3_4 = models.IntegerField(
        label = "When I conducted the audit tasks, I experienced time pressure.",
        choices = Constants.StandardChoices
    )

    pom_3_5 = models.IntegerField(
        label = "I had the feeling that I had too little time to execute the audit tasks well.",
        choices = Constants.StandardChoices
    )

    pom_4_1 = models.IntegerField(
        label = "I feel a high degree of personal ownership of the work I did during the audit engagement.",
        choices = Constants.StandardChoices
    )

    pom_4_2 = models.IntegerField(
        label = "The audit tasks that I did are my own work.",
        choices = Constants.StandardChoices
    )

    pom_4_3 = models.IntegerField(
        label = "I have the feeling that the audit tasks that I did are my own work.",
        choices = Constants.StandardChoices
    )

    pom_4_4 = models.IntegerField(
        label = "I have the feeling that the audit tasks that I did are mine.",
        choices = Constants.StandardChoices
    )

    po_check = models.IntegerField(
        label = "I consider the documentation as part of the audit tasks that I had to conduct within the eight minutes.",
        choices = Constants.StandardChoices
    )
    difficulty_consideration = models.IntegerField(
        label = "When I had to decide what task to do first, I took the difficulty of both tasks into consideration.",
        choices = Constants.StandardChoices
    )

    robofer_difficulty = models.IntegerField(
        label = "The audit of the Robofer patent was difficult.",
        choices = Constants.StandardChoices
    )

    feeder_difficulty = models.IntegerField(
        label = "The audit of the Feeder 2000 patent was difficult.",
        choices = Constants.StandardChoices
    )

    both_difficulty = models.IntegerField(
        label = "The audit of the Robofer patent was more difficult than the audit of the Feeder 2000 patent.",
        choices = Constants.StandardChoices
    )

    # Accountability

    accountability = models.IntegerField(
        label = "During the audit, I felt a high degree of accountability to the audit team leader.",
        choices = Constants.StandardChoices
    )

    # Interest and Enjoyment Questions:

    IE_1 = models.IntegerField(
        label = "I enjoyed doing the audit tasks.",
        choices = Constants.StandardChoices
    )

    IE_2 = models.IntegerField(
        label = "It was difficult to keep concentrated for a long time on the audit tasks.",
        choices = Constants.StandardChoices
    )

    # Work Engagement Questions

    WE_1 = models.IntegerField(
        label = "On my job, I am full of energy.",
        choices = Constants.StandardChoices
    )

    WE_2 = models.IntegerField(
        label = "My job inspires me.",
        choices = Constants.StandardChoices
    )

    WE_3 = models.IntegerField(
        label = "If I wake up in the morning, I enjoy going to my job.",
        choices = Constants.StandardChoices
    )

    # Need for Cognition: taken from scale Cacioppo, J.T. and Petty, R.E. (1982)
    need_for_cognition_1 = models.IntegerField(
        label="I enjoy doing tasks that require little thought, at the moment you have learned them.",
        choices= Constants.StandardChoices
    )

    need_for_cognition_2 = models.IntegerField(
        label="I enjoy having responsibility over tasks that require a lot of thinking.",
        choices= Constants.StandardChoices
    )

    need_for_cognition_3 = models.IntegerField(
        label="I am proud of the outcomes of my reasoning.",
        choices= Constants.StandardChoices
    )

    # Ervaring met taken

    experience_dcf = models.IntegerField(
        label="How often have you audited DCF models?",
        choices = [
            [1, 'Never'],
            [2, 'Rarely'],
            [3, 'Sometimes'],
            [4, 'Often'],
            [5, 'Very Often']
        ]
    )

    experience_fve = models.IntegerField(
        label="How often did you audit fair value estimates?",
        choices = [
            [1, 'Never'],
            [2, 'Rarely'],
            [3, 'Sometimes'],
            [4, 'Often'],
            [5, 'Very Often']
        ]
    )

    see_spreadsheet = models.IntegerField(
        label = "I could view the Excel spreadsheets and could work in it.",
        choices = [
            [1, 'True'],
            [2, 'False']
        ]
    )

    # Basic Needs Satisfaction (Deci et al., 2001)

    # Autonomy

    BNS_1 = models.IntegerField(
        label = "During the study, I had the feeling that I had a lot of control over the way in which I conducted the audit tasks.",
        choices = Constants.StandardChoices
    )

    BNS_2 = models.IntegerField(
        label = "During the audit tasks, I had the feeling that I had to do what was ordered to me.",
        choices=Constants.StandardChoices
    )

    BNS_3 = models.IntegerField(
        label = "There were not much possibilities to determine how to do the audit tasks during the study.",
        choices=Constants.StandardChoices
    )

    BNS_4 = models.IntegerField(
        label = "I had the feeling to have learned things while conducting the audit tasks.",
        choices=Constants.StandardChoices
    )

    BNS_5 = models.IntegerField(
        label = "During the audit tasks I did not have any opportunities to show my capabilities.",
        choices=Constants.StandardChoices
    )

    BNS_6 = models.IntegerField(
        label = "During the audit tasks, I felt very capable.",
        choices=Constants.StandardChoices
    )

    # Priority of Audit Quality

    PrAQ_1 = models.IntegerField(
        label = "When I have to work under high time pressure, I prefer to do my work as fast as possible, even if this leads to a lower level of audit quality.",
        choices=Constants.StandardChoices
    )

    PrAQ_2 = models.IntegerField(
        label = "To get the work done, sometimes prescribed audit procedures are neglected.",
        choices = Constants.StandardChoices
    )

    PrAQ_3 = models.IntegerField(
        label = "If there are not enough colleagues for the work that needs to be done, audit procedures are followed less strictly.",
        choices = Constants.StandardChoices
    )

    # Time Pressure at regular work

    TP_1 = models.IntegerField(
        label = "In my work, I have to do task for which I do not have enough time to conduct them properly.",
        choices = Constants.StandardChoices
    )

    TP_2 = models.IntegerField(
        label = "In my work, I divide my time well over the different tasks that I have to do.",
        choices = Constants.StandardChoices
    )

    TP_3 = models.IntegerField(
        label = "In my job, I experience time pressure.",
        choices = Constants.StandardChoices
    )

    # Psychological Ownership at regular work

    PO_1 = models.IntegerField(
        label = "I feel a high degree of psychological ownership over the work that I do.",
        choices = Constants.StandardChoices
    )

    PO_2 = models.IntegerField(
        label = "The work I conduct during audits, is MY work.",
        choices = Constants.StandardChoices
    )

    PO_3 = models.IntegerField(
        label = "If someone gives me a compliment about my work, it feels as a personal compliment.", #anders
        choices = Constants.StandardChoices
    )

    C_1 = models.IntegerField(
        label = "In general, I experience a lot of control over the tasks that I conduct.",
        choices = Constants.StandardChoices
    )

    C_2 = models.IntegerField(
        label = "I have a high degree of influence over the tasks I conduct during my work.",
        choices = Constants.StandardChoices
    )

    C_3 = models.IntegerField(
        label = "I have a high degree of influence over the speed and order in which I conduct tasks at work.",
        choices = Constants.StandardChoices
    )

    K_1 = models.IntegerField(
        label = "I have a deep understanding of the tasks that I conduct at my job",
        choices = Constants.StandardChoices
    )

    K_2 = models.IntegerField(
        label = "I know a lot about what is happening on-the-job.",
        choices = Constants.StandardChoices
    )

    K_3 = models.IntegerField(
        label = "I have a thorough knowledge of the tasks that I conduct at my job.",
        choices = Constants.StandardChoices
    )

    I_1 = models.IntegerField(
        label = "In general, I invest a lot of effort into my job.",
        choices = Constants.StandardChoices
    )

    I_2 = models.IntegerField(
        label = "I invest a large part of my energy into my job.",
        choices = Constants.StandardChoices
    )

    I_3 = models.IntegerField(
        label = "I invest a lot of time to gain knowledge about the tasks that I conduct.",
        choices = Constants.StandardChoices
    )

    TC = models.IntegerField(
        label = "In a typical audit, I start more often with an easy than a difficult task.",
        choices = Constants.StandardChoices
    )

    # Big 5

    Big1 = models.IntegerField(
        label = "Extravert, Enthusiastic",
        choices = Constants.StandardChoices
    )

    Big2 = models.IntegerField(
        label = "Critical, Quarrelsome",
        choices = Constants.StandardChoices
    )

    Big3 = models.IntegerField(
        label = "Dependable, Self-disciplined",
        choices = Constants.StandardChoices
    )

    Big4 = models.IntegerField(
        label = "Anxious, Easily Upset",
        choices = Constants.StandardChoices
    )

    Big5 = models.IntegerField(
        label = "Open to New Experiences, Complex",
        choices = Constants.StandardChoices
    )

    Big6 = models.IntegerField(
        label = "Reserved, Quiet",
        choices = Constants.StandardChoices
    )

    Big7 = models.IntegerField(
        label = "Sympathetic, Warm",
        choices = Constants.StandardChoices
    )

    Big8 = models.IntegerField(
        label = "Disorganized, Careless",
        choices = Constants.StandardChoices
    )

    Big9 = models.IntegerField(
        label = "Calm, Emotionally Stable",
        choices = Constants.StandardChoices
    )

    Big10 = models.IntegerField(
        label = "Conventional, Uncreative",
        choices = Constants.StandardChoices
    )

    # Demographics
    Age = models.IntegerField(label="What is your age?", min=17, max=67, blank=True)

    Gender = models.IntegerField(
        label="Wat is your gender?",
        choices=[
            [1, 'Male'],
            [2, 'Female'],
            [3, 'Other'],
            [4, 'Prefer not to say'],
        ]
    )

    WorkExp = models.IntegerField(label="How many months of work experience as auditor do you have?", min=0, max=480, blank=True)

    Big4_question = models.IntegerField(
        label="For which type of accounting firm do you work?",
        choices = [
            [1, 'A Big-4 office'],
            [2, 'A Non-Big-4 office'],
            [3, 'I do not work for an accounting firm.']
        ]
    )

    Leave_Office = models.IntegerField(
        label = 'How frequent do you think about leaving your accounting firm within three years?',
        choices = [
            [1, 'Almost never'],
            [2, 'Rarely'],
            [3, 'Sometimes'],
            [4, 'Often'],
            [5, 'Almost always']
        ]
    )

    Leave_Profession = models.IntegerField(
        label = 'How frequent do you think about leaving the profession within three years?',
        choices = [
            [1, 'Almost never'],
            [2, 'Rarely'],
            [3, 'Sometimes'],
            [4, 'Often'],
            [5, 'Almost always']
        ]
    )
    # Math Problems

    math1 = models.IntegerField(
        label="The host at a cocktail party has to divide seats between himself and five guests, how many different combinations can he make if he chooses a last spot for himself?",
        choices = [
            [1, 6],
            [2, 15],
            [3, 21],
            [4, 120],
            [5, 720],
            [6, "Skip question"]
        ],
        widget = widgets.RadioSelectHorizontal
    )

    math2 = models.IntegerField(
        label="A chemist has 10 liters of a solution that naturally contains 10 percent nitric acid. He wants to dilute the solution to 4 procent nitric acid by adding water. How many liters of water does he need to add?",
        choices = [
            [1, 15],
            [2, 18],
            [3, 20],
            [4, 25],
            [5, 26],
            [6,"Skip question"]
        ],
        widget = widgets.RadioSelectHorizontal
    )

    # Payment

    SNR = models.StringField(label='Please fill in your SNR number such that you can receive an e-mail with the payment details:')

    feedback = models.TextField(label="In case you have any feedback, you can write it in the textbox below.", blank=True)

