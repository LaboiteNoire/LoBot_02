"""
Skill Gestion Class File
"""
import TypographieFile as tf
import RpClassFile as rp
import StorageFile as st
import string
import random as rd
def getTheAbsoluteZero(value : int):
    if value < 0:
        return 0
    else:
        return value
def getUpdateStateOfCharacter(character):
    if (st.getTick() - character.state[2]) <= character.state[1]:
        return character.state[0]
    else:
        character.state = ("normal",character.state[1],character.state[2])
        return "normal"
def getIsInCooldown(skill):
    return ((st.getTick() - skill.last_utilisation) >= skill.competence_cooldown)
def canBeUse(character ,skill):
    return ((getIsInCooldown(skill) and (skill.level <= character.level)))
def getRestCooldown(skill):
    return getTheAbsoluteZero(skill.competence_cooldown - abs(st.getTick() - skill.last_utilisation))
def getRestCooldownState(character):
    return getTheAbsoluteZero(character.state[1] - abs(st.getTick() - character.state[2]))
def getUsableSkillList(character):
    new_list = []
    for skill_name in character.competences.keys():
        if (character.competences[skill_name].type[0] == "weapon_attack") and canBeUse(character,character.competences[skill_name]) and (skill_name in character.main_weapon.weapon_type.competences.keys()):
            new_list.append(skill_name)
        elif canBeUse(character,character.competences[skill_name]) and (character.competences[skill_name].type[0] != "weapon_attack"):
            new_list.append(skill_name)
        elif canBeUse(character,character.competences[skill_name]) and (character.competences[skill_name].type[0] == "one hand weapon_attack"):
            new_list.append(skill_name)
        elif canBeUse(character,character.competences[skill_name]) and (character.competences[skill_name].type[0] in ["ritual_skill","capacity"]):
            pass
    return new_list
def getUsableRitualList(character):
    new_list = []
    for skill_name in character.competences.keys():
        if canBeUse(character,character.competences[skill_name]) and (character.competences[skill_name].type[0] in ["ritual_skill"]):
            new_list.append(skill_name)
    return new_list
def rand(n : int):
    if n < 0:
        return rd.randint(n,0)
    else:
        return rd.randint(0,n)
def getBuffValue(buff_list : list ,buff_filter : str):
    new_value = (0,0)
    pop_list = []
    for k in range(len(buff_list)):
        buff = buff_list[k]
        if (st.getTick() - buff.last_utilisation) <= buff.cooldown:
            if buff_filter == "strength":
                new_value = (new_value[0] + buff.strength[0],new_value[1] + buff.strength[1])
            if buff_filter == "dexterity":
                new_value = (new_value[0] + buff.dexterity[0],new_value[1] + buff.dexterity[1])
            if buff_filter == "bleeding":
                new_value = (new_value[0] + buff.bleeding[0],new_value[1] + buff.bleeding[1])
            if buff_filter == "posture":
                new_value = (new_value[0] + buff.posture[0],new_value[1] + buff.posture[1])
            if buff_filter == "constitution":
                new_value = (new_value[0] + buff.constitution[0],new_value[1] + buff.constitution[1])
            if buff_filter == "evasion":
                new_value = (new_value[0] + buff.evasion[0],new_value[1] + buff.evasion[1])
            if buff_filter == "intellect":
                new_value = (new_value[0] + buff.intellect[0],new_value[1] + buff.intellect[1])
            if buff_filter == "charisma":
                new_value = (new_value[0] + buff.charisma[0],new_value[1] + buff.charisma[1])
            if buff_filter == "wisdom":
                new_value = (new_value[0] + buff.wisdom[0],new_value[1] + buff.wisdom[1])
        else:
            pop_list.append(k)
    for j in pop_list:
        buff_list.pop(j)
    return new_value



def updateBuffList(buff_list : list):
    new_buff_list = []
    for k in range(len(buff_list)):
        buff = buff_list[k]
        if (st.getTick() - buff.last_utilisation) <= buff.cooldown:
            new_buff_list.append(buff)
    return new_buff_list

            
def getAttackResult(competence,caster,target,competence_palier : int):
    strength_buffs = getBuffValue(caster.buffs,"strength")
    dexterity_buffs = getBuffValue(caster.buffs,"dexterity")
    bleeding_buffs = getBuffValue(caster.buffs,"bleeding")

    posture_buffs = getBuffValue(target.buffs,"posture")
    constitution_buffs = getBuffValue(target.buffs,"constitution")
    evasion_buffs = getBuffValue(target.buffs,"evasion")
    Buffs_dict = {"strength" : strength_buffs,"dexterity" : dexterity_buffs,"bleeding" : bleeding_buffs,
                  "posture" : posture_buffs,"constitution" : constitution_buffs,"evasion" : evasion_buffs}

    if competence.type[0] == "weapon_attack":
        strength_catser = rand(caster.main_weapon.strength[0] + competence.strength[0] + caster.accessorry01.strength[0] + caster.accessorry02.strength[0] + strength_buffs[0]) + competence.strength[1] + caster.main_weapon.strength[1] + caster.accessorry01.strength[1] + caster.accessorry02.strength[1] + strength_buffs[1]
        dexterity_catser = rand(caster.main_weapon.dexterity[0] + competence.dexterity[0] + caster.accessorry01.dexterity[0] + caster.accessorry02.dexterity[0] + dexterity_buffs[0]) + competence.dexterity[1] + caster.main_weapon.dexterity[1] + caster.accessorry01.dexterity[1] + caster.accessorry02.dexterity[1] + dexterity_buffs[1]
        bleeding_catser = rand(caster.main_weapon.bleeding[0] + competence.bleeding[0] + caster.accessorry01.bleeding[0] + caster.accessorry02.bleeding[0] + bleeding_buffs[0]) + competence.bleeding[1] + caster.main_weapon.bleeding[1] + caster.accessorry01.bleeding[0] + caster.accessorry02.bleeding[0] + bleeding_buffs[1]


        posture_target = rand(target.posture[0] + target.main_weapon.posture[0] + posture_buffs[0]) + target.posture[1] + target.main_weapon.posture[1] + posture_buffs[1]
        constitution_target = rand(target.constitution[0] + constitution_buffs[0]) + target.constitution[1] + constitution_buffs[1]
        evasion_target = rand(target.evasion[0] + evasion_buffs[0]) + target.evasion[1] + evasion_buffs[1]

        if caster.main_weapon.weapon_type.modifier == "strength":
            dexterity_catser = dexterity_catser + rd.randint(0,caster.strength[0]) + caster.strength[1]
        if caster.main_weapon.weapon_type.modifier == "dexterity":
            dexterity_catser = dexterity_catser + rd.randint(0,caster.dexterity[0]) + caster.dexterity[1]
        if caster.main_weapon.weapon_type.modifier == "bleeding":
            dexterity_catser = dexterity_catser + rd.randint(0,caster.bleeding[0]) + caster.bleeding[1]
        if caster.main_weapon.weapon_type.modifier == "posture":
            dexterity_catser = dexterity_catser + rd.randint(0,caster.posture[0]) + caster.posture[1]
        if caster.main_weapon.weapon_type.modifier == "constitution":
            dexterity_catser = dexterity_catser + rd.randint(0,caster.constitution[0]) + caster.constitution[1]
        if caster.main_weapon.weapon_type.modifier == "evasion":
            dexterity_catser = dexterity_catser + rd.randint(0,caster.evasion[0]) + caster.evasion[1]
        if caster.main_weapon.weapon_type.modifier == "intellect":
            dexterity_catser = dexterity_catser + rd.randint(0,caster.intellect[0]) + caster.intellect[1]
        if caster.main_weapon.weapon_type.modifier == "charisma":
            dexterity_catser = dexterity_catser + rd.randint(0,caster.charisma[0]) + caster.charisma[1]
        if caster.main_weapon.weapon_type.modifier == "wisdom":
            dexterity_catser = dexterity_catser + rd.randint(0,caster.wisdom[0]) + caster.wisdom[1]
        
        dice = rand(100)
        if getUpdateStateOfCharacter(target) == "block":
            return_result = (dice  <= competence_palier + dexterity_catser - evasion_target)
            if return_result:
                damage = getTheAbsoluteZero(getTheAbsoluteZero(constitution_target - strength_catser) + bleeding_catser - posture_target)
            else:
                damage = 0
        if getUpdateStateOfCharacter(target) == "iframe":
            return_result = False
            damage = 0
        else:
            return_result = (dice <= competence_palier + dexterity_catser - evasion_target)
            if return_result:
                damage = getTheAbsoluteZero(constitution_target - strength_catser) + bleeding_catser
            else:
                damage = 0
    else:
        strength_catser = rand(competence.strength[0]) + competence.strength[1] + rand(caster.strength[0]) + caster.strength[1] + rand(strength_buffs[0]) + strength_buffs[1]
        dexterity_catser = rand(competence.dexterity[0]) + competence.dexterity[1] + rand(caster.dexterity[0]) + caster.dexterity[1] + rand(dexterity_buffs[0]) + dexterity_buffs[1]
        bleeding_catser = rand(competence.bleeding[0]) + competence.bleeding[1] + rand(caster.bleeding[0]) + caster.bleeding[1] + rand(bleeding_buffs[0]) + bleeding_buffs[1]


        posture_target = rand(target.posture[0] + rand(posture_buffs[0])) + target.posture[1] + posture_buffs[1]

        constitution_target = rand(target.constitution[0] + rand(constitution_buffs[0])) + target.constitution[1] + constitution_buffs[1]
        evasion_target = rand(target.evasion[0] + rand(evasion_buffs[0])) + target.evasion[1] + evasion_buffs[1]
        dice = rand(100)
        return_result = (dice <= competence_palier + dexterity_catser - evasion_target)
        if caster.classe.modifier == "strength":
            strength_catser = strength_catser + rd.randint(0,caster.strength[0]) + caster.strength[1]
        if caster.classe.modifier == "dexterity":
            strength_catser = strength_catser + rd.randint(0,caster.dexterity[0]) + caster.dexterity[1]
        if caster.classe.modifier == "bleeding":
            strength_catser = strength_catser + rd.randint(0,caster.bleeding[0]) + caster.bleeding[1]
        if caster.classe.modifier == "posture":
            strength_catser = strength_catser + rd.randint(0,caster.posture[0]) + caster.posture[1]
        if caster.classe.modifier == "constitution":
            strength_catser = strength_catser + rd.randint(0,caster.constitution[0]) + caster.constitution[1]
        if caster.classe.modifier == "evasion":
            strength_catser = strength_catser + rd.randint(0,caster.evasion[0]) + caster.evasion[1]
        if caster.classe.modifier == "intellect":
            strength_catser = strength_catser + rd.randint(0,caster.intellect[0]) + caster.intellect[1]
        if caster.classe.modifier == "charisma":
            strength_catser = strength_catser + rd.randint(0,caster.charisma[0]) + caster.charisma[1]
        if caster.classe.modifier == "wisdom":
            strength_catser = strength_catser + rd.randint(0,caster.wisdom[0]) + caster.wisdom[1]
        if getUpdateStateOfCharacter(target) == "block":
            return_result = (dice + dexterity_catser - evasion_target <= competence_palier)
            if return_result:
                damage = getTheAbsoluteZero(getTheAbsoluteZero(constitution_target - strength_catser) + bleeding_catser - posture_target)
            else:
                damage = 0
        if getUpdateStateOfCharacter(target) == "iframe":
            return_result = False
            damage = 0
        else:
            return_result = (dice + dexterity_catser - evasion_target <= competence_palier)
            if return_result:
                damage = getTheAbsoluteZero(constitution_target - strength_catser) + bleeding_catser
            else:
                damage = 0
    return (return_result,damage,strength_catser,dexterity_catser,bleeding_catser,posture_target,constitution_target,evasion_target,dice,(competence_palier + dexterity_catser - evasion_target),Buffs_dict)
def getCharacteristicDiceResult(caster,competence_palier : int , dice_type : str):
    strength_buffs = getBuffValue(caster.buffs,"strength")
    dexterity_buffs = getBuffValue(caster.buffs,"dexterity")
    bleeding_buffs = getBuffValue(caster.buffs,"bleeding")
    posture_buffs = getBuffValue(caster.buffs,"posture")
    constitution_buffs = getBuffValue(caster.buffs,"constitution")
    evasion_buffs = getBuffValue(caster.buffs,"evasion")
    intellect_buffs = getBuffValue(caster.buffs,"intellect")
    charisma_buffs = getBuffValue(caster.buffs,"charisma")
    wisdom_buffs = getBuffValue(caster.buffs,"wisdom")


    dice = rand(100)
    strength_catser = rand(caster.strength[0]) + caster.strength[1] + rand(strength_buffs[0]) + strength_buffs[1]
    dexterity_catser = rand(caster.dexterity[0]) + caster.dexterity[1] + rand(dexterity_buffs[0]) + dexterity_buffs[1]
    bleeding_catser = rand(caster.bleeding[0]) + caster.bleeding[1] + rand(bleeding_buffs[0]) + bleeding_buffs[1]
    posture_catser = rand(caster.posture[0]) + caster.posture[1] + rand(posture_buffs[0]) + posture_buffs[1]
    constitution_catser = rand(caster.constitution[0]) + caster.constitution[1] + rand(constitution_buffs[0]) + constitution_buffs[1]
    evasion_catser = rand(caster.evasion[0]) + caster.evasion[1] + rand(evasion_buffs[0]) + evasion_buffs[1]
    intellect_catser = rand(caster.intellect[0]) + caster.intellect[1] + rand(intellect_buffs[0]) + intellect_buffs[1]
    charisma_catser = rand(caster.charisma[0]) + caster.charisma[1] + rand(charisma_buffs[0]) + charisma_buffs[1]
    wisdom_catser = rand(caster.wisdom[0]) + caster.wisdom[1] + rand(wisdom_buffs[0]) + wisdom_buffs[1]
    if dice_type == "arcanes":
        result = (getTheAbsoluteZero(dice - intellect_catser - caster.arcanes) <= competence_palier)
        return (result , getTheAbsoluteZero(dice - intellect_catser - caster.arcanes))
    if dice_type == "athletics":
        result = (getTheAbsoluteZero(dice - strength_catser - caster.athletics) <= competence_palier)
        return (result , getTheAbsoluteZero(dice - strength_catser - caster.athletics))
    if dice_type == "discretion":
        result = (getTheAbsoluteZero(dice - dexterity_catser - caster.discretion) <= competence_palier)
        return (result , getTheAbsoluteZero(dice - dexterity_catser - caster.discretion))
    if dice_type == "history":
        result = (getTheAbsoluteZero(dice - intellect_catser - caster.history) <= competence_palier)
        return (result , getTheAbsoluteZero(dice - intellect_catser - caster.history))
    if dice_type == "intimidation":
        result = (getTheAbsoluteZero(dice - charisma_catser - caster.intimidation) <= competence_palier)
        return (result , getTheAbsoluteZero(dice - charisma_catser - caster.intimidation))
    if dice_type == "investigation":
        result = (getTheAbsoluteZero(dice - dexterity_catser - caster.investigation) <= competence_palier)
        return (result , getTheAbsoluteZero(dice - dexterity_catser - caster.investigation))
    if dice_type == "medicine":
        result = (getTheAbsoluteZero(dice - intellect_catser - caster.medicine) <= competence_palier)
        return (result , getTheAbsoluteZero(dice - intellect_catser - caster.medicine))
    if dice_type == "religion":
        result = (getTheAbsoluteZero(dice - wisdom_catser - caster.religion) <= competence_palier)
        return (result , getTheAbsoluteZero(dice - wisdom_catser - caster.religion))
    if dice_type == "survive":
        result = (getTheAbsoluteZero(dice - wisdom_catser - caster.survive) <= competence_palier)
        return (result , getTheAbsoluteZero(dice - wisdom_catser - caster.survive))
    if dice_type == "occultism":
        result = (getTheAbsoluteZero(dice - intellect_catser - caster.occultism) <= competence_palier)
        return (result , getTheAbsoluteZero(dice - intellect_catser - caster.occultism))
    if dice_type == "calm":
        result = (getTheAbsoluteZero(dice - charisma_catser - caster.calm) <= competence_palier)
        return (result , getTheAbsoluteZero(dice - charisma_catser - caster.calm))







def getRandomName(long=100000):
    if long==100000:
        long = rd.randint(4,18)
    procedural_list = ["lexegezacebisone",
                       "usesarmaindireav",
                       "eratenberalaveti",
                       "edorquanteisrion"]
    txt = ""
    if (long % 2) == 0:
        for i in range(long//2):
            nul = rd.randint(0,14)
            txt = txt + procedural_list[rd.randint(0,3)][nul] + procedural_list[rd.randint(0,3)][nul+1]
    else:
        for i in range(long//2):
            nul = rd.randint(0,14)
            txt = txt + procedural_list[rd.randint(0,3)][nul] + procedural_list[rd.randint(0,3)][nul+1]
        txt = txt + rd.choice(string.ascii_letters)
    return txt












def getMassEntityAttackResult(caster , target ,palier : int):
    dice = rand(100)
    caster_morale_rate = caster.moral
    target_morale_rate = target.moral
    if isinstance(caster,rp.SectionClass):
        caster_dexterity = caster.dexterity
    else:
        caster_dexterity = 0
    if isinstance(target,rp.SectionClass):
        target_dexterity = target.dexterity
    else:
        target_dexterity = 0


    if dice <= (palier + cacaster_dexterity - target_dexterity):
        result = True
        target_damages = getTheAbsoluteZero(int(caster_morale_rate*caster.state.strength + rand(getTheAbsoluteZero((1-caster_morale_rate)*caster.state.strength))) + caster.rigidity - target.rigidity - int(target_morale_rate*target.state.constitution + rand(getTheAbsoluteZero((1-target_morale_rate)*target.state.constitution))))
        caster_damages = getTheAbsoluteZero(int(target_morale_rate*target.state.defensive_strength + rand(getTheAbsoluteZero((1-target_morale_rate)*target.state.defensive_strength)) - int(caster_morale_rate*caster.state.constitution + rand(getTheAbsoluteZero((1-caster_morale_rate)*caster.state.constitution)) -caster.rigidity + target.rigidity)))
    else:
        result = False
    
    pass
