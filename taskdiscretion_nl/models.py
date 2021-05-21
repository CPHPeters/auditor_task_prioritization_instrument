import random
import itertools

from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Christian Peters and Bart Dierynck'

doc = """
Ontwikkeld door Bart Dierynck en Christian Peters, Tilburg University. Voor vragen kunt u contact opnemen met Christian Peters 
(c.p.h.peters@tilburguniversity.edu).
"""


class Constants(BaseConstants):
    name_in_url = 'taskdiscretion'
    players_per_group = None
    num_rounds = 1
    StandardChoices=[
        [1, 'Helemaal oneens'],
        [2, 'Oneens'],
        [3, 'Beetje mee oneens'],
        [4, 'Noch mee oneens, noch mee eens'],
        [5, 'Beetje mee eens'],
        [6, 'Eens'],
        [7, 'Helemaal eens'],
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
        label = "Selecteer de stelling die het meest van toepassing is op deze situatie:",
        choices = [
            [1, 'CMG Machines bezit twee patenten en verleent de exclusieve rechten om de gepatenteerde machines te vervaardigen en te gebruiken aan Agrifirm, in ruil ontvangt CMG Machines royaltybetalingen.'],
            [2, 'Agrifirm bezit twee patenten en verleent de exclusieve rechten om de gepatenteerde machines te vervaardigen en te gebruiken aan CMG Machines, in ruil ontvangt Agrifirm royaltybetalingen.'],
            [3, 'Agrifirm heeft CMG Machines overgenomen en mag daarom de patenten in haar boeken activeren.']
        ],
        widget = widgets.RadioSelect
    )

    cq1 = models.IntegerField(
        label = "Een daling in het disconteerpercentage van Agrifirm:",
        choices=[
            [1, 'Zorgt voor een stijging van de contante waarde van de kasstromen.'],
            [2, 'Zorgt voor een daling van de contante waarde van de kasstromen.'],
            [3, 'Heeft geen effect op de contante waarde van de kasstromen.']
        ],
        widget = widgets.RadioSelect
    )
    cq2 = models.IntegerField(
        label = "Een daling in het royalty-percentage dat Agrifirm rekent:",
        choices = [
            [1, 'Zorgt voor een stijging van de contante waarde van de kasstromen.'],
            [2, 'Zorgt voor een daling van de contante waarde van de kasstromen.'],
            [3, 'Heeft geen effect op de contante waarde van de kasstromen.']
        ],
        widget = widgets.RadioSelect
    )

    # PO (Training)

    name_PO = models.StringField(label="Vul hier je voornaam in:", blank=False)

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

    mistakes_robofer = models.TextField(label="Vul de celnummers in (bv, B2) waarvan je denkt dat Agrifirm een fout heeft gemaakt:", blank=True)
    robofer_estimate = models.FloatField(label="Vul het fair value bedrag in waarvan jij denkt dat het de waarde van de patenten het meest accuraat presenteert gegeven de parameters:", blank=True)
    mistakes_feeder = models.TextField(label="Vul de celnummers (bv, B2) in waarvan je denkt dat Agrifirm een fout heeft gemaakt:", blank=True)
    feeder_estimate = models.FloatField(label="Vul het fair value bedrag in waarvan jij denkt dat het de waarde van de patenten het meest accuraat presenteert gegeven de parameters:", blank=True)

    # Manipulation Checks

    time_consideration = models.IntegerField(
        label = "Toen ik moest besluiten over welke audit taak ik als eerste wilde doen, heeft de verwachte tijd om de audit taak te voltooien mijn keuze beïnvloed.",
        choices = Constants.StandardChoices
    )

    learning_effect = models.IntegerField(
        label = "Toen ik moest besluiten over welke audit taak ik als eerste wilde doen, hebben de verwachte leereffecten van de audit taak mijn keuze beïnvloed.",
        choices = Constants.StandardChoices
    )

    choice_method_1 = models.IntegerField(
        label = "Toen ik moest besluiten over welke audit taak ik als eerste wilde doen, nam ik in overweging dat ik in ieder geval 1 taak wilde afronden binnen de tijdslimiet van 8 minuten.",
        choices = Constants.StandardChoices
    )

    choice_method_2 = models.IntegerField(
        label = "Toen ik moest besluiten welke audit taak ik als eerste wilde doen, had ik de aanname dat ik beide taken binnen de tijslimiet van 8 minuten zou kunnen afronden.",
        choices =Constants.StandardChoices
    )

    pom_1_1 = models.IntegerField(
        label = "In dit audit team wordt betrokkenheid bij de audit taken als een belangrijke waarde beschouwd.",
        choices = Constants.StandardChoices
    )

    pom_1_2 = models.IntegerField(
        label = "Binnen dit audit team krijg je weinig inspraak over hoe de audit taken werden aangepakt.",
        choices = Constants.StandardChoices
    )

    pom_1_3 = models.IntegerField(
        label = "In dit audit team kun je inzichten die je eerder hebt opgedaan gebruiken bij het uitvoeren van audit taken.",
        choices = Constants.StandardChoices
    )

    pom_1_4 = models.IntegerField(
        label = "Toen ik mij vertrouwd maakte met de audit taken, ervaarde ik tijdsdruk.",
        choices = Constants.StandardChoices
    )

    pom_2_1 = models.IntegerField(
        label = "Toen ik documenteerde waarom de patenten tegen fair value gewaardeerd worden, had ik weinig invloed op de manier waarop dit gebeurde.",
        choices = Constants.StandardChoices
    )

    pom_2_2 = models.IntegerField(
        label = "Ik voel een hoge mate van persoonlijke betrokkenheid bij de documentatie die ik heb geschreven.",
        choices = Constants.StandardChoices
    )

    pom_2_3 = models.IntegerField(
        label = "Als iemand mij zou complimenteren over de documentatie die ik heb geschreven, zou dat voelen als een persoonlijk compliment.",
        choices = Constants.StandardChoices
    )

    pom_2_4 = models.IntegerField(
        label = "Toen ik documenteerde waarom de patenten tegen fair value gewaardeerd worden, voelde ik me betrokken bij deze documentatie.",
        choices = Constants.StandardChoices
    )

    pom_3_1 = models.IntegerField(
        label = "Toen ik de audit taken uitvoerde, had ik het gevoel zelf te kunnen beslissen hoe ik deze uitvoerde.",
        choices = Constants.StandardChoices
    )

    pom_3_2 = models.IntegerField(
        label = "Toen ik de audit taken uitvoerde, voelde ik een hoge mate van persoonlijke betrokkenheid bij het werk dat ik deed.",
        choices = Constants.StandardChoices
    )

    pom_3_3 = models.IntegerField(
        label = "Als iemand mij zou complimenteren over de audit taken die ik heb gedaan, zou dat voelen als een persoonlijk compliment.",
        choices = Constants.StandardChoices
    )

    pom_3_4 = models.IntegerField(
        label = "Toen ik de audit taken uitvoerde, ervaarde ik tijdsdruk",
        choices = Constants.StandardChoices
    )

    pom_3_5 = models.IntegerField(
        label = "Ik had het gevoel te weinig tijd te hebben om de audit taken echt goed uit te voeren.",
        choices = Constants.StandardChoices
    )

    pom_4_1 = models.IntegerField(
        label = "Ik voel een hoge mate van persoonlijke betrokkenheid bij het werk dat ik heb gedaan in deze audit engagement.",
        choices = Constants.StandardChoices
    )

    pom_4_2 = models.IntegerField(
        label = "De taken die ik heb gedaan beschouw ik als mijn eigen werk.",
        choices = Constants.StandardChoices
    )

    pom_4_3 = models.IntegerField(
        label = "Ik heb het gevoel dat de taken die ik heb gedaan mijn eigen werk waren.",
        choices = Constants.StandardChoices
    )

    pom_4_4 = models.IntegerField(
        label = "Ik heb het gevoel dat het werk gedaan in de audit engagement van mij is.",
        choices = Constants.StandardChoices
    )

    po_check = models.IntegerField(
        label = "Het documenteren beschouw ik als een onderdeel van de audit taken.",
        choices = Constants.StandardChoices
    )
    difficulty_consideration = models.IntegerField(
        label = "Toen ik moest besluiten welke audit taak ik eerste wilde doen, nam ik de moeilijkheidsgraad van de taken in overweging.",
        choices = Constants.StandardChoices
    )

    robofer_difficulty = models.IntegerField(
        label = "De audit van het Robofer patent was moeilijk.",
        choices = Constants.StandardChoices
    )

    feeder_difficulty = models.IntegerField(
        label = "De audit van het Feeder 2000 patent was moeilijk.",
        choices = Constants.StandardChoices
    )

    both_difficulty = models.IntegerField(
        label = "De audit van het Robofer patent was moeilijker dan die van het Feeder 2000 patent.",
        choices = Constants.StandardChoices
    )

    # Accountability

    accountability = models.IntegerField(
        label = "Tijdens de audit voelde ik me verantwoordelijk voor de teamleider.",
        choices = Constants.StandardChoices
    )

    # Interest and Enjoyment Questions:

    IE_1 = models.IntegerField(
        label = "Ik vond het leuk om de audit taken te doen.",
        choices = Constants.StandardChoices
    )

    IE_2 = models.IntegerField(
        label = "Het was lastig om gedurende lange tijd mijn aandacht bij de audit taken te houden.",
        choices = Constants.StandardChoices
    )

    # Work Engagement Questions

    WE_1 = models.IntegerField(
        label = "Op mijn werk bruis ik van energie.",
        choices = Constants.StandardChoices
    )

    WE_2 = models.IntegerField(
        label = "Mijn werk inspireert mij.",
        choices = Constants.StandardChoices
    )

    WE_3 = models.IntegerField(
        label = "Als ik 's morgens opsta, heb ik zin om naar mijn werk te gaan.",
        choices = Constants.StandardChoices
    )

    # Need for Cognition: taken from scale Cacioppo, J.T. and Petty, R.E. (1982)
    need_for_cognition_1 = models.IntegerField(
        label="Ik doe graag taken die weinig nadenken vergen, op het moment dat je ze geleerd hebt.",
        choices= Constants.StandardChoices
    )

    need_for_cognition_2 = models.IntegerField(
        label="Ik heb graag de verantwoordelijkheid over een situatie die veel nadenken vergt.",
        choices= Constants.StandardChoices
    )

    need_for_cognition_3 = models.IntegerField(
        label="Ik ben trots op de uitkomsten van mijn redeneringen.",
        choices= Constants.StandardChoices
    )

    # Ervaring met taken

    experience_dcf = models.IntegerField(
        label="Hoe vaak heb je een discounted cash flow model geaudit?",
        choices = [
            [1, 'Nooit'],
            [2, 'Zelden'],
            [3, 'Soms'],
            [4, 'Vaak'],
            [5, 'Heel Vaak']
        ]
    )

    experience_fve = models.IntegerField(
        label="Hoe vaak heb je een fair value estimate geaudit?",
        choices = [
            [1, 'Nooit'],
            [2, 'Zelden'],
            [3, 'Soms'],
            [4, 'Vaak'],
            [5, 'Heel Vaak']
        ]
    )

    see_spreadsheet = models.IntegerField(
        label = "Ik kon de Excel spreadsheets bekijken en kon er in werken.",
        choices = [
            [1, 'Waar'],
            [2, 'Onwaar']
        ]
    )

    # Basic Needs Satisfaction (Deci et al., 2001)

    # Autonomy

    BNS_1 = models.IntegerField(
        label = "Ik had het gevoel dat ik veel invloed had op hoe ik de audit engagement uitvoerde tijdens de studie.",
        choices = Constants.StandardChoices
    )

    BNS_2 = models.IntegerField(
        label = "Tijdens de audit taken had ik het gevoel dat ik vooral moest doen wat me werd opgedragen.",
        choices=Constants.StandardChoices
    )

    BNS_3 = models.IntegerField(
        label = "Er waren weinig mogelijkheden voor mij om zelf te bepalen hoe ik de audit engagement deed tijdens de studie.",
        choices=Constants.StandardChoices
    )

    BNS_4 = models.IntegerField(
        label = "Ik had het gevoel iets geleerd te hebben na het werken aan de audit taken.",
        choices=Constants.StandardChoices
    )

    BNS_5 = models.IntegerField(
        label = "Gedurende de audit taken kreeg ik weinig kans om mijn eigen capaciteiten te tonen.",
        choices=Constants.StandardChoices
    )

    BNS_6 = models.IntegerField(
        label = "Gedurende het werken aan de audit taken, voelde ik me niet erg bekwaam.",
        choices=Constants.StandardChoices
    )

    # Priority of Audit Quality

    PrAQ_1 = models.IntegerField(
        label = "Wanneer ik onder hoge tijdsdruk moet werken, gaat de voorkeur uit naar het zo snel mogelijk uitvoeren van het werk, ook als dit mogelijk leidt tot een audit van mindere kwaliteit.",
        choices=Constants.StandardChoices
    )

    PrAQ_2 = models.IntegerField(
        label = "Om het werk gedaan te krijgen, worden voorgeschreven (audit) procedures soms genegeerd.",
        choices = Constants.StandardChoices
    )

    PrAQ_3 = models.IntegerField(
        label = "Indien er te weinig mensen in het team aanwezig zijn volgens het werk dat moet gebeuren, worden de audit procedures minder strikt nageleefd.",
        choices = Constants.StandardChoices
    )

    # Time Pressure at regular work

    TP_1 = models.IntegerField(
        label = "In mijn werk krijg ik taken waarvoor ik niet genoeg tijd heb om deze uit te voeren.",
        choices = Constants.StandardChoices
    )

    TP_2 = models.IntegerField(
        label = "In mijn werk verdeel ik mijn tijd goed over de verschillende taken die ik zou moeten doen.",
        choices = Constants.StandardChoices
    )

    TP_3 = models.IntegerField(
        label = "In mijn werk ervaar ik tijdsdruk.",
        choices = Constants.StandardChoices
    )

    # Psychological Ownership at regular work

    PO_1 = models.IntegerField(
        label = "Ik voel een hoge mate van persoonlijk eigenaarschap over het werk dat ik doe.",
        choices = Constants.StandardChoices
    )

    PO_2 = models.IntegerField(
        label = "Het werk dat ik binnen het accountantskantoor doe is MIJN werk.",
        choices = Constants.StandardChoices
    )

    PO_3 = models.IntegerField(
        label = "Als iemand mij een compliment geeft over mijn werk, voelt dat als een persoonlijk compliment.", #anders
        choices = Constants.StandardChoices
    )

    C_1 = models.IntegerField(
        label = "Over het algemeen heb ik veel invloed over hoe ik mijn taken uitvoer.",
        choices = Constants.StandardChoices
    )

    C_2 = models.IntegerField(
        label = "Ik heb een grote mate van invloed over de taken die ik doe op mijn werk.",
        choices = Constants.StandardChoices
    )

    C_3 = models.IntegerField(
        label = "Ik heb een grote mate van invloed op het tempo en de volgorde waarmee ik op mijn werk de taken uitvoer.",
        choices = Constants.StandardChoices
    )

    K_1 = models.IntegerField(
        label = "Ik heb een diepgaande kennis van de taken die ik op mijn werk uitvoer.",
        choices = Constants.StandardChoices
    )

    K_2 = models.IntegerField(
        label = "Ik ben erg bekend met wat er gaande is omtrent mijn werk.",
        choices = Constants.StandardChoices
    )

    K_3 = models.IntegerField(
        label = "Ik heb een grondig begrip van de taken die ik op mijn werk moet doen.",
        choices = Constants.StandardChoices
    )

    I_1 = models.IntegerField(
        label = "Over het algemeen investeer ik veel in mijn baan.",
        choices = Constants.StandardChoices
    )

    I_2 = models.IntegerField(
        label = "Ik investeer een groot deel van mijn energie in mijn baan.",
        choices = Constants.StandardChoices
    )

    I_3 = models.IntegerField(
        label = "Ik investeer veel tijd om kennis op te doen van de taken die ik uitvoer.",
        choices = Constants.StandardChoices
    )

    TC = models.IntegerField(
        label = "In een typische audit begin ik vaker met een makkelijke taak dan met een moeilijke taak.",
        choices = Constants.StandardChoices
    )

    # Big 5

    Big1 = models.IntegerField(
        label = "Extravert, Enthousiast",
        choices = Constants.StandardChoices
    )

    Big2 = models.IntegerField(
        label = "Kritisch, Assertief",
        choices = Constants.StandardChoices
    )

    Big3 = models.IntegerField(
        label = "Betrouwbaar, Zelfdiscipline",
        choices = Constants.StandardChoices
    )

    Big4 = models.IntegerField(
        label = "Angstig, Snel Verdrietig",
        choices = Constants.StandardChoices
    )

    Big5 = models.IntegerField(
        label = "Open voor Nieuwe Ervaringen, Complex",
        choices = Constants.StandardChoices
    )

    Big6 = models.IntegerField(
        label = "Gereserveerd, Stil",
        choices = Constants.StandardChoices
    )

    Big7 = models.IntegerField(
        label = "Sympathiek, Warm",
        choices = Constants.StandardChoices
    )

    Big8 = models.IntegerField(
        label = "Ongeorganiseerd, Zorgeloos",
        choices = Constants.StandardChoices
    )

    Big9 = models.IntegerField(
        label = "Rustig, Emotioneel Stabiel",
        choices = Constants.StandardChoices
    )

    Big10 = models.IntegerField(
        label = "Conventioneel, Oncreatief",
        choices = Constants.StandardChoices
    )

    # Demographics
    Age = models.IntegerField(label="Wat is je leeftijd?", min=17, max=67, blank=True)

    Gender = models.IntegerField(
        label="Wat is je geslacht?",
        choices=[
            [1, 'Man'],
            [2, 'Vrouw'],
            [3, 'Anders'],
            [4, 'Wil liever niet zeggen.'],
        ]
    )

    WorkExp = models.IntegerField(label="Hoeveel maanden of werkervaring als auditor heb je?", min=0, max=480, blank=True)

    Big4_question = models.IntegerField(
        label="Voor welk type accountantskantoor werk je?",
        choices = [
            [1, 'Een Big-4 kantoor'],
            [2, 'Een Niet-Big-4 kantoor'],
            [3, 'Ik werk niet voor een accountantskantoor.']
        ]
    )

    Leave_Office = models.IntegerField(
        label = 'Hoe frequent komt de gedachte bij je op om je huidige organisatie te verlaten binnen drie jaar?',
        choices = [
            [1, 'Bijna nooit'],
            [2, 'Zelden'],
            [3, 'Soms'],
            [4, 'Vaak'],
            [5, 'Bijna altijd']
        ]
    )

    Leave_Profession = models.IntegerField(
        label = 'Hoe frequent komt de gedachte bij je op om de audit professie te verlaten binnen drie jaar?',
        choices = [
            [1, 'Bijna nooit'],
            [2, 'Zelden'],
            [3, 'Soms'],
            [4, 'Vaak'],
            [5, 'Bijna altijd']
        ]
    )
    # Math Problems

    math1 = models.IntegerField(
        label="De gastheer op een cocktailparty moet de zitplaatsen verdelen tussen hemzelf en vijf andere gasten in een enkele rij. Hoeveel verschillende mogelijkheden zijn er als de gastheer steeds dezelfde plaats voor hemzelf kiest?",
        choices = [
            [1, 6],
            [2, 15],
            [3, 21],
            [4, 120],
            [5, 720],
            [6, "Sla vraag over"]
        ],
        widget = widgets.RadioSelectHorizontal
    )

    math2 = models.IntegerField(
        label="Een scheikundige heeft 10 liter van een oplossing die van nature 10 procent salpeterzuur bevat. Hij wil deze oplossing verdunnen tot 4 procent salpeterzuur door water toe te voegen. Hoeveel liter water moet hij toevoegen?",
        choices = [
            [1, 15],
            [2, 18],
            [3, 20],
            [4, 25],
            [5, 26],
            [6,"Sla vraag over"]
        ],
        widget = widgets.RadioSelectHorizontal
    )

    # Payment

    SNR = models.StringField(label='Vul hier je SNR nummer in en je zult een e-mail ontvangen omtrent de betaalprocedure:')

    feedback = models.TextField(label="Mocht je feedback over deze studie hebben, laat deze dan achter in het tekstvak.", blank=True)

