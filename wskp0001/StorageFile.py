"""
Storage Class File
"""
import RpClassFile as rp
import os
import io
import pickle
import csv
def tickUpdate(path="database\Wdatatick.txt"):
    if os.path.exists(path):
        openFile = open(path,"r")
        tickValue = int(openFile.readlines()[0]) + 1
        openFile.close()

        fileSave = open(path,"w")
        fileSave.write(str(tickValue))
        fileSave.close()
    else:
        pass
def tickReset(path="database\Wdatatick.txt"):
    if os.path.exists(path):
        fileSave = open(path,"w")
        fileSave.write("0")
        fileSave.close()
    else:
        pass
def getTick(path="database\Wdatatick.txt"):
    if os.path.exists(path):
        openFile = open(path,"r")
        tickValue = int(openFile.readlines()[0])
        openFile.close()
        return tickValue
def saveDict(Dictionnaire : dict ,path : str):
    fileIn = open(path,"wb")
    pickle.dump(Dictionnaire,fileIn)
    fileIn.close()
def loadDict(path : str):
    fileout = open(path,"rb")
    Load = pickle.load(fileout) 
    fileout.close()
    return Load
def deleteData(Dictionnaire : dict , data_name : str):
    del Dictionnaire[data_name]
def researchData(data_name : str ,data_path : str):
    return data_name in loadDict(data_path)



def getIndice(my_list : list , value):
    for i in range(len(my_list)):
        if value == my_list[i]:
            return i







def filterCompetences(skill_type=""):
    new_list = []
    skill_dict = loadDict("database\CompetencesDatabase.obj")
    if type(skill_type) == str:
        if skill_type == "":
            new_list = skill_dict.keys()
        else:
            for key in skill_dict.keys():
                if skill_dict[key].type[0] == skill_type:
                    new_list.append(key)
    elif type(skill_type) == list:
        if skill_type == []:
            new_list = skill_dict.keys()
        else:
            for key in skill_dict.keys():
                if skill_dict[key].type[0] in skill_type:
                    new_list.append(key)
    return new_list
def antiFilterCompetences(skill_type=""):
    new_list = []
    skill_dict = loadDict("database\CompetencesDatabase.obj")
    if type(skill_type) == str:
        if skill_type != "":
            new_list = skill_dict.keys()
        else:
            for key in skill_dict.keys():
                if skill_dict[key].type[0] == skill_type:
                    new_list.append(key)
    elif type(skill_type) == list:
        if skill_type == []:
            new_list = skill_dict.keys()
        else:
            for key in skill_dict.keys():
                if skill_dict[key].type[0] not in skill_type:
                    new_list.append(key)
    return new_list
def filterEquipementType(equipement=""):
    new_list = []
    equipement_dict = loadDict("database\EquipementsDatabase.obj")
    if equipement == "":
        new_list = equipement_dict.keys()
    if equipement == "weapon_type":
        for key in equipement_dict.keys():
            if isinstance(equipement_dict[key],rp.WeaponTypeClass):
                new_list.append(key)
    if equipement == "accessory_type":
        for key in equipement_dict.keys():
            if isinstance(equipement_dict[key],rp.AccessoryClassTypeClass):
                new_list.append(key)
    elif equipement == "armor_type":
        for key in equipement_dict.keys():
            if isinstance(equipement_dict[key],rp.ArmorClassTypeClass):
                new_list.append(key)
    return new_list




def getCharactersList():
    user_data = loadDict(r"database\users_database.obj")
    character_names_list = []
    for user in user_data.keys():
        for family_name in user_data[user].content.keys():
            for character_name in user_data[user].content[family_name].keys():
                character_names_list.append(character_name)
    return character_names_list
def getCharactersDict():
    user_data = loadDict(r"database\users_database.obj")
    user_dict = {}
    for user in user_data.keys():
        family_dict = {}
        for family_name in user_data[user].content.keys():
            character_list = []
            for character_name in user_data[user].content[family_name].keys():
                character_list.append(character_name)
            family_dict[family_name] = character_list
        user_dict[user_data[user].user_name] = family_dict
    return user_dict



def getCharactersPaths(Caracter_name : str):
    user_data = loadDict(r"database\users_database.obj")
    character_path_list = []
    for user_name in user_data.keys():
        for display_name in user_data[user_name].content.keys():
            for character_name in user_data[user_name].content[display_name].keys():
                if character_name == Caracter_name:
                    character_path_list.append(user_name + "|" + display_name + "|" + character_name)
    return character_path_list
            




def cvsEnchanceInterpretor(csv_file_path : str):
    lecteur = csv.DictReader(open(csv_file_path,"r"))
    new_list = []
    for ligne in lecteur:
        new_ligne = {}
        for name in ligne.keys():
            if name != "level":
                treatement = ligne[name][1:(len(ligne[name])-1)].split(",")
                new_ligne[name] = (int(treatement[0]),int(treatement[1]))
        new_list.append(new_ligne)
    return new_list




def loadOrganisation(organisation_name : str):
    return (loadDict("database\OrganisationsDatabase.obj"))[organisation_name]
def saveOrganisation(new_organisation):
    load_dict = loadDict("database\OrganisationsDatabase.obj")
    load_dict[new_organisation.name] = new_organisation
    saveDict(load_dict, "database\OrganisationsDatabase.obj")
def loadClasse(classe_name : str):
    return (loadDict("database\ClassDatabase.obj"))[classe_name]
def saveClasse(new_class):
    load_dict = loadDict("database\ClassDatabase.obj")
    load_dict[new_class.name] = new_class
    saveDict(load_dict, "database\ClassDatabase.obj")
def loadRace(race_name : str):
    return (loadDict("database\RacesDatabase.obj"))[race_name]
def saveRace(new_race):
    load_dict = loadDict("database\RacesDatabase.obj")
    load_dict[new_race.name] = new_race
    saveDict(load_dict, "database\RacesDatabase.obj")
def loadLore(lore_name : str):
    return (loadDict("database\LoresDatabase.obj"))[lore_name]
def saveLore(new_lore):
    load_dict = loadDict("database\LoresDatabase.obj")
    load_dict[new_lore.name] = new_lore
    saveDict(load_dict, "database\LoresDatabase.obj")
def loadCompetence(competence_name : str):
    return (loadDict("database\CompetencesDatabase.obj"))[competence_name]
def saveCompetence(new_competence):
    load_dict = loadDict("database\CompetencesDatabase.obj")
    load_dict[new_competence.name] = new_competence
    saveDict(load_dict, "database\CompetencesDatabase.obj")
def loadCompetence(competence_name : str):
    return (loadDict("database\CompetencesDatabase.obj"))[competence_name]
def saveCompetence(new_competence):
    load_dict = loadDict("database\CompetencesDatabase.obj")
    load_dict[new_competence.name] = new_competence
    saveDict(load_dict, "database\CompetencesDatabase.obj")
def loadEnchance(competence_name : str):
    return (loadDict("database\EnchancesDatabase.obj"))[competence_name]
def saveEnchance(new_enchance : list,new_enchance_name : str):
    load_dict = loadDict("database\EnchancesDatabase.obj")
    load_dict[new_enchance_name] = new_enchance
    saveDict(load_dict, "database\EnchancesDatabase.obj")
def loadEquipement(equipement_name : str):
    return (loadDict("database\EquipementsDatabase.obj"))[equipement_name]
def saveEquipement(new_equipement : list,new_equipement_name : str):
    load_dict = loadDict("database\EquipementsDatabase.obj")
    load_dict[new_equipement_name] = new_equipement
    saveDict(load_dict, "database\EquipementsDatabase.obj")
def loadCharacter(user_name : str ,display_name : str ,character_name : str):
    return ((loadDict(r"database\users_database.obj"))[user_name].content[display_name][character_name])
def saveCharacter(new_character ,user_name : str ,display_name : str):
    if researchData(user_name,r"database\users_database.obj"):
        user = loadDict(r"database\users_database.obj")[user_name]
        user.content[display_name][new_character.name] = new_character
    else:
        constructor = {display_name : {new_character.name : new_character}}
        user = rp.UserClass(user_name,constructor)
    user.pointage = display_name
    user.sub_pointage = new_character.name
    user.sub_sub_pointage = ""
    load_dict = loadDict(r"database\users_database.obj")
    load_dict[user_name] = user
    saveDict(load_dict, r"database\users_database.obj")
def loadUser(user_name : str):
    return ((loadDict(r"database\users_database.obj"))[user_name])
def saveUser(new_user):
    load_dict = loadDict(r"database\users_database.obj")
    load_dict[new_user.user_name] = new_user
    saveDict(load_dict, r"database\users_database.obj")
def loadItem(organisation_name : str):
    return (loadDict("database\ItemsDatabase.obj"))[organisation_name]
def saveItem(new_item):
    load_dict = loadDict("database\ItemsDatabase.obj")
    load_dict[new_item.name] = new_item
    saveDict(load_dict, "database\ItemsDatabase.obj")
def loadArchetype(archetype_name : str):
    return (loadDict(r"database\archetypes_database.obj"))[archetype_name]
def saveArchetype(new_archetype):
    load_dict = loadDict(r"database\archetypes_database.obj")
    load_dict[new_archetype.name] = new_archetype
    saveDict(load_dict, r"database\archetypes_database.obj")




def updateTheArchetypes():
    load_dict = loadDict(r"database\archetypes_database.obj")
    for character_name in load_dict.keys():
        char_name = character_name
        display_character = load_dict[character_name]
        char_description = display_character.presentation
        char_history = display_character.lore_history
        char_nickname = display_character.nickname
        char_titles = display_character.title_list
        char_background = display_character.background
        char_allignement = display_character.alignement
        char_max_hp = display_character.life[1]
        char_level = display_character.level
        if display_character.race.name != "":
            char_race = loadRace(display_character.race.name)
        else:
            char_race = display_character.race
        if display_character.classe.name != "":
            char_classe = loadClasse(display_character.classe.name)
        else:
            char_classe = display_character.classe
        char_basic_stats = display_character.basic_stat
        char_constructor_weapon01 = display_character.constructor_weapon01
        char_constructor_weapon02 = display_character.constructor_weapon02
        char_constructor_weapon03 = display_character.constructor_weapon03
        char_constructor_acces01 = display_character.constructor_acces01
        char_constructor_acces02 = display_character.constructor_acces02
        char_constructor_armor = display_character.constructor_armor
        char_other_stats = display_character.other_stats
        char_image_path = display_character.image_path
        char_inventory = display_character.inventory
        char_capital = display_character.capital
        char_languages = display_character.languages
        char_autority = display_character.autority
        char_organisation = display_character.organisation
        char_inventory = {}
        char_knowledge = display_character.craft_knowledge
        for name in display_character.inventory.keys():
            char_inventory[name] = st.loadItem(name)
            char_inventory[name].quantity = display_character.inventory[name].quantity
        fresh_character = rp.CharacterClass(char_name,char_description,char_history,char_nickname,char_titles,char_background,char_allignement,char_max_hp,char_level,char_race,char_classe,char_basic_stats,char_constructor_weapon01,char_constructor_weapon02,char_constructor_weapon03,char_constructor_acces01,char_constructor_acces02, char_constructor_armor,char_other_stats,char_image_path,char_inventory,char_capital,char_languages,char_autority,char_organisation,char_knowledge)
        load_dict[char_name] = fresh_character
    saveDict(load_dict, r"database\archetypes_database.obj")




