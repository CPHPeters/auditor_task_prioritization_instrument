from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import time
import random


class Intro(Page):
    form_model = 'player'
    form_fields = [
        'accept_conditions',
        'name_PO'
    ]
    def before_next_page(self):
        self.player.random = random.choice([0, 1])

class Scenario(Page):
    pass

class Scenario_2(Page):
    form_model = 'player'
    form_fields = ['understanding']

    def error_message(self, values):
        if values['understanding'] != 2:
            return 'Je antwoord is incorrect. Lees alsjeblieft nogmaals het scenario en beantwoordt de vraag.'

class Scenario_3(Page):
    form_model = 'player'
    form_fields = [
        'inspectinfo',
        'cq1',
        'cq2'
    ]

class Scenario_4(Page):
    def before_next_page(self):
        if self.player.treat > 2:
            self.participant.vars['expirytime'] = time.time() + 5 * 60 #low tp
        else:
            self.participant.vars['expirytime'] = time.time() + 3 * 60 #high tp
    pass

class Training(Page):
    form_model = 'player'
    form_fields = ['screenshot_training']

    def get_timeout_seconds(self):
        return self.participant.vars['expirytime'] - time.time()

class Task(Page):
    form_model = 'player'
    form_fields = [
        'documentatie',
        'summary_figure'
    ]

class Judgment(Page):
    form_model = 'player'
    form_fields = ['difficulty_slider']

class Choice(Page):
    form_model = 'player'
    form_fields = ['task_choice']
    # Participant has 8 or 12 minutes to complete the two audit tasks
    def before_next_page(self):
        if self.player.treat > 2:
            self.participant.vars['expiry'] = time.time() + 12 * 60 #low tp
        else:
            self.participant.vars['expiry'] = time.time() + 8 * 60 #high tp

class MyPage(Page):
    pass

class Page(Page):
    pass

class Robofer_P1(Page):
    form_model = 'player'
    form_fields = [
        'mistakes_robofer',
        'robofer_estimate'
    ]

    # Only display the page if the player chooses the Robofer as first task
    def is_displayed(self):
        return self.player.task_choice == False

    # Adjust for time spent
    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()
    timer_text = 'Tijd over om de audit engagement te voltooien:'


class Feeder_2000_P1(Page):
    form_model = 'player'
    form_fields = [
        'mistakes_feeder',
        'feeder_estimate'
    ]

    # Only display the page if the player chooses the Robofer as first task
    def is_displayed(self):
        return self.player.task_choice == True

    # Adjust for time spent
    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()
    timer_text = 'Tijd over om de audit engagement te voltooien:'


class Robofer_P2(Page):
    form_model = 'player'
    form_fields = [
        'mistakes_robofer',
        'robofer_estimate'
    ]

    def is_displayed(self):
        return self.player.task_choice == True

    # Adjust for time spent
    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()
    timer_text = 'Tijd over om de audit engagement te voltooien:'

class Feeder_2000_P2(Page):
    form_model = 'player'
    form_fields = [
        'mistakes_feeder',
        'feeder_estimate'
    ]

    def is_displayed(self):
        return self.player.task_choice == False

    # Adjust for time spent
    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()
    timer_text = 'Tijd over om de audit engagement te voltooien:'

class MC_1(Page):
    form_model = 'player'
    form_fields = [
        'pom_1_1',
        'pom_1_2',
        'pom_1_3',
        'pom_1_4'
    ]

class MC_2(Page):
    form_model = 'player'
    form_fields = [
        'pom_2_1',
        'pom_2_2',
        'pom_2_3',
        'pom_2_4'
    ]

class MC_3(Page):
    form_model = 'player'
    form_fields = [
        'pom_3_1',
        'pom_3_2',
        'pom_3_3',
        'pom_3_4',
        'pom_3_5'
    ]

class MC_4(Page):
    form_model = 'player'
    form_fields = [
        'pom_4_1',
        'pom_4_2',
        'pom_4_3',
        'pom_4_4',
    ]

class MC_5(Page):
    form_model = 'player'
    form_fields= [
        'IE_1',
        'IE_2',
        'BNS_1',
        'BNS_2',
        'BNS_3',
        'accountability',
        'po_check',
        'difficulty_consideration',
        'robofer_difficulty',
        'feeder_difficulty',
        'both_difficulty',
        'see_spreadsheet',
        'time_consideration',
        'learning_effect'
    ]

    def get_form_fields(self):
        fields = self.form_fields
        random.shuffle(fields)
        return fields

class Personality_Variables(Page):
    form_model = 'player'
    form_fields = [
        'need_for_cognition_1',
        'need_for_cognition_2',
        'need_for_cognition_3',
        'PrAQ_1',
        'PrAQ_2',
        'PrAQ_3',
        'C_1',
        'C_2',
        'C_3',
        'I_1',
        'I_2',
        'I_3',
        'K_1',
        'K_2',
        'K_3',
        'WE_1',
        'WE_2',
        'WE_3',
        'TC',
        'PO_1',
        'PO_2',
        'PO_3',
        'Leave_Office',
        'Leave_Profession',
        'experience_dcf',
        'experience_fve'
    ]

    def get_form_fields(self):
        fields = self.form_fields
        random.shuffle(fields)
        return fields

class Big_5(Page):
    form_model = 'player'
    form_fields = [
        'Big1',
        'Big2',
        'Big3',
        'Big4',
        'Big5',
        'Big6',
        'Big7',
        'Big8',
        'Big9',
        'Big10',
    ]

    def get_form_fields(self):
        fields = self.form_fields
        random.shuffle(fields)
        return fields

class After_Audit(Page):
    form_model = 'player'
    form_fields = ['orderDemographics']

class Demographics_P1(Page):
    def is_displayed(self):
        return self.player.orderDemographics == True

    form_model = 'player'
    form_fields= [
        'Age',
        'Gender',
        'WorkExp',
        'Big4_question',
        'SNR',
    ]

class Demographics_P2(Page):
    def is_displayed(self):
        return self.player.orderDemographics == False

    form_model = 'player'
    form_fields= [
        'Age',
        'Gender',
        'WorkExp',
        'Big4_question',
        'SNR',
    ]

class Math_Problems_P1(Page):
    def is_displayed(self):
        return self.player.orderDemographics == False

    form_model = 'player'
    form_fields = [
        'math1',
        'math2'
    ]


class Math_Problems_P2(Page):
    def is_displayed(self):
        return self.player.orderDemographics == True

    form_model = 'player'
    form_fields = [
        'math1',
        'math2'
    ]

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        pass

class Results(Page):
    pass

class Thanks(Page):
    form_model = 'player'
    form_fields = ['feedback']

page_sequence = [
    Intro,
    Scenario,
    Scenario_2,
    Scenario_3,
    Scenario_4,
    Training,
    Task,
    Judgment,
    Choice,
    Robofer_P1,
    Feeder_2000_P1,
    Robofer_P2,
    Feeder_2000_P2,
    MC_1,
    MC_2,
    MC_3,
    MC_4,
    MC_5,
    Personality_Variables,
    Big_5,
    After_Audit,
    Demographics_P1,
    Math_Problems_P1,
    Demographics_P2,
    Math_Problems_P2,
    Thanks
]