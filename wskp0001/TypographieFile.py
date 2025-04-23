"""
Typographie File
"""
import discord
from discord.ext import commands
import random
from discord.ext import commands
from discord_slash import ButtonStyle , SlashCommand
from discord_slash.utils.manage_components import *
import matplotlib.pyplot as plt
import RpClassFile as rp
import SkillsTreatmentFile as sktr
nonetxt = "᲼"


def getListSelection(ctx , name : str ,selectionList : list ,subSelectionList : list ,mi_val=1,ma_val=1):
    if len(selectionList) == len(subSelectionList):
        options=[]
        for i in range(len(selectionList)):
            options.append(create_select_option(selectionList[i], value=subSelectionList[i]))
        my_selection = create_select(
            options,
            placeholder=name,
            min_values=mi_val,
            max_values=ma_val
        )
    else:
        my_selection = create_select(
            options=[create_select_option(nonetxt, value=nonetxt)],
            placeholder=nonetxt,
            min_values=mi_val,
            max_values=ma_val
        )
    return my_selection
def getEmbedImageCompetence(ctx ,name : str , link="https://cdn.discordapp.com/attachments/1002657461842497597/1013535251777196163/Vierges_du_Sang_Symbole.png"):
    embed = discord.Embed(
        title="__Statistiques__" ,
        description = "*Name of the skill:*" + " **" + name + "**" ,
        color = discord.Colour.purple()
        )
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url=link)
    embed.set_image(url=link)
    return embed
def TypographyCompetenceInterface(ctx,competence,my_embed):
    my_embed.add_field(name="`*state of the skill*` : `" + competence.state[0] + "`", value="`" + str(competence.state[1]) + " *ticks*`", inline=False)
    my_embed.add_field(name="`*cooldown of the skill*` :", value="`" + str(competence.competence_cooldown) + " *ticks*`", inline=False)
    my_embed.add_field(name="`*type of the skill*` :", value="`" + str(competence.type) + "`", inline=False)
    if competence.type[0] == "normal_attack":
        my_embed.add_field(name="`*attack statistics*`", value=nonetxt, inline=False)
        my_embed.add_field(name=":medical_symbol: __*Strength__" + "`" + str(competence.strength) + "`", value=nonetxt, inline=True)
        my_embed.add_field(name=":medical_symbol: __*Dexterity__" + "`" + str(competence.dexterity) + "`", value=nonetxt, inline=True)
        my_embed.add_field(name=":medical_symbol: __*Bleeding__" + "`" + str(competence.bleeding) + "`", value=nonetxt, inline=True)
        my_embed.add_field(name=":medical_symbol: __*Posture__" + "`" + str(competence.posture) + "`", value=nonetxt, inline=True)
        my_embed.add_field(name=":medical_symbol: __*Constitution__" + "`" + str(competence.constitution) + "`", value=nonetxt, inline=True)
        my_embed.add_field(name=":medical_symbol: __*Intellect__" + "`" + str(competence.intellect) + "`", value=nonetxt, inline=True)
        my_embed.add_field(name=":medical_symbol: __*Charisma__" + "`" + str(competence.charisma) + "`", value=nonetxt, inline=True)
        my_embed.add_field(name=":medical_symbol: __*Wisdom__" + "`" + str(competence.wisdom) + "`", value=nonetxt, inline=True)
    if competence.type[0] == "weapon_attack" or competence.type[0] == "one hand weapon_attack" or competence.type[0] == "transversal_attack":
        my_embed.add_field(name="`*attack additionnal statistics for the weapon*`", value=nonetxt, inline=False)
        my_embed.add_field(name=":medical_symbol: __*Strength__" + "`" + str(competence.strength) + "`", value=nonetxt, inline=True)
        my_embed.add_field(name=":medical_symbol: __*Dexterity__" + "`" + str(competence.dexterity) + "`", value=nonetxt, inline=True)
        my_embed.add_field(name=":medical_symbol: __*Bleeding__" + "`" + str(competence.bleeding) + "`", value=nonetxt, inline=True)
        my_embed.add_field(name=":medical_symbol: __*Posture__" + "`" + str(competence.posture) + "`", value=nonetxt, inline=True)
        my_embed.add_field(name=":medical_symbol: __*Constitution__" + "`" + str(competence.constitution) + "`", value=nonetxt, inline=True)
        my_embed.add_field(name=":medical_symbol: __*Intellect__" + "`" + str(competence.intellect) + "`", value=nonetxt, inline=True)
        my_embed.add_field(name=":medical_symbol: __*Charisma__" + "`" + str(competence.charisma) + "`", value=nonetxt, inline=True)
        my_embed.add_field(name=":medical_symbol: __*Wisdom__" + "`" + str(competence.wisdom) + "`", value=nonetxt, inline=True)
    if (competence.type[0] == "mouvement_skill") or (competence.type[0] == "util_skill") or (competence.type[0] == "transformation"):
        pass
    if (competence.type[0] == "massive_skill") or (competence.type[0] == "rituel_skill"):
        if competence.level <= 14:
            my_embed.add_field(name="`*for 6 tagets*`", value="__for : __" + "`" +  str(competence.state[1]) + " ticks`", inline=False)
        else:
            my_embed.add_field(name="`*for only 3 tagets*`", value="__for : __" + "`" +  str(competence.state[1]) + " ticks`", inline=False)
        pass
    if (competence.type[1] == "self_buff"):
        my_embed.add_field(name="`*self buff statistics*`", value="__for : __" + "`" +  str(competence.state[1]) + " ticks`", inline=False)
        my_embed.add_field(name=":medical_symbol: __*Strength__" + "`" + str(competence.self_buff.strength) + "`", value=nonetxt, inline=True)
        my_embed.add_field(name=":medical_symbol: __*Dexterity__" + "`" + str(competence.self_buff.dexterity) + "`", value=nonetxt, inline=True)
        my_embed.add_field(name=":medical_symbol: __*Bleeding__" + "`" + str(competence.self_buff.bleeding) + "`", value=nonetxt, inline=True)
        my_embed.add_field(name=":medical_symbol: __*Posture__" + "`" + str(competence.self_buff.posture) + "`", value=nonetxt, inline=True)
        my_embed.add_field(name=":medical_symbol: __*Constitution__" + "`" + str(competence.self_buff.constitution) + "`", value=nonetxt, inline=True)
        my_embed.add_field(name=":medical_symbol: __*Evasion__" + "`" + str(competence.self_buff.evasion) + "`", value=nonetxt, inline=True)
        my_embed.add_field(name=":medical_symbol: __*Intellect__" + "`" + str(competence.self_buff.intellect) + "`", value=nonetxt, inline=True)
        my_embed.add_field(name=":medical_symbol: __*Charisma__" + "`" + str(competence.self_buff.charisma) + "`", value=nonetxt, inline=True)
        my_embed.add_field(name=":medical_symbol: __*Wisdom__" + "`" + str(competence.self_buff.wisdom) + "`", value=nonetxt, inline=True)
        pass
    if (competence.type[1] == "buff"):
        my_embed.add_field(name="`*buff statistics for target touch*`", value="__for : __" + "`" +  str(competence.state[1]) + " ticks`", inline=False)
        my_embed.add_field(name=":medical_symbol: __*Strength__" + "`" + str(competence.buff.strength) + "`", value=nonetxt, inline=True)
        my_embed.add_field(name=":medical_symbol: __*Dexterity__" + "`" + str(competence.buff.dexterity) + "`", value=nonetxt, inline=True)
        my_embed.add_field(name=":medical_symbol: __*Bleeding__" + "`" + str(competence.buff.bleeding) + "`", value=nonetxt, inline=True)
        my_embed.add_field(name=":medical_symbol: __*Posture__" + "`" + str(competence.buff.posture) + "`", value=nonetxt, inline=True)
        my_embed.add_field(name=":medical_symbol: __*Constitution__" + "`" + str(competence.buff.constitution) + "`", value=nonetxt, inline=True)
        my_embed.add_field(name=":medical_symbol: __*Evasion__" + "`" + str(competence.buff.evasion) + "`", value=nonetxt, inline=True)
        my_embed.add_field(name=":medical_symbol: __*Intellect__" + "`" + str(competence.buff.intellect) + "`", value=nonetxt, inline=True)
        my_embed.add_field(name=":medical_symbol: __*Charisma__" + "`" + str(competence.buff.charisma) + "`", value=nonetxt, inline=True)
        my_embed.add_field(name=":medical_symbol: __*Wisdom__" + "`" + str(competence.buff.wisdom) + "`", value=nonetxt, inline=True)
        pass
    my_embed.add_field(name="__Skill Description__", value="`" +  competence.presentation + "`", inline=False)
    my_embed.set_footer(text="mise a jour par: {}".format(ctx.author.display_name))
    pass
def getEmbedImageEnchance(ctx,argu :str ,enchance : list):
    embed = discord.Embed(
        title="__Statistiques__" ,
        description = "*evolution of the enchance for the " + argu + "* " ,
        color = discord.Colour.purple()
        )
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    if argu == "strength":
        plt.clf()
        plt.figure(facecolor="gray")
        plt.axes().set_facecolor("black")
        plt.plot([0,1,2,3,4,5,6,7,8,9],[x.strength[0] for x in enchance])
        plt.plot([0,1,2,3,4,5,6,7,8,9],[x.strength[1] for x in enchance])
        plt.savefig("rsc/courb_drawing/strength_drawing.png")
        file = discord.File("rsc/courb_drawing/strength_drawing.png", filename="strength_drawing.png")
        embed.set_image(url="attachment://strength_drawing.png")
    if argu == "dexterity":
        plt.clf()
        plt.figure(facecolor="gray")
        plt.axes().set_facecolor("black")
        plt.plot([0,1,2,3,4,5,6,7,8,9],[x.dexterity[0] for x in enchance])
        plt.plot([0,1,2,3,4,5,6,7,8,9],[x.dexterity[1] for x in enchance])
        plt.savefig("rsc/courb_drawing/dexterity_drawing.png")
        file = discord.File("rsc/courb_drawing/dexterity_drawing.png", filename="dexterity_drawing.png")
        embed.set_image(url="attachment://dexterity_drawing.png")
    if argu == "bleeding":
        plt.clf()
        plt.figure(facecolor="gray")
        plt.axes().set_facecolor("black")
        plt.plot([0,1,2,3,4,5,6,7,8,9],[x.bleeding[0] for x in enchance])
        plt.plot([0,1,2,3,4,5,6,7,8,9],[x.bleeding[1] for x in enchance])
        plt.savefig("rsc/courb_drawing/bleeding_drawing.png")
        file = discord.File("rsc/courb_drawing/bleeding_drawing.png", filename="bleeding_drawing.png")
        embed.set_image(url="attachment://bleeding_drawing.png")
    if argu == "posture":
        plt.clf()
        plt.figure(facecolor="gray")
        plt.axes().set_facecolor("black")
        plt.plot([0,1,2,3,4,5,6,7,8,9],[x.posture[0] for x in enchance])
        plt.plot([0,1,2,3,4,5,6,7,8,9],[x.posture[1] for x in enchance])
        plt.savefig("rsc/courb_drawing/posture_drawing.png")
        file = discord.File("rsc/courb_drawing/posture_drawing.png", filename="posture_drawing.png")
        embed.set_image(url="attachment://posture_drawing.png")
    if argu == "constitution":
        plt.clf()
        plt.figure(facecolor="gray")
        plt.axes().set_facecolor("black")
        plt.plot([0,1,2,3,4,5,6,7,8,9],[x.constitution[0] for x in enchance])
        plt.plot([0,1,2,3,4,5,6,7,8,9],[x.constitution[1] for x in enchance])
        plt.savefig("rsc/courb_drawing/constitution_drawing.png")
        file = discord.File("rsc/courb_drawing/constitution_drawing.png", filename="constitution_drawing.png")
        embed.set_image(url="attachment://constitution_drawing.png")
    if argu == "evasion":
        plt.clf()
        plt.figure(facecolor="gray")
        plt.axes().set_facecolor("black")
        plt.plot([0,1,2,3,4,5,6,7,8,9],[x.evasion[0] for x in enchance])
        plt.plot([0,1,2,3,4,5,6,7,8,9],[x.evasion[1] for x in enchance])
        plt.savefig("rsc/courb_drawing/evasion_drawing.png")
        file = discord.File("rsc/courb_drawing/evasion_drawing.png", filename="evasion_drawing.png")
        embed.set_image(url="attachment://evasion_drawing.png")
    if argu == "intellect":
        plt.clf()
        plt.figure(facecolor="gray")
        plt.axes().set_facecolor("black")
        plt.plot([0,1,2,3,4,5,6,7,8,9],[x.intellect[0] for x in enchance])
        plt.plot([0,1,2,3,4,5,6,7,8,9],[x.intellect[1] for x in enchance])
        plt.savefig("rsc/courb_drawing/intellect_drawing.png")
        file = discord.File("rsc/courb_drawing/intellect_drawing.png", filename="intellect_drawing.png")
        embed.set_image(url="attachment://intellect_drawing.png")
    if argu == "charisma":
        plt.clf()
        plt.figure(facecolor="gray")
        plt.axes().set_facecolor("black")
        plt.plot([0,1,2,3,4,5,6,7,8,9],[x.charisma[0] for x in enchance])
        plt.plot([0,1,2,3,4,5,6,7,8,9],[x.charisma[1] for x in enchance])
        plt.savefig("rsc/courb_drawing/charisma_drawing.png")
        file = discord.File("rsc/courb_drawing/charisma_drawing.png", filename="charisma_drawing.png")
        embed.set_image(url="attachment://charisma_drawing.png")
    if argu == "wisdom":
        plt.clf()
        plt.figure(facecolor="gray")
        plt.axes().set_facecolor("black")
        plt.plot([0,1,2,3,4,5,6,7,8,9],[x.wisdom[0] for x in enchance])
        plt.plot([0,1,2,3,4,5,6,7,8,9],[x.wisdom[1] for x in enchance])
        plt.savefig("rsc/courb_drawing/wisdom_drawing.png")
        file = discord.File("rsc/courb_drawing/wisdom_drawing.png", filename="wisdom_drawing.png")
        embed.set_image(url="attachment://wisdom_drawing.png")
    return (embed , file)
def isAWeaponEnchance(enchance : list):
    for x in enchance:
        if (x.constitution != (0,0)) or (x.evasion != (0,0)) or (x.intellect != (0,0)) or (x.charisma != (0,0)) or (x.wisdom != (0,0)):
            return False
    return True
def isAArmorEnchance(enchance : list):
    for x in enchance:
        if (x.strength != (0,0)) or (x.dexterity != (0,0)) or (x.bleeding != (0,0)) or (x.intellect != (0,0)) or (x.charisma != (0,0)) or (x.wisdom != (0,0)):
            return False
    return True
def getTheEmbedEnchance(ctx,enchance : list):
    my_liste_of_embed = []
    if isAWeaponEnchance(enchance):
        my_liste_of_embed.append(getEmbedImageEnchance(ctx,"strength",enchance))
        my_liste_of_embed.append(getEmbedImageEnchance(ctx,"dexterity",enchance))
        my_liste_of_embed.append(getEmbedImageEnchance(ctx,"bleeding",enchance))
        my_liste_of_embed.append(getEmbedImageEnchance(ctx,"posture",enchance))
        return my_liste_of_embed
    if isAArmorEnchance(enchance):
        my_liste_of_embed.append(getEmbedImageEnchance(ctx,"posture",enchance))
        my_liste_of_embed.append(getEmbedImageEnchance(ctx,"constitution",enchance))
        my_liste_of_embed.append(getEmbedImageEnchance(ctx,"evasion",enchance))
        return my_liste_of_embed
    else:
        my_liste_of_embed.append(getEmbedImageEnchance(ctx,"strength",enchance))
        my_liste_of_embed.append(getEmbedImageEnchance(ctx,"dexterity",enchance))
        my_liste_of_embed.append(getEmbedImageEnchance(ctx,"bleeding",enchance))
        my_liste_of_embed.append(getEmbedImageEnchance(ctx,"posture",enchance))
        my_liste_of_embed.append(getEmbedImageEnchance(ctx,"constitution",enchance))
        my_liste_of_embed.append(getEmbedImageEnchance(ctx,"evasion",enchance))
        my_liste_of_embed.append(getEmbedImageEnchance(ctx,"intellect",enchance))
        my_liste_of_embed.append(getEmbedImageEnchance(ctx,"charisma",enchance))
        my_liste_of_embed.append(getEmbedImageEnchance(ctx,"wisdom",enchance))
        return my_liste_of_embed
def getCompilePresentation(enchance : list , level : int):
    return "`(" + str(enchance[level].strength[0]) + "," + str(enchance[level].strength[1]) + ")` , " + "`(" + str(enchance[level].dexterity[0]) + "," + str(enchance[level].dexterity[1]) + ")` , " + "`(" + str(enchance[level].bleeding[0]) + "," + str(enchance[level].bleeding[1]) + ")` , " + "`(" + str(enchance[level].posture[0]) + "," + str(enchance[level].posture[1]) + ")` , " + "`(" + str(enchance[level].constitution[0]) + "," + str(enchance[level].constitution[1]) + ")` , " + "`(" + str(enchance[level].evasion[0]) + "," + str(enchance[level].evasion[1]) + ")` , " + "`(" + str(enchance[level].intellect[0]) + "," + str(enchance[level].intellect[1]) + ")` , " + "`(" + str(enchance[level].charisma[0]) + "," + str(enchance[level].charisma[1]) + ")` , " + "`(" + str(enchance[level].wisdom[0]) + "," + str(enchance[level].wisdom[1]) + ")`"
def getFirstEmbedImageEnchance(ctx ,name : str ,enchance : list):
    embed = discord.Embed(
        title="__Statistiques__" ,
        description = "**__" + name + "__**" ,
        color = discord.Colour.purple()
        )
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed.add_field(name="__*Statistics of the level 00__", value=getCompilePresentation(enchance,0), inline=False)
    embed.add_field(name="__*Statistics of the level 01__", value=getCompilePresentation(enchance,1), inline=False)
    embed.add_field(name="__*Statistics of the level 02__", value=getCompilePresentation(enchance,2), inline=False)
    embed.add_field(name="__*Statistics of the level 03__", value=getCompilePresentation(enchance,3), inline=False)
    embed.add_field(name="__*Statistics of the level 04__", value=getCompilePresentation(enchance,4), inline=False)
    embed.add_field(name="__*Statistics of the level 05__", value=getCompilePresentation(enchance,5), inline=False)
    embed.add_field(name="__*Statistics of the level 06__", value=getCompilePresentation(enchance,6), inline=False)
    embed.add_field(name="__*Statistics of the level 07__", value=getCompilePresentation(enchance,7), inline=False)
    embed.add_field(name="__*Statistics of the level 08__", value=getCompilePresentation(enchance,8), inline=False)
    embed.add_field(name="__*Statistics of the level 09__", value=getCompilePresentation(enchance,9), inline=False)
    return embed
def getEmbedImageLore(ctx ,lore):
    embed = discord.Embed(
        title=":u6307: `" + lore.name + "`" ,
        description ="**__Name of the lore event :__** " + " `" + lore.name + "`",
        color = discord.Colour.dark_green()
        )
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed.set_image(url=lore.image_path)
    embed.add_field(name=":prayer_beads: __*Presentation__", value="`" + lore.presentation + "`", inline=False)
    return embed

def getEmbedEquipementType(ctx ,equipement):
    embed = discord.Embed(
        title="__Statistiques__",
        description ="`equipement type`",
        color = discord.Colour.purple()
        )
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed.add_field(name=":aries: `name of the equipement type : `", value="**" + equipement.name + "**", inline=False)
    if isinstance(equipement,rp.WeaponTypeClass):
        embed.add_field(name=nonetxt, value="`list of competences : `", inline=False)
        learn_list = equipement.competences.keys()
        for skill_name in learn_list:
            embed.add_field(name="*" + skill_name + "*", value="*description : * `" + equipement.competences[skill_name].presentation + "` , " + "*state : * `" + equipement.competences[skill_name].state[0] + "` " + "`" + str(equipement.competences[skill_name].state[1]) + " cd`", inline=False)
        embed.add_field(name="__*description*__", value="`" + equipement.description + "`", inline=False)
        embed.add_field(name=":aries: *modifier :*", value="`" + equipement.modifier + "`", inline=False)
        embed.add_field(name="*basic statistics : *", value="strength : " + "`" + str(equipement.strength) + "` | " + " dexterity : " + "`" + str(equipement.dexterity) + "` | " + " bleeding : " + "`" + str(equipement.bleeding) + "` | " + " posture : " + "`" + str(equipement.posture) + "`", inline=False)
    if isinstance(equipement,rp.AccessoryClassTypeClass):
        embed.add_field(name=nonetxt, value="`list of competences : `", inline=False)
        learn_list = equipement.competences.keys()
        for skill_name in learn_list:
            embed.add_field(name="*" + skill_name + "*", value="*description : * `" + equipement.competences[skill_name].presentation + "` , " + "*state : * `" + equipement.competences[skill_name].state[0] + "` " + "`" + str(equipement.competences[skill_name].state[1]) + " cd`", inline=False)
        embed.add_field(name="__*description*__", value="`" + equipement.description + "`", inline=False)
        embed.add_field(name=":aries: *modifier : *", value="`" + equipement.modifier + "`", inline=False)
        pass
    if isinstance(equipement,rp.ArmorClassTypeClass):
        embed.add_field(name="__*description*__", value="`" + equipement.description + "`", inline=False)
        embed.add_field(name="*basic statistics : *", value="posture : " + "`" + str(equipement.posture) + "` | " + " constitution : " + "`" + str(equipement.constitution) + "` | " + " evasion : " + "`" + str(equipement.evasion) + "`", inline=False)
        pass
    embed.set_thumbnail(url=equipement.image_path)
    embed.set_image(url=equipement.image_path)
    return embed
def getEmbedImageRace(ctx ,race):
    embed = discord.Embed(
        title="__Statistiques__" ,
        description = "*Name of the race : *" + " **" + race.name + "**" ,
        color = discord.Colour.purple()
        )
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed.add_field(name=nonetxt, value="`list of competences : `", inline=False)
    for skill_name in race.competences.keys():
        embed.add_field(name="*" + skill_name + "*", value="*description : * `" + race.competences[skill_name].presentation + "` , " + "*state : * `" + race.competences[skill_name].state[0] + "` " + "`" + str(race.competences[skill_name].state[1]) + " cd`", inline=False)
    embed.add_field(name="__*description of the race : *__", value="`" + race.description + "`", inline=False)
    embed.set_thumbnail(url=race.image_path)
    embed.set_image(url=race.image_path)
    return embed
def getEncapsule(enca_value : int , file_procc , split_type=" "):
    if len(file_procc) <= enca_value:
        return [file_procc]
    else:
        if type(file_procc) == list:
            return [file_procc[:enca_value]] + getEncapsule(enca_value,file_procc[enca_value:],split_type)
        elif type(file_procc) == str:
            my_split = file_procc[:enca_value].split(split_type)[-1]
            length = len(my_split)
            if length != 1:
                return [file_procc[:enca_value - length]] + getEncapsule(enca_value,file_procc[enca_value-length:],split_type)
            else:
                return [file_procc[:enca_value]] + getEncapsule(enca_value,file_procc[enca_value:],split_type)
def getTestEmbedImage(ctx,txt : str):
    list_of_embed = []
    list_of_embed_txt = getEncapsule(5,getEncapsule(1022,txt))
    if len(list_of_embed_txt) >= 2:
        first_embed = discord.Embed(
            title="__First Embed__" ,
            description =nonetxt ,
            color = discord.Colour.default()
            )
        first_embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        for txt in list_of_embed_txt[0]:
            first_embed.add_field(name=nonetxt, value="`"+txt+"`", inline=False)
        list_of_embed.append(first_embed)
    if len(list_of_embed_txt) > 2:
        for k in range(1,len(list_of_embed_txt)-1):
            embed = discord.Embed(
                title="__Name__" ,
                description =nonetxt ,
                color = discord.Colour.default()
                )
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
            for txt in list_of_embed_txt[k]:
                embed.add_field(name=nonetxt, value="`"+txt+"`", inline=False)
            list_of_embed.append(embed)
    last_embed = discord.Embed(
        title="__Last Embed__" ,
        description =nonetxt ,
        color = discord.Colour.default()
        )
    last_embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    for txt in list_of_embed_txt[len(list_of_embed_txt)-1]:
        last_embed.add_field(name=nonetxt, value="`"+txt+"`", inline=False)
    last_embed.set_image(url="https://cdn.discordapp.com/attachments/1002657461842497597/1013535251777196163/Vierges_du_Sang_Symbole.png")
    list_of_embed.append(last_embed)
    return list_of_embed
def getListEmbedImageOrganisation(ctx ,organisation):
    list_of_embed = []
    list_of_embed_txt = getEncapsule(5,getEncapsule(1022,organisation.presentation))
    if len(list_of_embed_txt) >= 2:
        first_embed = discord.Embed(
            title="__Statistiques__" ,
            description ="`organisation information`" ,
            color = discord.Colour.dark_green()
            )
        first_embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        first_embed.set_image(url=organisation.image_path)
        for txt in list_of_embed_txt[0]:
            first_embed.add_field(name="__*Description of the organisation__ : ", value="`"+txt+"`", inline=False)
        list_of_embed.append(first_embed)
    if len(list_of_embed_txt) > 2:
        for k in range(1,len(list_of_embed_txt)-1):
            embed = discord.Embed(
                title="__Statistiques__" ,
                description ="`organisation information`" ,
                color = discord.Colour.dark_green()
                )
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
            embed.set_image(url=organisation.image_path)
            for txt in list_of_embed_txt[k]:
                embed.add_field(name="__*Description of the organisation__ : ", value="`"+txt+"`", inline=False)
            list_of_embed.append(embed)
    last_embed = discord.Embed(
        title="__Statistiques__" ,
        description ="`(" +str(organisation.life[0]) +"/" + str(organisation.life[1]) +") hp`" ,
        color = discord.Colour.dark_green()
        )
    last_embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    last_embed.set_image(url=organisation.image_path)
    for txt in list_of_embed_txt[len(list_of_embed_txt)-1]:
        last_embed.add_field(name="__*Description of the organisation__ : ", value="`"+txt+"`", inline=False)
    last_embed.add_field(name="*Name of the organisation:*" + " **" + organisation.name + "**", value=nonetxt, inline=False)
    last_embed.add_field(name="__*Capital possessions of the organisation__ : ", value="`"+str(organisation.capital) + " golds`", inline=False)
    last_embed.add_field(name="__*Bonus statistics of the organisation__", value=getCompilePresentation([organisation],0), inline=False)
    list_of_embed.append(last_embed)
    return list_of_embed
    return embed
def getListEmbedImageLore(ctx,lore):
    list_of_embed = []
    list_of_embed_txt = getEncapsule(5,getEncapsule(1022,lore.presentation))
    if len(list_of_embed_txt) >= 2:
        first_embed = discord.Embed(
            title=":u6307: `" + lore.name + "`" ,
            description=":u6307: **__lore event :__** " + " `" + lore.name + "`" ,
            color = discord.Colour.dark_green()
            )
        first_embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        first_embed.set_image(url=lore.image_path)
        list_of_embed.append(first_embed)
    if len(list_of_embed_txt) > 1:
        for k in range(len(list_of_embed_txt)):
            embed = discord.Embed(
                title=":u6307: `" + lore.name + "`" ,
                description =nonetxt ,
                color = discord.Colour.dark_green()
                )
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
            for txt in list_of_embed_txt[k]:
                embed.add_field(name=nonetxt, value="`"+txt+"`", inline=False)
            list_of_embed.append(embed)
    last_embed = discord.Embed(
        title=":u6307: `" + lore.name + "`" ,
        description =":u6307: **__lore event :__** " + " `" + lore.name + "`" ,
        color = discord.Colour.dark_green()
        )
    last_embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    for txt in list_of_embed_txt[len(list_of_embed_txt)-1]:
        last_embed.add_field(name=nonetxt, value="`"+txt+"`", inline=False)
    last_embed.set_image(url=lore.image_path)
    list_of_embed.append(last_embed)
    return list_of_embed
def lenDivisionAuxiliar(my_list : list ,enca_value : int , txt=""):
    if my_list == []:
        return txt
    else:
        if len(my_list) > enca_value:
            return txt
        else:
            if (len(txt) + len(my_list[0]) + 4) < enca_value:
                return lenDivisionAuxiliar(my_list[1:],enca_value,txt + " `" + my_list[0] + "` ")
            else:
                return txt
def getLenDivisionList(my_list : list, enca_value : int):
    if my_list == []:
        return []
    else:
        new_txt = lenDivisionAuxiliar(my_list,enca_value)
        return [new_txt] + getLenDivisionList(my_list[(len(new_txt.split(" `")) - 1):], enca_value)
def getListEmbedSkillsList(ctx ,skill_list_name : list , filter_type : str):
    display_txt_list = getLenDivisionList(skill_list_name, 1022)
    list_of_embed = []
    list_of_embed_txt = getEncapsule(5,display_txt_list)
    if len(list_of_embed_txt) >= 2:
        first_embed = discord.Embed(
            title="__List of Skills__      , *filter : *" ,
            description="`" + filter_type + "`" ,
            color = discord.Colour.default()
            )
        first_embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        for txt in list_of_embed_txt[0]:
            first_embed.add_field(name=nonetxt, value=txt, inline=False)
        first_embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1002657461842497597/1013535251777196163/Vierges_du_Sang_Symbole.png")
        list_of_embed.append(first_embed)
    if len(list_of_embed_txt) > 2:
        for k in range(1,len(list_of_embed_txt)-1):
            embed = discord.Embed(
                title="__List of Skills__*" ,
                description =nonetxt ,
                color = discord.Colour.default()
                )
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
            for txt in list_of_embed_txt[k]:
                embed.add_field(name=nonetxt, value=txt, inline=False)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1002657461842497597/1013535251777196163/Vierges_du_Sang_Symbole.png")
            list_of_embed.append(embed)
    last_embed = discord.Embed(
        title="__List of Skills__      , *filter : *" ,
        description ="`" + filter_type + "`" ,
        color = discord.Colour.default()
        )
    last_embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    for txt in list_of_embed_txt[len(list_of_embed_txt)-1]:
        last_embed.add_field(name=nonetxt, value=txt, inline=False)
    last_embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1002657461842497597/1013535251777196163/Vierges_du_Sang_Symbole.png")
    list_of_embed.append(last_embed)
    return list_of_embed
def getListEmbedEnchancesList(ctx ,enchance_list_name : list):
    display_txt_list = getLenDivisionList(enchance_list_name, 1022)
    list_of_embed = []
    list_of_embed_txt = getEncapsule(5,display_txt_list)
    if len(list_of_embed_txt) >= 2:
        first_embed = discord.Embed(
            title="__List of Enchance__*" ,
            description=nonetxt ,
            color = discord.Colour.default()
            )
        first_embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        for txt in list_of_embed_txt[0]:
            first_embed.add_field(name=nonetxt, value=txt, inline=False)
        first_embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1002657461842497597/1013535251777196163/Vierges_du_Sang_Symbole.png")
        list_of_embed.append(first_embed)
    if len(list_of_embed_txt) > 2:
        for k in range(1,len(list_of_embed_txt)-1):
            embed = discord.Embed(
                title="__List of Enchance__*" ,
                description =nonetxt ,
                color = discord.Colour.default()
                )
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
            for txt in list_of_embed_txt[k]:
                embed.add_field(name=nonetxt, value=txt, inline=False)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1002657461842497597/1013535251777196163/Vierges_du_Sang_Symbole.png")
            list_of_embed.append(embed)
    last_embed = discord.Embed(
        title="__List of Enchance__*" ,
        description =nonetxt ,
        color = discord.Colour.default()
        )
    last_embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    for txt in list_of_embed_txt[len(list_of_embed_txt)-1]:
        last_embed.add_field(name=nonetxt, value=txt, inline=False)
    last_embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1002657461842497597/1013535251777196163/Vierges_du_Sang_Symbole.png")
    list_of_embed.append(last_embed)
    return list_of_embed
def getListEmbedLoreList(ctx ,lore_list_name : list):
    display_txt_list = getLenDivisionList(lore_list_name, 1022)
    list_of_embed = []
    list_of_embed_txt = getEncapsule(5,display_txt_list)
    if len(list_of_embed_txt) >= 2:
        first_embed = discord.Embed(
            title="__List of Lore events__*" ,
            description=nonetxt ,
            color = discord.Colour.default()
            )
        first_embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        for txt in list_of_embed_txt[0]:
            first_embed.add_field(name=nonetxt, value=txt, inline=False)
        first_embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1002657461842497597/1013535251777196163/Vierges_du_Sang_Symbole.png")
        list_of_embed.append(first_embed)
    if len(list_of_embed_txt) > 2:
        for k in range(1,len(list_of_embed_txt)-1):
            embed = discord.Embed(
                title="__List of Lore events__*" ,
                description =nonetxt ,
                color = discord.Colour.default()
                )
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
            for txt in list_of_embed_txt[k]:
                embed.add_field(name=nonetxt, value=txt, inline=False)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1002657461842497597/1013535251777196163/Vierges_du_Sang_Symbole.png")
            list_of_embed.append(embed)
    last_embed = discord.Embed(
        title="__List of Lore events__*" ,
        description =nonetxt ,
        color = discord.Colour.default()
        )
    last_embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    for txt in list_of_embed_txt[len(list_of_embed_txt)-1]:
        last_embed.add_field(name=nonetxt, value=txt, inline=False)
    last_embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1002657461842497597/1013535251777196163/Vierges_du_Sang_Symbole.png")
    list_of_embed.append(last_embed)
    return list_of_embed
def getListEmbedOrganisationList(ctx ,organisation_list_name : list):
    display_txt_list = getLenDivisionList(organisation_list_name, 1022)
    list_of_embed = []
    list_of_embed_txt = getEncapsule(5,display_txt_list)
    if len(list_of_embed_txt) >= 2:
        first_embed = discord.Embed(
            title="__List of Organisations__*" ,
            description=nonetxt ,
            color = discord.Colour.default()
            )
        first_embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        for txt in list_of_embed_txt[0]:
            first_embed.add_field(name=nonetxt, value=txt, inline=False)
        first_embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1002657461842497597/1013535251777196163/Vierges_du_Sang_Symbole.png")
        list_of_embed.append(first_embed)
    if len(list_of_embed_txt) > 2:
        for k in range(1,len(list_of_embed_txt)-1):
            embed = discord.Embed(
                title="__List of Organisations__*" ,
                description =nonetxt ,
                color = discord.Colour.default()
                )
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
            for txt in list_of_embed_txt[k]:
                embed.add_field(name=nonetxt, value=txt, inline=False)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1002657461842497597/1013535251777196163/Vierges_du_Sang_Symbole.png")
            list_of_embed.append(embed)
    last_embed = discord.Embed(
        title="__List of Organisations__*" ,
        description =nonetxt ,
        color = discord.Colour.default()
        )
    last_embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    for txt in list_of_embed_txt[len(list_of_embed_txt)-1]:
        last_embed.add_field(name=nonetxt, value=txt, inline=False)
    last_embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1002657461842497597/1013535251777196163/Vierges_du_Sang_Symbole.png")
    list_of_embed.append(last_embed)
    return list_of_embed
def getListEmbedRaceList(ctx ,race_list_name : list):
    display_txt_list = getLenDivisionList(race_list_name, 1022)
    list_of_embed = []
    list_of_embed_txt = getEncapsule(5,display_txt_list)
    if len(list_of_embed_txt) >= 2:
        first_embed = discord.Embed(
            title="__List of Races__*" ,
            description=nonetxt ,
            color = discord.Colour.default()
            )
        first_embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        for txt in list_of_embed_txt[0]:
            first_embed.add_field(name=nonetxt, value=txt, inline=False)
        first_embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1002657461842497597/1013535251777196163/Vierges_du_Sang_Symbole.png")
        list_of_embed.append(first_embed)
    if len(list_of_embed_txt) > 2:
        for k in range(1,len(list_of_embed_txt)-1):
            embed = discord.Embed(
                title="__List of Races__*" ,
                description =nonetxt ,
                color = discord.Colour.default()
                )
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
            for txt in list_of_embed_txt[k]:
                embed.add_field(name=nonetxt, value=txt, inline=False)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1002657461842497597/1013535251777196163/Vierges_du_Sang_Symbole.png")
            list_of_embed.append(embed)
    last_embed = discord.Embed(
        title="__List of Races__*" ,
        description =nonetxt ,
        color = discord.Colour.default()
        )
    last_embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    for txt in list_of_embed_txt[len(list_of_embed_txt)-1]:
        last_embed.add_field(name=nonetxt, value=txt, inline=False)
    last_embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1002657461842497597/1013535251777196163/Vierges_du_Sang_Symbole.png")
    list_of_embed.append(last_embed)
    return list_of_embed
def getListEmbedClasseList(ctx ,classe_list_name : list):
    display_txt_list = getLenDivisionList(classe_list_name, 1022)
    list_of_embed = []
    list_of_embed_txt = getEncapsule(5,display_txt_list)
    if len(list_of_embed_txt) >= 2:
        first_embed = discord.Embed(
            title="__List of Classes__*" ,
            description=nonetxt ,
            color = discord.Colour.default()
            )
        first_embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        for txt in list_of_embed_txt[0]:
            first_embed.add_field(name=nonetxt, value=txt, inline=False)
        first_embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1002657461842497597/1013535251777196163/Vierges_du_Sang_Symbole.png")
        list_of_embed.append(first_embed)
    if len(list_of_embed_txt) > 2:
        for k in range(1,len(list_of_embed_txt)-1):
            embed = discord.Embed(
                title="__List of Classes__*" ,
                description =nonetxt ,
                color = discord.Colour.default()
                )
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
            for txt in list_of_embed_txt[k]:
                embed.add_field(name=nonetxt, value=txt, inline=False)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1002657461842497597/1013535251777196163/Vierges_du_Sang_Symbole.png")
            list_of_embed.append(embed)
    last_embed = discord.Embed(
        title="__List of Classes__*" ,
        description =nonetxt ,
        color = discord.Colour.default()
        )
    last_embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    for txt in list_of_embed_txt[len(list_of_embed_txt)-1]:
        last_embed.add_field(name=nonetxt, value=txt, inline=False)
    last_embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1002657461842497597/1013535251777196163/Vierges_du_Sang_Symbole.png")
    list_of_embed.append(last_embed)
    return list_of_embed
def getListEmbedEquipementList(ctx ,equipement_list_name : list):
    display_txt_list = getLenDivisionList(equipement_list_name, 1022)
    list_of_embed = []
    list_of_embed_txt = getEncapsule(5,display_txt_list)
    if len(list_of_embed_txt) >= 2:
        first_embed = discord.Embed(
            title="__List of Equipement-Types__*" ,
            description=nonetxt ,
            color = discord.Colour.default()
            )
        first_embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        for txt in list_of_embed_txt[0]:
            first_embed.add_field(name=nonetxt, value=txt, inline=False)
        first_embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1002657461842497597/1013535251777196163/Vierges_du_Sang_Symbole.png")
        list_of_embed.append(first_embed)
    if len(list_of_embed_txt) > 2:
        for k in range(1,len(list_of_embed_txt)-1):
            embed = discord.Embed(
                title="__List of Equipement-Types__*" ,
                description =nonetxt ,
                color = discord.Colour.default()
                )
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
            for txt in list_of_embed_txt[k]:
                embed.add_field(name=nonetxt, value=txt, inline=False)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1002657461842497597/1013535251777196163/Vierges_du_Sang_Symbole.png")
            list_of_embed.append(embed)
    last_embed = discord.Embed(
        title="__List of Equipement-Types__*" ,
        description =nonetxt ,
        color = discord.Colour.default()
        )
    last_embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    for txt in list_of_embed_txt[len(list_of_embed_txt)-1]:
        last_embed.add_field(name=nonetxt, value=txt, inline=False)
    last_embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1002657461842497597/1013535251777196163/Vierges_du_Sang_Symbole.png")
    list_of_embed.append(last_embed)
    return list_of_embed
def getListEmbedImageClasse(ctx ,classe):
    list_of_embed = []
    list_of_embed_txt = getEncapsule(4,getEncapsule(1022,classe.description))
    list_of_embed_skills = getEncapsule(10,list(classe.competences.keys()))
    max_len = max(len(list_of_embed_txt),len(list_of_embed_skills))
    if max_len >= 2:
        first_embed = discord.Embed(
            title="__Statistiques__" ,
            description ="*Name of the classe : *" + " **" + classe.name + "**" ,
            color = discord.Colour.purple()
            )
        first_embed.add_field(name="*modifier*", value="`"+ classe.modifier +"`", inline=False)
        first_embed.add_field(name=nonetxt, value="`list of competences : `", inline=False)
        for skill_name in list_of_embed_skills[0]:
            first_embed.add_field(name="*" + skill_name + "Lv  : (" + str(classe.competences[skill_name].level) + ")*", value="*description : * `" + classe.competences[skill_name].presentation + "` , " + "*state : * `" + classe.competences[skill_name].state[0] + "` " + "`" + str(classe.competences[skill_name].state[1]) + " cd`", inline=False)
        first_embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        if (len(list_of_embed_txt) !=1 and max_len) == 2 or len(list_of_embed_txt) >= 2:
            for txt in list_of_embed_txt[0]:
                first_embed.add_field(name=nonetxt, value="`"+txt+"`", inline=False)
        first_embed.set_thumbnail(url=classe.image_path)
        list_of_embed.append(first_embed)
    if max_len > 2:
        for k in range(1,max_len-1):
            embed = discord.Embed(
                title="__Statistiques__" ,
                description =nonetxt ,
                color = discord.Colour.purple()
                )
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
            if k < len(list_of_embed_skills):
                for skill_name in list_of_embed_skills[k]:
                    embed.add_field(name="*" + skill_name + "Lv  : (" + str(classe.competences[skill_name].level) + ")*", value="*description : * `" + classe.competences[skill_name].presentation + "` , " + "*state : * `" + classe.competences[skill_name].state[0] + "` " + "`" + str(classe.competences[skill_name].state[1]) + " cd`", inline=False)
            if k < len(list_of_embed_txt):
                for txt in list_of_embed_txt[k]:
                    embed.add_field(name=nonetxt, value="`"+txt+"`", inline=False)
            embed.set_thumbnail(url=classe.image_path)
            list_of_embed.append(embed)
    last_embed = discord.Embed(
        title="__Statistiques__" ,
        description ="*Name of the classe : *" + " **" + classe.name + "**" ,
        color = discord.Colour.purple()
        )
    last_embed.add_field(name="*modifier*", value="`"+ classe.modifier +"`", inline=False)
    last_embed.add_field(name=nonetxt, value="`list of competences : `", inline=False)
    if max_len == 1:
        for skill_name in classe.competences.keys():
            last_embed.add_field(name="*" + skill_name + "Lv  : (" + str(classe.competences[skill_name].level) + ")*", value="*description : * `" + classe.competences[skill_name].presentation + "` , " + "*state : * `" + classe.competences[skill_name].state[0] + "` " + "`" + str(classe.competences[skill_name].state[1]) + " cd`", inline=False)
    else:
        for skill_name in list_of_embed_skills[-1]:
            last_embed.add_field(name="*" + skill_name + "Lv  : (" + str(classe.competences[skill_name].level) + ")*", value="*description : * `" + classe.competences[skill_name].presentation + "` , " + "*state : * `" + classe.competences[skill_name].state[0] + "` " + "`" + str(classe.competences[skill_name].state[1]) + " cd`", inline=False)
    last_embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    last_embed.set_thumbnail(url=classe.image_path)
    for txt in list_of_embed_txt[len(list_of_embed_txt)-1]:
        last_embed.add_field(name="Lore Of The Class", value="`"+txt+"`", inline=False)
    list_of_embed.append(last_embed)
    last_last_embed = discord.Embed(
        title="__Statistiques__" ,
        description ="*Name of the classe : *" + " **" + classe.name + "**" ,
        color = discord.Colour.purple()
        )
    last_last_embed.set_thumbnail(url=classe.image_path)
    last_last_embed.set_image(url=classe.image_path)
    last_last_embed.set_footer(text="afficher par: {}".format(ctx.author.display_name))
    list_of_embed.append(last_last_embed)
    return list_of_embed
def getListEmbedImageRace(ctx ,race):
    list_of_embed = []
    list_of_embed_txt = getEncapsule(4,getEncapsule(1022,race.description))
    if len(list_of_embed_txt) >= 2:
        first_embed = discord.Embed(
            title="__Statistiques__" ,
            description ="*Name of the race : *" + " **" + classe.name + "**" ,
            color = discord.Colour.purple()
            )
        first_embed.add_field(name=nonetxt, value="`list of competences : `", inline=False)
        for skill_name in race.competences.keys():
            first_embed.add_field(name="*" + skill_name + "*", value="*description : * `" + race.competences[skill_name].presentation + "` , " + "*state : * `" + race.competences[skill_name].state[0] + "` " + "`" + str(race.competences[skill_name].state[1]) + " cd`", inline=False)
        first_embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        for txt in list_of_embed_txt[0]:
            first_embed.add_field(name=nonetxt, value="`"+txt+"`", inline=False)
        first_embed.set_thumbnail(url=race.image_path)
        list_of_embed.append(first_embed)
    if len(list_of_embed_txt) > 2:
        for k in range(1,len(list_of_embed_txt)-1):
            embed = discord.Embed(
                title="__Statistiques__" ,
                description =nonetxt ,
                color = discord.Colour.purple()
                )
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
            for txt in list_of_embed_txt[k]:
                embed.add_field(name=nonetxt, value="`"+txt+"`", inline=False)
            embed.set_thumbnail(url=race.image_path)
            list_of_embed.append(embed)
    last_embed = discord.Embed(
        title="__Statistiques__" ,
        description ="*Name of the race : *" + " **" + race.name + "**" ,
        color = discord.Colour.purple()
        )
    if len(list_of_embed_txt) == 1:
        last_embed.add_field(name=nonetxt, value="`list of competences : `", inline=False)
        for skill_name in race.competences.keys():
            last_embed.add_field(name="*" + skill_name + "*", value="*description : * `" + race.competences[skill_name].presentation + "` , " + "*state : * `" + race.competences[skill_name].state[0] + "` " + "`" + str(race.competences[skill_name].state[1]) + " cd`", inline=False)
    last_embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    for txt in list_of_embed_txt[len(list_of_embed_txt)-1]:
        last_embed.add_field(name=nonetxt, value="`"+txt+"`", inline=False)
    last_embed.set_thumbnail(url=race.image_path)
    last_embed.set_image(url=race.image_path)
    list_of_embed.append(last_embed)
    return list_of_embed
def getTitlesString(character):
    txt = ""
    for name in character.title_list:
        txt = txt + " `" + name + "` "
    return txt
def getLanguagesString(character):
    txt = ""
    for name in character.languages:
        txt = txt + " `" + name + "` "
    return txt
def getBackgroundString(character):
    txt = ""
    for name in character.background:
        txt = txt + "  `" + name + "`  "
    return txt
def getFirstEmbedImageCharacter(ctx ,character):
    embed = discord.Embed(
        title="__Statistiques Of " + character.name + "__" ,
        description = ":u6307: `character board : `   " + "*character state :* `" + character.state[0] + "`" ,
        color = discord.Colour.dark_green()
        )
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed.add_field(name=":medical_symbol: __Level__ __of__ __The__ __Character__`:`", value="*Lv :* " + "`" + str(character.level)+ "`", inline=True)
    embed.add_field(name=":fleur_de_lis: __Sub__ __Level__ `:`", value="*Pl :* " + "`0`", inline=True)

    
    embed.add_field(name="__*character name : __ `" + character.name + " `" + "   __*character allignement : __ `" + character.alignement + " `", value="__*character nick-name : __ `" + character.nickname + "`", inline=False)


    embed.add_field(name=":white_heart: __Health__ __of__ __The__ __Character__", value="**Hp : ** " + "`" + str(character.life[0]) + "`  ** \ **  `" + str(character.life[1]) + "`", inline=True)
    embed.add_field(name=":white_large_square: __*character languages : __", value=getLanguagesString(character), inline=True)



    embed.add_field(name="__**character background : **__", value=getBackgroundString(character), inline=False)
    embed.add_field(name="__*character titles : __", value=getTitlesString(character), inline=False)



    if character.weapon01 == character.main_weapon:
        embed.add_field(name=" :x_ray: __*first weapon__ __| Main Weapon__ `name/type/enchance/level :`:*", value="`" + character.weapon01.name + "`  **/**  `" + character.weapon01.weapon_type.name + "`  **/**  `" + character.weapon01.enchance_name + "`  **/**  `" + str(character.weapon01.level) + "`", inline=False)
    else:
        embed.add_field(name=" :x_ray: __*first weapon__ `name/type/enchance/level :`:*", value="`" + character.weapon01.name + "`  **/**  `" + character.weapon01.weapon_type.name + "`  **/**  `" + character.weapon01.enchance_name + "`  **/**  `" + str(character.weapon01.level) + "`", inline=False)
    if character.weapon02 == character.main_weapon:
        embed.add_field(name=" :x_ray: __*second weapon__ __| Main Weapon__ `name/type/enchance/level :`:*", value="`" + character.weapon02.name + "`  **/**  `" + character.weapon02.weapon_type.name + "`  **/**  `" + character.weapon02.enchance_name + "`  **/**  `" + str(character.weapon02.level) + "`", inline=False)
    else:
        embed.add_field(name=" :x_ray: __*second weapon__ `name/type/enchance/level :`:*", value="`" + character.weapon02.name + "`  **/**  `" + character.weapon02.weapon_type.name + "`  **/**  `" + character.weapon02.enchance_name + "`  **/**  `" + str(character.weapon02.level) + "`", inline=False)
    if character.weapon03 == character.main_weapon:
        embed.add_field(name=" :x_ray: __*third weapon__ __| Main Weapon__ `name/type/enchance/level :`:*", value="`" + character.weapon03.name + "`  **/**  `" + character.weapon03.weapon_type.name + "`  **/**  `" + character.weapon03.enchance_name + "`  **/**  `" + str(character.weapon03.level) + "`", inline=False)
    else:
        embed.add_field(name=" :x_ray: __*third weapon__ `name/type/enchance/level :`:*", value="`" + character.weapon03.name + "`  **/**  `" + character.weapon03.weapon_type.name + "`  **/**  `" + character.weapon03.enchance_name + "`  **/**  `" + str(character.weapon03.level) + "`", inline=False)
    
    embed.add_field(name=" :prayer_beads: __*first accessory__ `name/type/enchance/level :`:*", value= "`" + character.accessorry01.name + "`  **/**  `" + character.accessorry01.accessory_type.name + "`  **/**  `" + character.accessorry01.enchance_name + "`  **/**  `" + str(character.accessorry01.level) + "`", inline=False)
    embed.add_field(name=" :prayer_beads: __*second accessory__ `name/type/enchance/level :`:*", value= "`" + character.accessorry02.name + "`  **/**  `" + character.accessorry02.accessory_type.name + "`  **/**  `" + character.accessorry02.enchance_name + "`  **/**  `" + str(character.accessorry02.level) + "`", inline=False)

    embed.add_field(name=" :shield: __*armor equiped__ `name/type/enchance/level :`:*", value= "`" + character.armor.name + "`  **/**  `" + character.armor.armor_type.name + "`  **/**  `" + character.armor.enchance_name + "`  **/**  `" + str(character.armor.level) + "`", inline=False)


    
    embed.add_field(name=":u6307: __*character organisation : *__", value="`" + character.organisation.name + "`", inline=False)
    
    

 
    
    embed.add_field(name=":curly_loop: __*arcanes value(int) : __", value="**+** `" + str(character.arcanes) + "`", inline=True)
    embed.add_field(name=":curly_loop: __*athletics value(for) : __", value="**+** `" + str(character.athletics) + "`", inline=True)
    embed.add_field(name=":curly_loop: __*discretion value(dex) : __", value="**+** `" + str(character.discretion) + "`", inline=True)
    embed.add_field(name=":curly_loop: __*history value(int) : __", value="**+** `" + str(character.history) + "`", inline=True)
    embed.add_field(name=":curly_loop: __*intimidation value(cha) : __", value="**+** `" + str(character.intimidation) + "`", inline=True)
    embed.add_field(name=":curly_loop: __*investigation value(dex) : __", value="**+** `" + str(character.investigation) + "`", inline=True)

    embed.add_field(name=":curly_loop: __*medicine value(int) : __", value="**+** `" + str(character.medicine) + "`", inline=True)

    embed.add_field(name=":curly_loop: __*religion value(sag) : __", value="**+** `" + str(character.religion) + "`", inline=True)
    embed.add_field(name=":curly_loop: __*survive value(sag) : __", value="**+** `" + str(character.survive) + "`", inline=True)
    embed.add_field(name=":curly_loop: __*occultism value(int) : __", value="**+** `" + str(character.occultism) + "`", inline=True)
    embed.add_field(name=":curly_loop: __*calm value(cha) : __", value="**+** `" + str(character.calm) + "`", inline=True)


    embed.set_thumbnail(url=character.image_path)
    embed.set_image(url=character.image_path)
    return embed
def getSecondEmbedImageCharacter(ctx ,character):
    embed = discord.Embed(
        title="__Statistiques Of " + character.name + "__" ,
        description = ":u6307: `character board : `   " + "*character state :* `" + character.state[0] + "`",
        color = discord.Colour.dark_green()
        )
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    

    embed.add_field(name="__*character race : *__                                    __*character class : *__", value="`" + character.race.name + "`" + nonetxt*23 + "`" + character.classe.name + "`", inline=False)


    embed.add_field(name="__**capital of the character : **__", value="`"+ str(character.capital) + "` :coin: **golds**", inline=False)
    embed.add_field(name="__**character presentation : **__", value="`"+ getEncapsule(1000,character.presentation)[0] + "`", inline=False)
    
    embed.add_field(name=":white_small_square: __strength value : __", value="` |" + str(character.strength[0]) + "| + " + str(character.strength[1]) + "`", inline=True)
    embed.add_field(name=":white_small_square: __dexterity value : __", value="` |" + str(character.dexterity[0]) + "| + " + str(character.dexterity[1]) + "`", inline=True)
    embed.add_field(name=":white_small_square: __bleeding value : __", value="` |" + str(character.bleeding[0]) + "| + " + str(character.bleeding[1]) + "`", inline=True)
    embed.add_field(name=":white_small_square: __posture value : __", value="` |" + str(character.posture[0]) + "| + " + str(character.posture[1]) + "`", inline=True)
    embed.add_field(name=":white_small_square: __constitution value : __", value="` |" + str(character.constitution[0]) + "| + " + str(character.constitution[1]) + "`", inline=True)
    embed.add_field(name=":white_small_square: __evasion value : __", value="` |" + str(character.evasion[0]) + "| + " + str(character.evasion[1]) + "`", inline=True)
    embed.add_field(name=":white_small_square: __intellect value : __", value="` |" + str(character.intellect[0]) + "| + " + str(character.intellect[1]) + "`", inline=True)
    embed.add_field(name=":white_small_square: __charisma value : __", value="` |" + str(character.charisma[0]) + "| + " + str(character.charisma[1]) + "`", inline=True)
    embed.add_field(name=":white_small_square: __wisdom value : __", value="` |" + str(character.wisdom[0]) + "| + " + str(character.wisdom[1]) + "`", inline=True)
    embed.set_thumbnail(url=character.image_path)
    embed.set_image(url=character.image_path)
    return embed
def getListLoreCharacterEmbedImage(ctx,txt : str,character):
    list_of_embed = []
    list_of_embed_txt = getEncapsule(5,getEncapsule(1022,txt))
    if len(list_of_embed_txt) >= 2:
        first_embed = discord.Embed(
            title="__Lore Of " + character.name + "__" ,
            description =nonetxt ,
            color = discord.Colour.default()
            )
        first_embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        first_embed.set_thumbnail(url=character.image_path)
        first_embed.set_image(url=character.image_path)
        for txt in list_of_embed_txt[0]:
            first_embed.add_field(name=nonetxt, value="`"+txt+"`", inline=False)
        list_of_embed.append(first_embed)
    if len(list_of_embed_txt) > 2:
        for k in range(1,len(list_of_embed_txt)-1):
            embed = discord.Embed(
                title="__Lore Of " + character.name + "__" ,
                description =nonetxt ,
                color = discord.Colour.default()
                )
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url=character.image_path)
            embed.set_image(url=character.image_path)
            for txt in list_of_embed_txt[k]:
                embed.add_field(name=nonetxt, value="`"+txt+"`", inline=False)
            list_of_embed.append(embed)
    last_embed = discord.Embed(
        title="__Lore Of " + character.name + "__" ,
        description =nonetxt ,
        color = discord.Colour.default()
        )
    last_embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    last_embed.set_thumbnail(url=character.image_path)
    for txt in list_of_embed_txt[len(list_of_embed_txt)-1]:
        last_embed.add_field(name=nonetxt, value="`"+txt+"`", inline=False)
    last_embed.set_image(url=character.image_path)
    list_of_embed.append(last_embed)
    return list_of_embed
def getEmbedImageCharacterEquipement(ctx ,equipement):
    embed = discord.Embed(
        title=":clubs: __Statistiques Of " + equipement.name + "__" ,
        description = ":u6307: `" + equipement.description + "`" ,
        color = discord.Colour.dark_green()
        )
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    if isinstance(equipement,rp.WeaponClass):
        embed.set_thumbnail(url=equipement.weapon_type.image_path)
        embed.set_image(url=equipement.weapon_type.image_path)
        embed.add_field(name=":clubs: *Modifier : *", value="`"+equipement.weapon_type.modifier+"`", inline=False)
        embed.add_field(name="__**Statistiques : **__", value="**strength : **" + "`|" + str(equipement.strength[0]) + "| +" + str(equipement.strength[1]) + "`  " + "**dexterity : **" + "`|" + str(equipement.dexterity[0]) +"| +" + str(equipement.dexterity[1]) + "`  " + "**bleeding : **" + "`|" + str(equipement.bleeding[0]) + "| +" + str(equipement.bleeding[1]) + "`  " + "**posture : **" + "`|"+ str(equipement.posture[0]) +"| +" + str(equipement.posture[1]) + "`", inline=False)
        embed.add_field(name=":u6307: **level of " + equipement.name + " : **", value="` "+str(equipement.level)+" `", inline=False)
        embed.add_field(name=":clubs: __enchance " + equipement.name + " : __", value="` "+str(equipement.enchance_name)+" `", inline=False)
        embed.add_field(name=nonetxt, value="`skill list : `", inline=False)
        for name in equipement.weapon_type.competences.keys():
            embed.add_field(name="__*" + equipement.weapon_type.competences[name].name + "*__", value="`"+ equipement.weapon_type.competences[name].state[0] + "`  **|**  `" + str(equipement.weapon_type.competences[name].state[1]) + "`  **cd : **  `" + str(equipement.weapon_type.competences[name].competence_cooldown) + "`", inline=False)
        pass
    if isinstance(equipement,rp.AccessoryClass):
        embed.set_thumbnail(url=equipement.accessory_type.image_path)
        embed.set_image(url=equipement.accessory_type.image_path)
        embed.add_field(name=":clubs: *Modifier : *", value="`"+equipement.accessory_type.modifier+"`", inline=False)
        embed.add_field(name="__**Statistiques : **__", value="**strength : **" + "`|" + str(equipement.strength[0]) + "| +" + str(equipement.strength[1]) + "`  " + "**dexterity : **" + "`|"+ str(equipement.dexterity[0]) +"| +" + str(equipement.dexterity[1]) + "`  " + "**bleeding : **" + "`|"+ str(equipement.bleeding[0]) +"| +" + str(equipement.bleeding[1]) + "`  " + "**posture : **" + "`|"+ str(equipement.posture[0]) +"| +" + str(equipement.posture[1]) + "`  " + "**constitution : **" + "`|"+ str(equipement.constitution[0]) +"| +" + str(equipement.constitution[1]) + "`  " + "**evasion : **" + "`|"+ str(equipement.evasion[0]) +"| +" + str(equipement.evasion[1]) + "`  " + "**intellect : **" + "`|"+ str(equipement.intellect[0]) +"| +" + str(equipement.intellect[1]) + "`  " + "**charisma : **" + "`|"+ str(equipement.charisma[0]) +"| +" + str(equipement.charisma[1]) + "`  " + "**wisdom : **" + "`|"+ str(equipement.wisdom[0]) +"| +" + str(equipement.wisdom[1]) + "`", inline=False)
        embed.add_field(name=":u6307: **level of " + equipement.name + " : **", value="` "+str(equipement.level)+" `", inline=False)
        embed.add_field(name=":clubs: __enchance " + equipement.name + " : __", value="` "+str(equipement.enchance_name)+" `", inline=False)
        embed.add_field(name=nonetxt, value="`skill list : `", inline=False)
        for name in equipement.accessory_type.competences.keys():
            embed.add_field(name="__*" + equipement.accessory_type.competences[name].name + "*__", value="`"+ equipement.accessory_type.competences[name].state[0] + "`  **|**  `" + str(equipement.accessory_type.competences[name].state[1]) + "`  **cd : **  `" + str(equipement.accessory_type.competences[name].competence_cooldown) + "`", inline=False)
        pass
    if isinstance(equipement,rp.ArmorClass):
        embed.set_thumbnail(url=equipement.armor_type.image_path)
        embed.set_image(url=equipement.armor_type.image_path)
        embed.add_field(name="__**Statistiques : **__", value="**posture : **" + "`|"+ str(equipement.posture[0]) +"| +" + str(equipement.posture[1]) + "`  " + "**constitution : **" + "`|"+ str(equipement.constitution[0]) +"| +" + str(equipement.constitution[1]) + "`  " + "**evasion : **" + "`|"+ str(equipement.evasion[0]) +"| +" + str(equipement.evasion[1]) + "`" , inline=False)
        embed.add_field(name=":u6307: **level of " + equipement.name + " : **", value="` "+str(equipement.level)+" `", inline=False)
        embed.add_field(name=":clubs: __enchance " + equipement.name + " : __", value="` "+str(equipement.enchance_name)+" `", inline=False)
        pass
    
    return embed
def getEmbedImageItem(ctx ,item):
    embed = discord.Embed(
        title=":u6307: __Statistiques__" ,
        description ="**item : ** `" + item.name + "`",
        color = discord.Colour.dark_green()
        )
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed.add_field(name=":u6307: *Name of the item:*" + " **" + item.name + "**", value=nonetxt, inline=False)
    if isinstance(item,rp.ConsumableClass):
        embed.add_field(name="__**is consumable**__", value="`regene : ` __**" + str(item.life) + "**__", inline=False)
    if isinstance(item,rp.MagicalConsumableClass):
        embed.add_field(name="__**is a magic consumable**__", value="`regene : ` __**" + str(item.life) + "**__", inline=False)
        embed.add_field(name="*" + item.competence.name + "*", value="*Lv : * `" + str(item.competence.level)+ "`" + " *state : * `" + str(item.competence.state) + "`" + " *type : * `" + str(item.competence.type) + "`", inline=True)
    if isinstance(item,rp.MagicalItemClass):
        embed.add_field(name="__**This is a Magical Item**__", value=nonetxt, inline=False)
        embed.add_field(name="*" + item.competence.name + "*", value="*Lv : * `" + str(item.competence.level)+ "`" + " *cd restant : * `" + str(sktr.getRestCooldown(item.competence))+ "`" + " *cd : * `" + str(item.competence.competence_cooldown)+ "`" + " *state : * `" + str(item.competence.state) + "`" + " *type : * `" + str(item.competence.type) + "`", inline=True)    
    embed.add_field(name=":u6307: __*Description of the item__ : ", value="` " + item.description + "`", inline=False)
    embed.add_field(name=":u6307: __Price__ __Of__ __The__ __Item__ : ", value="` " + str(item.price) + "` :coin: **golds**", inline=False)
    embed.set_image(url=item.image_path)
    embed.set_thumbnail(url=item.image_path)
    return embed
def getInventoryChar(inventory : dict):
    txt = ""
    for item_name in inventory.keys():
        if isinstance(inventory[item_name],rp.ConsumableClass):
            txt = txt + "*name of the item : *`" + item_name + "` , **consummable** ,  *quantity : * `" + str(inventory[item_name].quantity) + "`  \n"
        elif isinstance(inventory[item_name],rp.MagicalConsumableClass):
            txt = txt + "*name of the item : *`" + item_name + "` , **magical consummable** ,  *quantity : * `" + str(inventory[item_name].quantity) + "` , *description : * `" + inventory[item_name].description + "` \n"
        elif isinstance(inventory[item_name],rp.MagicalItemClass):
            txt = txt + "*name of the item : *`" + item_name + "` , **magical item** ,  *quantity : * `" + str(inventory[item_name].quantity) + "` , *description : * `" + inventory[item_name].description + "` \n"
        else:
            txt = txt + "*name of the item : *`" + item_name + "` , *quantity : * `" + str(inventory[item_name].quantity) + "`  \n"
    return txt
def getListInventoryCharacterEmbedImage(ctx,character):
    list_of_embed = []
    list_of_embed_txt = getEncapsule(5,getEncapsule(1022,getInventoryChar(character.inventory)))
    if True:
        for k in range(len(list_of_embed_txt)):
            embed = discord.Embed(
                title="__Inventory Of " + character.name + "__" ,
                description =nonetxt ,
                color = discord.Colour.default()
                )
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
            for txt in list_of_embed_txt[k]:
                embed.add_field(name=nonetxt, value=txt, inline=False)
            list_of_embed.append(embed)
    return list_of_embed
def getListItemEmbedImageList(ctx,item_list : list):
    display_txt_list = getLenDivisionList(item_list, 1022)
    list_of_embed = []
    list_of_embed_txt = getEncapsule(5,display_txt_list)
    if True:
        for k in range(len(list_of_embed_txt)):
            embed = discord.Embed(
                title="__Items List__" ,
                description =nonetxt ,
                color = discord.Colour.default()
                )
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
            for txt in list_of_embed_txt[k]:
                embed.add_field(name=nonetxt, value=txt, inline=False)
            list_of_embed.append(embed)
    return list_of_embed
def getListArchetypesEmbedImageList(ctx,archetypes_list : list):
    display_txt_list = getLenDivisionList(archetypes_list, 1022)
    list_of_embed = []
    list_of_embed_txt = getEncapsule(5,display_txt_list)
    if True:
        for k in range(len(list_of_embed_txt)):
            embed = discord.Embed(
                title="__Archetypes List__" ,
                description =nonetxt ,
                color = discord.Colour.default()
                )
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
            for txt in list_of_embed_txt[k]:
                embed.add_field(name=nonetxt, value=txt, inline=False)
            list_of_embed.append(embed)
    return list_of_embed
def getListKnoledgeEmbedImageList(ctx,knoledge_list : list):
    display_txt_list = getLenDivisionList(knoledge_list, 1022)
    list_of_embed = []
    list_of_embed_txt = getEncapsule(5,display_txt_list)
    if True:
        for k in range(len(list_of_embed_txt)):
            embed = discord.Embed(
                title="__Archetypes List__" ,
                description =nonetxt ,
                color = discord.Colour.default()
                )
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
            for txt in list_of_embed_txt[k]:
                embed.add_field(name=nonetxt, value=txt, inline=False)
            list_of_embed.append(embed)
    return list_of_embed
def getCharWeaponStat(weapon):
    txt = " `|" + str(weapon.strength[0]) + "|+" + str(weapon.strength[1]) + "` " + "`|" + str(weapon.dexterity[0]) + "|+" + str(weapon.dexterity[1]) + "` " + "`|" + str(weapon.bleeding[0]) + "|+" + str(weapon.bleeding[1]) + "` " + "`|" + str(weapon.posture[0]) + "|+" + str(weapon.posture[1]) + "` "
    return txt
def getLiteEmbedCharacter(ctx ,character):
    embed = discord.Embed(
        title="__Statistiques Of " + character.name + "__" ,
        description = ":u6307: `character liteboard : `   " + "*character state :* `" + character.state[0] + "`  " + "***dscr***" + "`"+ getEncapsule(2000,character.presentation)[0] + "`",
        color = discord.Colour.dark_green()
        )
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed.add_field(name=":medical_symbol: __Level__ __of__ __The__ __Character__`:`", value="*Lv :* " + "`" + str(character.level)+ "`", inline=True)
    embed.add_field(name=":fleur_de_lis: __Sub__ __Level__ `:`", value="*Pl :* " + "`0`", inline=True)


    embed.add_field(name=" :x_ray: __*Main weapon__ `name/type/ench/level ` " + getCharWeaponStat(character.main_weapon) + " **:**", value="`" + character.main_weapon.name + "`  **/**  `" + character.main_weapon.weapon_type.name + "`  **/**  `" + character.main_weapon.enchance_name + "`  **/**  `" + str(character.main_weapon.level) + "`", inline=False)
    embed.add_field(name="__*character name : __ `" + character.name + "`" , value="__*character nick-name : __ `" + character.nickname + "`", inline=False)


    embed.add_field(name=":green_heart: __Health__ __of__ __The__ __Character__", value="**Hp : ** " + "`" + str(character.life[0]) + "`  ** \ **  `" + str(character.life[1]) + "`", inline=True)


    embed.add_field(name="__*character class : *__", value="`" + character.classe.name + "`", inline=False)
    embed.add_field(name="__*character race : *__", value="`" + character.race.name + "`", inline=False)
    

    embed.add_field(name="__**capital of the character : **__", value="`"+ str(character.capital) + "` :coin: **golds**", inline=False)
    


    embed.set_thumbnail(url=character.image_path)
    return embed
def getFirstEmbedImageCharacterCompetencesList(ctx ,character):
    my_embed_list = []
    skill_list = getEncapsule(10,list(character.competences.keys()))
    for k in range(len(skill_list)):
        embed = discord.Embed(
            title="__Competence Of " + character.name + " with the weapon " + character.main_weapon.name + "__" ,
            description = ":u6307: `character board : `   " + "*character state :* `" + character.state[0] + "` , *for : * `" + str(sktr.getRestCooldownState(character)) + " cd`",
            color = discord.Colour.dark_green()
            )
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        if character.main_weapon.weapon_type.image_path == "https://cdn.discordapp.com/attachments/1005626886195527720/1005627343999610910/Inconnu.png" or character.main_weapon.weapon_type.image_path == "https://media.discordapp.net/attachments/1002657461842497597/1005621372438986903/Inconnu.png?width=225&height=225":
            embed.set_thumbnail(url=character.image_path)
        else:
            embed.set_thumbnail(url=character.main_weapon.weapon_type.image_path)
        if k == 0:
            embed.add_field(name="__**Weapon Skills | Main weapon skills : **__", value="```main weapon skills```", inline=False)
            for skill_name in character.competences.keys():
                if skill_name in character.main_weapon.weapon_type.competences:
                    embed.add_field(name="*" + skill_name + "*", value="*Lv : * `" + str(character.competences[skill_name].level)+ "`" + " *cd restant : * `" + str(sktr.getRestCooldown(character.competences[skill_name]))+ "`" + " *cd : * `" + str(character.competences[skill_name].competence_cooldown)+ "`" + " *state : * `" + str(character.competences[skill_name].state) + "`" + " *type : * `" + str(character.competences[skill_name].type) + "`", inline=True)
        embed.add_field(name="__**Charcater special Skills : **__", value="```character special skills```", inline=False)
        for skill_name in skill_list[k]:
            if skill_name not in character.main_weapon.weapon_type.competences:
                embed.add_field(name="*" + skill_name + "*", value="*Lv : * `" + str(character.competences[skill_name].level)+ "`" + " *cd restant : * `" + str(sktr.getRestCooldown(character.competences[skill_name]))+ "`" + " *cd : * `" + str(character.competences[skill_name].competence_cooldown)+ "`" + " *state : * `" + str(character.competences[skill_name].state) + "`" + " *type : * `" + str(character.competences[skill_name].type) + "`", inline=True)
        my_embed_list.append(embed)

    return my_embed_list
def getLiteEmbedCharacteristicRole(ctx ,results : tuple , characteristic : str , palier : int):
    if results[0] == True:
        embed = discord.Embed(
            title="__Resulte Of " + characteristic + "__" ,
            description = ":u6307: `dice roll result : `   " + "**the dice roll is a SUCCES**",
            color = discord.Colour.dark_green()
            )
    else:
        embed = discord.Embed(
            title="__Resulte Of " + characteristic + "__" ,
            description = ":u6307: `dice roll result : `   " + "**the dice roll is a FAIL**",
            color = discord.Colour.dark_green()
            )
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed.add_field(name=":fleur_de_lis: __The__ __Roll__ __Level__ `:`", value="` " + str(palier) + " `", inline=True)
    embed.add_field(name=":game_die: __The__ __Roll__ __Result__ `:`", value="` " + str(results[1]) + " `", inline=True)
    embed.set_thumbnail(url=ctx.author.avatar_url)
    embed.set_footer(text="mise a jour par: {}".format(ctx.author.display_name))
    return embed
def getPlayerArchitectureChar(character_dict : dict):
    txt_list = []
    space = " "
    for user_name in character_dict.keys():
        txt = "`-" + user_name +"` " +"\n"
        for user_display_name in character_dict[user_name].keys():
            txt = txt +  "`" + space*4  + "-" + user_display_name + "` " + "\n"
            for character_name in character_dict[user_name][user_display_name]:
                txt = txt + ":flower_playing_cards:" + "`" + space*9 + character_name + "` " + "\n"
        txt_list.append(txt)
    return txt_list
def getEmbedCharacterDict(ctx ,character_dict : dict):
    my_embed_list = []
    txt_list_list = getEncapsule(5,getPlayerArchitectureChar(character_dict))
    for txt_list in txt_list_list:
        embed = discord.Embed(
            title="__Characters__ __List__" ,
            description = ":u6307: `characters list : `",
            color = discord.Colour.default()
            )
        for txt in txt_list:
            embed.add_field(name="__characters__ __architecture__", value=txt, inline=False)
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.set_footer(text="mise a jour par : {}".format(ctx.author.display_name))
        my_embed_list.append(embed)
    return my_embed_list
def getEmbedStateCharacter(ctx , state_of_caster : str , state_of_target : str , caster_name : str , target_name : str):
    embed = discord.Embed(
        title="__Statistiques __Of__ __:__" ,
        description = ":u6307: `caster board |" + caster_name + "| : `  **" + state_of_caster + "** :flower_playing_cards: \n " + ":u6307: `target board |" + target_name + "| : `  **" + state_of_target + "** :flower_playing_cards:" ,
        color = discord.Colour.dark_green()
        )
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url=ctx.author.avatar_url)
    embed.set_footer(text="mise a jour par : {}".format(ctx.author.display_name))
    return embed
def getEmbedAttackRole(ctx ,results : tuple ,caster_name : str ,target_name : str ,caster,target,last_life):
    if results[0] == True:
        embed = discord.Embed(
            title="__Resulte__ __Of__ __The__ __Attack__" ,
            description = ":u6307: `dice roll result : `   " + "**the dice roll is a SUCCES**",
            color = discord.Colour.dark_green()
            )
    else:
        embed = discord.Embed(
            title="__Resulte__ __Of__ __The__ __Attack__" ,
            description = ":u6307: `dice roll result : `   " + "**the dice roll is a FAIL**",
            color = discord.Colour.dark_green()
            )
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

    
    embed.add_field(name=":fleur_de_lis: __The__ __Roll__ __Level__ `:`", value="` " + str(results[9]) + " `", inline=True)
    embed.add_field(name=":game_die: __The__ __Roll__ __Result__ `:`", value="` " + str(results[8]) + " `", inline=True)
    embed.add_field(name=":u6307: __The__ __Damage__ __Result__", value="` " + str(results[1]) + " `", inline=True)


    embed.add_field(name=":u6307: `| " + caster_name + " board |` , **state : ** `| " + caster.state[0] +" |`", value="``` strength : " + str(results[2]) + "\n dexterity : " + str(results[3]) + "\n bleeding : " +  str(results[4]) +"```", inline=True)
    embed.add_field(name=":u6307: `| " + target_name + " board |` , **state : ** `| " + target.state[0] +" |`", value="``` posture : " + str(results[5]) + "\n constitution : " + str(results[6]) + "\n evasion : " +  str(results[7]) +"```", inline=True)
    

    embed.add_field(name=":u6307: __The__ __Damage__ __Result__", value="`last hp : " + str(last_life) + "\n present hp : " + str(target.life) + " `", inline=False)

    
    embed.set_thumbnail(url=caster.image_path)
    embed.set_footer(text="mise a jour par : {}".format(ctx.author.display_name))
    return embed
def getEmbedAttacDescription(ctx,skill):
    embed = discord.Embed(
        title="__Description__ __Of__ __" + skill.name + "__" ,
        description = "`" + skill.presentation + "`" ,
        color = discord.Colour.dark_green()
        )
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed.set_footer(text="mise a jour par : {}".format(ctx.author.display_name))
    return embed
def getEmbedAttackBuff(ctx,skill,results):
    embed = discord.Embed(
        title="__Buff__ __List__ __Of__ __" + skill.name + "__" ,
        description = ":u6307: `attack board : `" ,
        color = discord.Colour.dark_green()
        )


    embed.add_field(name=":u6307: __The__ __Caster__ __Buffs__", value="``` strength : " + str(results[10]["strength"]) + "\n dexterity : " + str(results[10]["dexterity"]) + "\n bleeding : " +  str(results[10]["bleeding"]) +"```", inline=True)
    embed.add_field(name=":u6307: __The__ __Target__ __Buffs__", value="``` posture : " + str(results[10]["posture"]) + "\n constitution : " + str(results[10]["constitution"]) + "\n evasion : " +  str(results[10]["evasion"]) +"```", inline=True)

    
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed.set_footer(text="mise a jour par : {}".format(ctx.author.display_name))
    return embed
def getFirstEmbedImageCharacterCompetencesListWeapons(ctx ,character):
    skill_list = list(character.competences.keys())
    embed = discord.Embed(
        title="__Competence Of " + character.name + " with the weapon " + character.main_weapon.name + "__" ,
        description = ":u6307: `character board : `   " + "*character state :* `" + character.state[0] + "` , *for : * `" + str(sktr.getRestCooldownState(character)) + " cd`",
        color = discord.Colour.dark_green()
        )
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    if character.main_weapon.weapon_type.image_path == "https://cdn.discordapp.com/attachments/1005626886195527720/1005627343999610910/Inconnu.png" or character.main_weapon.weapon_type.image_path == "https://media.discordapp.net/attachments/1002657461842497597/1005621372438986903/Inconnu.png?width=225&height=225":
        embed.set_thumbnail(url=character.image_path)
    else:
        embed.set_thumbnail(url=character.main_weapon.weapon_type.image_path)
    embed.add_field(name="__**Weapon Skills | First weapon skills : **__", value="```first weapon skills```", inline=False)
    for skill_name in skill_list:
        if skill_name in character.weapon01.weapon_type.competences:
            embed.add_field(name="*" + skill_name + "*", value="*Lv : * `" + str(character.competences[skill_name].level)+ "`" + " *cd restant : * `" + str(sktr.getRestCooldown(character.competences[skill_name]))+ "`" + " *cd : * `" + str(character.competences[skill_name].competence_cooldown)+ "`" + " *state : * `" + str(character.competences[skill_name].state) + "`" + " *type : * `" + str(character.competences[skill_name].type) + "`", inline=True)
        pass
    embed.add_field(name="__**Weapon Skills | Second weapon skills : **__", value="```second weapon skills```", inline=False)
    for skill_name in skill_list:
        if skill_name in character.weapon02.weapon_type.competences:
            embed.add_field(name="*" + skill_name + "*", value="*Lv : * `" + str(character.competences[skill_name].level)+ "`" + " *cd restant : * `" + str(sktr.getRestCooldown(character.competences[skill_name]))+ "`" + " *cd : * `" + str(character.competences[skill_name].competence_cooldown)+ "`" + " *state : * `" + str(character.competences[skill_name].state) + "`" + " *type : * `" + str(character.competences[skill_name].type) + "`", inline=True)
        pass
    embed.add_field(name="__**Weapon Skills | Third weapon skills : **__", value="```third weapon skills```", inline=False)
    for skill_name in skill_list:
        if skill_name in character.weapon03.weapon_type.competences:
            embed.add_field(name="*" + skill_name + "*", value="*Lv : * `" + str(character.competences[skill_name].level)+ "`" + " *cd restant : * `" + str(sktr.getRestCooldown(character.competences[skill_name]))+ "`" + " *cd : * `" + str(character.competences[skill_name].competence_cooldown)+ "`" + " *state : * `" + str(character.competences[skill_name].state) + "`" + " *type : * `" + str(character.competences[skill_name].type) + "`", inline=True)
        pass
    embed.add_field(name="__**Accessory Skills | First accessory skills : **__", value="```first accessory skills```", inline=False)
    for skill_name in skill_list:
        if skill_name in character.accessorry01.accessory_type.competences:
            embed.add_field(name="*" + skill_name + "*", value="*Lv : * `" + str(character.competences[skill_name].level)+ "`" + " *cd restant : * `" + str(sktr.getRestCooldown(character.competences[skill_name]))+ "`" + " *cd : * `" + str(character.competences[skill_name].competence_cooldown)+ "`" + " *state : * `" + str(character.competences[skill_name].state) + "`" + " *type : * `" + str(character.competences[skill_name].type) + "`", inline=True)
        pass
    embed.add_field(name="__**Accessory Skills | Second accessory skills : **__", value="```second accessory skills```", inline=False)
    for skill_name in skill_list:
        if skill_name in character.accessorry02.accessory_type.competences:
            embed.add_field(name="*" + skill_name + "*", value="*Lv : * `" + str(character.competences[skill_name].level)+ "`" + " *cd restant : * `" + str(sktr.getRestCooldown(character.competences[skill_name]))+ "`" + " *cd : * `" + str(character.competences[skill_name].competence_cooldown)+ "`" + " *state : * `" + str(character.competences[skill_name].state) + "`" + " *type : * `" + str(character.competences[skill_name].type) + "`", inline=True)
        pass
    return embed
def getFirstEmbedImageCharacterCompetencesListRacesClasses(ctx ,character):
    skill_list = list(character.competences.keys())
    embed = discord.Embed(
        title="__Competence Of " + character.name + " with the weapon " + character.main_weapon.name + "__" ,
        description = ":u6307: `character board : `   " + "*character state :* `" + character.state[0] + "` , *for : * `" + str(sktr.getRestCooldownState(character)) + " cd`",
        color = discord.Colour.dark_green()
        )
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    if character.main_weapon.weapon_type.image_path == "https://cdn.discordapp.com/attachments/1005626886195527720/1005627343999610910/Inconnu.png" or character.main_weapon.weapon_type.image_path =="https://media.discordapp.net/attachments/1002657461842497597/1005621372438986903/Inconnu.png?width=225&height=225":
        embed.set_thumbnail(url=character.image_path)
    else:
        embed.set_thumbnail(url=character.main_weapon.weapon_type.image_path)
    embed.add_field(name="__**Charcater race Skills : **__", value="```character race skills```", inline=False)
    for skill_name in skill_list:
        if skill_name in character.race.competences:
            embed.add_field(name="*" + skill_name + "*", value="*Lv : * `" + str(character.competences[skill_name].level)+ "`" + " *cd restant : * `" + str(sktr.getRestCooldown(character.competences[skill_name]))+ "`" + " *cd : * `" + str(character.competences[skill_name].competence_cooldown)+ "`" + " *state : * `" + str(character.competences[skill_name].state) + "`" + " *type : * `" + str(character.competences[skill_name].type) + "`", inline=True)
        pass
    embed.add_field(name="__**Charcater class Skills : **__", value="```character class skills```", inline=False)
    for skill_name in skill_list:
        if skill_name in character.classe.competences:
            embed.add_field(name="*" + skill_name + "*", value="*Lv : * `" + str(character.competences[skill_name].level)+ "`" + " *cd restant : * `" + str(sktr.getRestCooldown(character.competences[skill_name]))+ "`" + " *cd : * `" + str(character.competences[skill_name].competence_cooldown)+ "`" + " *state : * `" + str(character.competences[skill_name].state) + "`" + " *type : * `" + str(character.competences[skill_name].type) + "`", inline=True)
        pass
    return embed
