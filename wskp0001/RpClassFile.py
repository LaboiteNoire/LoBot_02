"""
Rp Class File
"""
import StorageFile as st
normal_template = {"strength" : (0,0),"dexterity" : (0,0),"bleeding" : (0,0) ,"posture" : (0,0) ,
            "constitution" : (0,0),"evasion" : (0,0),
            "intellect" : (0,0),"charisma" : (0,0) ,"wisdom" : (0,0)}
import copy
class StatisticsClass():
    def __init__(self, name : str ,statistic=normal_template):
        self.strength = statistic["strength"]
        self.dexterity = statistic["dexterity"]
        self.bleeding = statistic["bleeding"]
        self.posture = statistic["posture"]
        self.constitution = statistic["constitution"]
        self.evasion = statistic["evasion"]
        self.intellect = statistic["intellect"]
        self.charisma = statistic["charisma"]
        self.wisdom = statistic["wisdom"]
        self.name = name
        pass
enchance_template = [StatisticsClass(""),StatisticsClass(""),StatisticsClass(""),StatisticsClass(""),StatisticsClass(""),
                     StatisticsClass(""),StatisticsClass(""),StatisticsClass(""),StatisticsClass(""),StatisticsClass("")]
levelling_template = [StatisticsClass(""),StatisticsClass(""),StatisticsClass(""),StatisticsClass(""),StatisticsClass(""),
                      StatisticsClass(""),StatisticsClass(""),StatisticsClass(""),StatisticsClass(""),StatisticsClass(""),
                      StatisticsClass(""),StatisticsClass(""),StatisticsClass(""),StatisticsClass(""),StatisticsClass(""),
                      StatisticsClass(""),StatisticsClass(""),StatisticsClass(""),StatisticsClass(""),StatisticsClass(""),
                      StatisticsClass("")]
class ItemClass(StatisticsClass):
    def __init__(self, name : str ,presentation : str ,statistic=normal_template):
        super().__init__(name,statistic)
        self.description = presentation
        pass
class NewItemClass():
    def __init__(self, name : str ,presentation : str ,image_path="",quantity=1,price=0):
        self.image_path = image_path
        self.quantity = quantity
        self.name = name
        self.description = presentation
        self.price = price
        pass
class ConsumableClass(NewItemClass):
    def __init__(self, name : str ,presentation : str ,life : int ,image_path="",quantity=1,price=0):
        super().__init__(name,presentation,image_path,quantity,price)
        self.life = life
        pass
class CompetenceClass(StatisticsClass):
    def __init__(self, name : str ,presentation : str ,competence_type : tuple ,cooldown : int ,state : tuple ,attack_level : int ,normal_stats=normal_template ,self_buff=StatisticsClass(""),buff=StatisticsClass("")):
        super().__init__(name,normal_stats)
        self.level = attack_level
        self.type = competence_type
        self.state = state
        self.presentation = presentation
        self.normal_statistic = normal_stats
        self.competence_cooldown = cooldown
        self.last_utilisation = -self.competence_cooldown
        self.self_buff = self_buff
        self.buff = buff
        pass
class BuffClass(StatisticsClass):
    def __init__(self,cooldown : int ,basic_statistiques=StatisticsClass("")):
        super().__init__("buff")
        self.cooldown = cooldown
        self.last_utilisation = st.getTick()
        self.strength = basic_statistiques.strength
        self.dexterity = basic_statistiques.dexterity
        self.bleeding = basic_statistiques.bleeding
        self.posture = basic_statistiques.posture
        self.constitution = basic_statistiques.constitution
        self.evasion = basic_statistiques.evasion
        self.intellect = basic_statistiques.intellect
        self.charisma = basic_statistiques.charisma
        self.wisdom = basic_statistiques.wisdom
        pass
class MagicalItemClass(NewItemClass):
    def __init__(self, name : str ,presentation : str ,competence , image_path="",quantity=1,price=0):
        super().__init__(name,presentation,image_path,quantity,price)
        self.competence = copy.deepcopy(competence)
        pass
class MagicalConsumableClass(NewItemClass):
    def __init__(self, name : str ,presentation : str ,life : int , competence , image_path="",quantity=1,price=0):
        super().__init__(name,presentation,image_path,quantity,price)
        self.life = life
        self.competence = copy.deepcopy(competence)
        pass
class WeaponTypeClass(StatisticsClass):
    def __init__(self,name : str ,description : str ,basic_statistiques=StatisticsClass("") , weapon_competences={} , modifier="strength" ,imagepath="https://media.discordapp.net/attachments/1002657461842497597/1005621372438986903/Inconnu.png?width=225&height=225"):
        super().__init__(name)
        self.description = description
        self.image_path = imagepath
        self.modifier = modifier
        self.competences = weapon_competences
        self.strength = basic_statistiques.strength
        self.dexterity = basic_statistiques.dexterity
        self.bleeding = basic_statistiques.bleeding
        self.posture = basic_statistiques.posture
        self.constitution = basic_statistiques.constitution
        self.evasion = basic_statistiques.evasion
        self.intellect = basic_statistiques.intellect
        self.charisma = basic_statistiques.charisma
        self.wisdom = basic_statistiques.wisdom
        pass
class AccessoryClassTypeClass(StatisticsClass):
    def __init__(self,name : str ,description : str ,accessory_competences={} , modifier="strength" ,imagepath="https://media.discordapp.net/attachments/1002657461842497597/1005621372438986903/Inconnu.png?width=225&height=225"):
        super().__init__(name)
        self.description = description
        self.image_path = imagepath
        self.modifier = modifier
        self.competences = accessory_competences
        pass
class ArmorClassTypeClass(StatisticsClass):
    def __init__(self,name : str ,description : str ,basic_statistiques=StatisticsClass(""),imagepath="https://media.discordapp.net/attachments/1002657461842497597/1005621372438986903/Inconnu.png?width=225&height=225"):
        super().__init__(name)
        self.description = description
        self.image_path = imagepath
        self.posture = basic_statistiques.posture
        self.constitution = basic_statistiques.constitution
        self.evasion = basic_statistiques.evasion
        pass
class WeaponClass(ItemClass):
    def __init__(self, name : str ,description : str , weapon_level : int , WeaponType=WeaponTypeClass("",""), enchance_type=enchance_template , enchance_name="none"):
        super().__init__(name,description)
        self.enchance_name = enchance_name
        self.level = weapon_level
        self.enchance_type = enchance_type
        self.weapon_type = WeaponType
        self.strength = (self.weapon_type.strength[0] + self.enchance_type[self.level].strength[0] , self.weapon_type.strength[1] + self.enchance_type[self.level].strength[1])
        self.dexterity = (self.weapon_type.dexterity[0] + self.enchance_type[self.level].dexterity[0] , self.weapon_type.dexterity[1] + self.enchance_type[self.level].dexterity[1])
        self.bleeding = (self.weapon_type.bleeding[0] + self.enchance_type[self.level].bleeding[0] , self.weapon_type.bleeding[1] + self.enchance_type[self.level].bleeding[1])
        self.posture = (self.weapon_type.posture[0] + self.enchance_type[self.level].posture[0] , self.weapon_type.posture[1] + self.enchance_type[self.level].posture[1])
        pass
    def updateStatistics(self):
        self.strength = (self.weapon_type.strength[0] + self.enchance_type[self.level].strength[0] , self.weapon_type.strength[1] + self.enchance_type[self.level].strength[1])
        self.dexterity = (self.weapon_type.dexterity[0] + self.enchance_type[self.level].dexterity[0] , self.weapon_type.dexterity[1] + self.enchance_type[self.level].dexterity[1])
        self.bleeding = (self.weapon_type.bleeding[0] + self.enchance_type[self.level].bleeding[0] , self.weapon_type.bleeding[1] + self.enchance_type[self.level].bleeding[1])
        self.posture = (self.weapon_type.posture[0] + self.enchance_type[self.level].posture[0] , self.weapon_type.posture[1] + self.enchance_type[self.level].posture[1])
        pass
    def updateLevel(self, new_level : int):
        self.level = new_level
        self.updateStatistics()
        pass
class AccessoryClass(ItemClass):
    def __init__(self, name : str ,description : str , accesory_level : int , AccessoryType ,enchance_type=enchance_template ,enchance_name="none"):
        super().__init__(name,description)
        self.enchance_name = enchance_name
        self.level = accesory_level
        self.enchance_type = enchance_type
        self.accessory_type = AccessoryType
        self.strength = enchance_type[self.level].strength
        self.dexterity = enchance_type[self.level].dexterity
        self.bleeding = enchance_type[self.level].bleeding
        self.posture = enchance_type[self.level].posture
        self.constitution = enchance_type[self.level].constitution
        self.evasion = enchance_type[self.level].evasion
        self.intellect = enchance_type[self.level].intellect
        self.charisma = enchance_type[self.level].charisma
        self.wisdom = enchance_type[self.level].wisdom
    def updateStatistics(self):
        self.strength = enchance_type[self.level].strength
        self.dexterity = enchance_type[self.level].dexterity
        self.bleeding = enchance_type[self.level].bleeding
        self.posture = enchance_type[self.level].posture
        self.constitution = enchance_type[self.level].constitution
        self.evasion = enchance_type[self.level].evasion
        self.intellect = enchance_type[self.level].intellect
        self.charisma = enchance_type[self.level].charisma
        self.wisdom = enchance_type[self.level].wisdom
        pass
    def updateLevel(self, new_level : int):
        self.level = new_level
        self.updateStatistics()
        pass
class ArmorClass(ItemClass):
    def __init__(self, name : str ,description : str , armor_level : int , ArmorType ,enchance_type=enchance_template , enchance_name="none"):
        super().__init__(name,description)
        self.enchance_name= enchance_name
        self.level = armor_level
        self.enchance_type = enchance_type
        self.armor_type = ArmorType
        self.posture = (self.armor_type.posture[0] + self.enchance_type[self.level].posture[0] , self.armor_type.posture[1] + self.enchance_type[self.level].posture[1])
        self.constitution = (self.armor_type.constitution[0] + self.enchance_type[self.level].constitution[0] , self.armor_type.constitution[1] + self.enchance_type[self.level].constitution[1])
        self.evasion = (self.armor_type.evasion[0] + self.enchance_type[self.level].evasion[0] , self.armor_type.evasion[1] + self.enchance_type[self.level].evasion[1])
    def updateStatistics(self):
        self.posture = (self.armor_type.posture[0] + self.enchance_type[self.level].posture[0] , self.armor_type.posture[1] + self.enchance_type[self.level].posture[1])
        self.constitution = (self.armor_type.constitution[0] + self.enchance_type[self.level].constitution[0] , self.armor_type.constitution[1] + self.enchance_type[self.level].constitution[1])
        self.evasion = (self.armor_type.evasion[0] + self.enchance_type[self.level].evasion[0] , self.armor_type.evasion[1] + self.enchance_type[self.level].evasion[1])
        pass
    def updateLevel(self, new_level : int):
        self.level = new_level
        self.updateStatistics()
        pass
class RaceClass():
    def __init__(self,name : str ,description : str ,image_path="" ,competences={}):
        self.name = name
        self.description = description
        self.image_path = image_path
        self.competences = competences
class ClasseClass():
    def __init__(self,name : str ,description : str ,image_path="",competences={},modifier=""):
        self.modifier = modifier
        self.name = name 
        self.description = description
        self.image_path = image_path
        self.competences = competences
class EntityClass(StatisticsClass):
    def __init__(self, name : str ,max_hp : int ,inventory={}):
        super().__init__(name)
        self.life = (max_hp,max_hp)
        self.inventory = inventory
        self.buffs = []
        pass
class PersonnalityClass(EntityClass):
    def __init__(self,name : str, max_hp : int ,level : int ,race ,classe ,basic_statistics ,constructor_weapon01 ,constructor_weapon02 ,constructor_weapon03 ,constructor_acces01 ,constructor_acces02 ,constructor_armor ,inventory={}):
        super().__init__(name,max_hp,inventory)
        self.state = ("normal",0,0)
        self.level = level
        self.race = race
        self.classe = classe
        self.basic_stat = basic_statistics
        self.weapon01 = WeaponClass(constructor_weapon01["name"],constructor_weapon01["description"],constructor_weapon01["level"],constructor_weapon01["type"],constructor_weapon01["enchance"],constructor_weapon01["enchance_name"])
        self.weapon02 = WeaponClass(constructor_weapon02["name"],constructor_weapon02["description"],constructor_weapon02["level"],constructor_weapon02["type"],constructor_weapon02["enchance"],constructor_weapon02["enchance_name"])
        self.weapon03 = WeaponClass(constructor_weapon03["name"],constructor_weapon03["description"],constructor_weapon03["level"],constructor_weapon03["type"],constructor_weapon03["enchance"],constructor_weapon03["enchance_name"])
        self.accessorry01 = AccessoryClass(constructor_acces01["name"],constructor_acces01["description"],constructor_acces01["level"],constructor_acces01["type"],constructor_acces01["enchance"],constructor_acces01["enchance_name"])
        self.accessorry02 = AccessoryClass(constructor_acces02["name"],constructor_acces02["description"],constructor_acces02["level"],constructor_acces02["type"],constructor_acces02["enchance"],constructor_acces02["enchance_name"])
        self.armor = ArmorClass(constructor_armor["name"],constructor_armor["description"],constructor_armor["level"],constructor_armor["type"],constructor_armor["enchance"],constructor_armor["enchance_name"])
        self.main_weapon = self.weapon01
        self.strength = (basic_statistics.strength[0] + self.accessorry01.strength[0] + self.accessorry02.strength[0] , basic_statistics.strength[1] + self.accessorry01.strength[1] + self.accessorry02.strength[1])
        self.dexterity = (basic_statistics.dexterity[0] + self.accessorry01.dexterity[0] + self.accessorry02.dexterity[0] , basic_statistics.dexterity[1] + self.accessorry01.dexterity[1] + self.accessorry02.dexterity[1])
        self.bleeding = (basic_statistics.bleeding[0] + self.accessorry01.bleeding[0] + self.accessorry02.bleeding[0] , basic_statistics.bleeding[1] + self.accessorry01.bleeding[1] + self.accessorry02.bleeding[1])
        self.posture = (basic_statistics.posture[0] + self.accessorry01.posture[0] + self.accessorry02.posture[0] , basic_statistics.posture[1] + self.accessorry01.posture[1] + self.accessorry02.posture[1])
        self.constitution = (basic_statistics.constitution[0] + self.accessorry01.constitution[0] + self.accessorry02.constitution[0] + self.armor.constitution[0] , basic_statistics.constitution[1] + self.accessorry01.constitution[1] + self.accessorry02.constitution[1] + + self.armor.constitution[1])
        self.evasion = (basic_statistics.evasion[0] + self.accessorry01.evasion[0] + self.accessorry02.evasion[0] + self.armor.evasion[0] , basic_statistics.evasion[1] + self.accessorry01.evasion[1] + self.accessorry02.evasion[1] + + self.armor.evasion[1])
        self.intellect = (basic_statistics.intellect[0] + self.accessorry01.intellect[0] + self.accessorry02.intellect[0] , basic_statistics.intellect[1] + self.accessorry01.intellect[1] + self.accessorry02.intellect[1])
        self.charisma = (basic_statistics.charisma[0] + self.accessorry01.charisma[0] + self.accessorry02.charisma[0] , basic_statistics.charisma[1] + self.accessorry01.charisma[1] + self.accessorry02.charisma[1])
        self.wisdom = (basic_statistics.wisdom[0] + self.accessorry01.wisdom[0] + self.accessorry02.wisdom[0] , basic_statistics.wisdom[1] + self.accessorry01.wisdom[1] + self.accessorry02.wisdom[1])
        self.competences = copy.deepcopy(self.race.competences) | copy.deepcopy(self.classe.competences) | copy.deepcopy(self.weapon01.weapon_type.competences) | copy.deepcopy(self.weapon02.weapon_type.competences) | copy.deepcopy(self.accessorry01.accessory_type.competences) | copy.deepcopy(self.accessorry02.accessory_type.competences)
        pass
    def refreshEquipement(self):
        self.strength = (self.basic_stat.strength[0] + self.accessorry01.strength[0] + self.accessorry02.strength[0] , self.basic_stat.strength[1] + self.accessorry01.strength[1] + self.accessorry02.strength[1])
        self.dexterity = (self.basic_stat.dexterity[0] + self.accessorry01.dexterity[0] + self.accessorry02.dexterity[0] , self.basic_stat.dexterity[1] + self.accessorry01.dexterity[1] + self.accessorry02.dexterity[1])
        self.bleeding = (self.basic_stat.bleeding[0] + self.accessorry01.bleeding[0] + self.accessorry02.bleeding[0] , self.basic_stat.bleeding[1] + self.accessorry01.bleeding[1] + self.accessorry02.bleeding[1])
        self.posture = (self.basic_stat.posture[0] + self.accessorry01.posture[0] + self.accessorry02.posture[0] , self.basic_stat.posture[1] + self.accessorry01.posture[1] + self.accessorry02.posture[1])
        self.constitution = (self.basic_stat.constitution[0] + self.accessorry01.constitution[0] + self.accessorry02.constitution[0] + self.armor.constitution[0] , self.basic_stat.constitution[1] + self.accessorry01.constitution[1] + self.accessorry02.constitution[1] + + self.armor.constitution[1])
        self.evasion = (self.basic_stat.evasion[0] + self.accessorry01.evasion[0] + self.accessorry02.evasion[0] + self.armor.evasion[0] , self.basic_stat.evasion[1] + self.accessorry01.evasion[1] + self.accessorry02.evasion[1] + + self.armor.evasion[1])
        self.intellect = (self.basic_stat.intellect[0] + self.accessorry01.intellect[0] + self.accessorry02.intellect[0] , self.basic_stat.intellect[1] + self.accessorry01.intellect[1] + self.accessorry02.intellect[1])
        self.charisma = (self.basic_stat.charisma[0] + self.accessorry01.charisma[0] + self.accessorry02.charisma[0] , self.basic_stat.charisma[1] + self.accessorry01.charisma[1] + self.accessorry02.charisma[1])
        self.wisdom = (self.basic_stat.wisdom[0] + self.accessorry01.wisdom[0] + self.accessorry02.wisdom[0] , self.basic_stat.wisdom[1] + self.accessorry01.wisdom[1] + self.accessorry02.wisdom[1])
        self.competences = copy.deepcopy(self.race.competences) | copy.deepcopy(self.classe.competences) | copy.deepcopy(self.weapon01.weapon_type.competences) | copy.deepcopy(self.weapon02.weapon_type.competences) | copy.deepcopy(self.accessorry01.accessory_type.competences) | copy.deepcopy(self.accessorry02.accessory_type.competences)
        pass
    def switchWeapon(self):
        if self.main_weapon == self.weapon01:
            self.main_weapon = self.weapon02
        if self.main_weapon == self.weapon02:
            self.main_weapon = self.weapon03
        elif self.main_weapon == self.weapon03:
            self.main_weapon = self.weapon01
        pass
    def refreshCompetences(self):
        self.competences = copy.deepcopy(self.race.competences) | copy.deepcopy(self.classe.competences) | copy.deepcopy(self.weapon01.weapon_type.competences) | copy.deepcopy(self.weapon02.weapon_type.competences) | copy.deepcopy(self.accessorry01.accessory_type.competences) | copy.deepcopy(self.accessorry02.accessory_type.competences)
        pass
class OrganisationClass(EntityClass):
    def __init__(self,name : str ,presentation : str ,max_hp : int ,capital : int ,basic_statistiques=StatisticsClass(""),image_path="https://media.discordapp.net/attachments/1002657461842497597/1005621372438986903/Inconnu.png?width=225&height=225"):
        super().__init__(name,max_hp,{})
        self.strength = basic_statistiques.strength
        self.dexterity = basic_statistiques.dexterity
        self.bleeding = basic_statistiques.bleeding
        self.posture = basic_statistiques.posture
        self.constitution = basic_statistiques.constitution
        self.evasion = basic_statistiques.evasion
        self.intellect = basic_statistiques.intellect
        self.charisma = basic_statistiques.charisma
        self.wisdom = basic_statistiques.wisdom
        self.presentation = presentation
        self.image_path = image_path
        self.capital = capital
        pass
class ArchetypeClass(PersonnalityClass):
    def __init__(self,name : str, presentation : str ,max_hp : int ,level : int ,race ,classe ,basic_statistics ,constructor_weapon01 ,constructor_weapon02 ,constructor_weapon03 ,constructor_acces01 ,constructor_acces02 ,constructor_armor ,image_path="https://media.discordapp.net/attachments/1002657461842497597/1005621372438986903/Inconnu.png?width=225&height=225",organisation=OrganisationClass("","",0,0)):
        super().__init__(name,max_hp,level,race,classe,basic_statistics,constructor_weapon01,constructor_weapon02,constructor_weapon03,constructor_acces01,constructor_acces02,constructor_armor,{})
        self.presentation = presentation
        self.image_path = image_path
        self.organisation = organisation  
        self.strength = (self.strength[0] + self.organisation.strength[0] , self.strength[1] + self.organisation.strength[1])
        self.dexterity = (self.dexterity[0] + self.organisation.dexterity[0] , self.dexterity[1] + self.organisation.dexterity[1])
        self.bleeding = (self.bleeding[0] + self.organisation.bleeding[0] , self.bleeding[1] + self.organisation.bleeding[1])
        self.posture = (self.posture[0] + self.organisation.posture[0] , self.posture[1] + self.organisation.posture[1])
        self.constitution = (self.constitution[0] + self.organisation.constitution[0] , self.constitution[1] + self.organisation.constitution[1])
        self.evasion = (self.evasion[0] + self.organisation.evasion[0] , self.evasion[1] + self.organisation.evasion[1])
        self.intellect = (self.intellect[0] + self.organisation.intellect[0] , self.intellect[1] + self.organisation.intellect[1])
        self.charisma = (self.charisma[0] + self.organisation.charisma[0] , self.charisma[1] + self.organisation.charisma[1])
        self.wisdom = (self.wisdom[0] + self.organisation.wisdom[0] , self.wisdom[1] + self.organisation.wisdom[1])
        self.presentation = presentation
    def refreshOrga(self):
        self.strength = (self.strength[0] + self.organisation.strength[0] , self.strength[1] + self.organisation.strength[1])
        self.dexterity = (self.dexterity[0] + self.organisation.dexterity[0] , self.dexterity[1] + self.organisation.dexterity[1])
        self.bleeding = (self.bleeding[0] + self.organisation.bleeding[0] , self.bleeding[1] + self.organisation.bleeding[1])
        self.posture = (self.posture[0] + self.organisation.posture[0] , self.posture[1] + self.organisation.posture[1])
        self.constitution = (self.constitution[0] + self.organisation.constitution[0] , self.constitution[1] + self.organisation.constitution[1])
        self.evasion = (self.evasion[0] + self.organisation.evasion[0] , self.evasion[1] + self.organisation.evasion[1])
        self.intellect = (self.intellect[0] + self.organisation.intellect[0] , self.intellect[1] + self.organisation.intellect[1])
        self.charisma = (self.charisma[0] + self.organisation.charisma[0] , self.charisma[1] + self.organisation.charisma[1])
        self.wisdom = (self.wisdom[0] + self.organisation.wisdom[0] , self.wisdom[1] + self.organisation.wisdom[1])
        pass
class CharacterClass(ArchetypeClass):
    def __init__(self,name : str, presentation : str ,history : str ,nickname : str , titles : list ,background : str ,alignement : str ,max_hp : int ,level : int ,race ,classe ,basic_statistics ,constructor_weapon01 ,constructor_weapon02 ,constructor_weapon03,constructor_acces01 ,constructor_acces02 ,constructor_armor , other_stats ,image_path : str , inventory={} , capital=0,languages=[],autority=OrganisationClass("","",0,0),organisation=OrganisationClass("","",0,0),craft_knowledge=[]):
        super().__init__(name,presentation,max_hp,level,race,classe,basic_statistics,constructor_weapon01,constructor_weapon02,constructor_weapon03,constructor_acces01,constructor_acces02,constructor_armor,{},organisation)
        self.other_stats = other_stats
        self.title_list = titles
        self.nickname = nickname
        self.constructor_weapon01 = constructor_weapon01
        self.constructor_weapon02 = constructor_weapon02
        self.constructor_weapon03 = constructor_weapon03
        self.constructor_acces01 = constructor_acces01
        self.constructor_acces02 = constructor_acces01
        self.constructor_armor = constructor_armor
        self.arcanes = other_stats["arcanes"]
        self.athletics = other_stats["athletics"]
        self.discretion = other_stats["discretion"]
        self.history = other_stats["history"]
        self.intimidation = other_stats["intimidation"]
        self.investigation = other_stats["investigation"]
        self.medicine = other_stats["medicine"]
        self.religion = other_stats["religion"]
        self.survive = other_stats["survive"]
        self.occultism = other_stats["occultism"]
        self.calm = other_stats["calm"]
        self.image_path = image_path
        self.languages = languages
        self.capital = capital
        self.autority = autority
        self.lore_history = history
        self.background = background
        self.alignement = alignement
        self.craft_knowledge = craft_knowledge
        pass
class LoreClass():
    def __init__(self,name : str ,presentation : str ,image_path="https://media.discordapp.net/attachments/1002657461842497597/1005621372438986903/Inconnu.png?width=225&height=225"):
        self.presentation = presentation
        self.image_path = image_path
        self.name = name
        pass
class FormationClass():
    def __init__(self,name : str ,description : str ,strength : int ,constitution : int ,defensive_strength : int ,morale_value=0):
        self.name = name
        self.description = description
        self.strength = strength
        self.constitution = constitution
        self.defensive_strength = defensive_strength
        self.morale_value = morale_value
        pass
class MassEntityClass():
    def __init__(self,name : str ,type_mass : str ,max_hp : int ,description : str ,image_path="https://media.discordapp.net/attachments/1002657461842497597/1005621372438986903/Inconnu.png?width=225&height=225",formations_dict={},inventory = {},organisation=OrganisationClass("","",0,0)):
        self.inventory = inventory
        self.moral_value = 100
        self.name = name
        self.life = (max_hp,max_hp)
        self.moral = 0
        self.description = description
        self.formation = formations_dict
        self.organisation = organisation
        self.rest_formation = FormationClass("rest_order","rest formation",0,10,5)
        self.camp_formation = FormationClass("camp_order","camp formation",0,25,15,10)
        self.walking_formation = FormationClass("walking_order","walking formation",0,20,20)
        self.state = self.rest_formation
        self.officer_hp = 300
        self.formation["rest_order"] = self.rest_formation
        self.formation["camp_order"] = self.camp_formation
        self.formation["walking_order"] = self.walking_formation
    def changeTheFormation(self,name : str):
        self.state = self.formation[name]
        pass
class SectionClass(MassEntityClass):
    def __init__(self,name : str ,type_mass : str ,level : int ,dexterity : int ,rigidity : int , max_hp : int ,description : str ,image_path="https://media.discordapp.net/attachments/1002657461842497597/1005621372438986903/Inconnu.png?width=225&height=225",formations_dict={},inventory = {},organisation=OrganisationClass("","",0,0)):
        super().__init__(name,type_mass,max_hp,description,image_path,formations_dict,inventory,organisation)
        self.level = level
        self.dexterity = dexterity
        self.rigidity = rigidity
class CastlleClass(EntityClass):
    def __init__(self,name : str , level : int ,max_hp : int ,content={},inventory={}):
        super().__init__(name,max_hp,inventory)
        self.name = name
        self.content = content
        self.level = level
class UserClass():
    def __init__(self,user_name : str ,content={}):
        self.user_name = user_name
        self.content = content
        self.pointage = ""
        self.sub_pointage = ""
        self.sub_sub_pointage = ""
        pass





    
