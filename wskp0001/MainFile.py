"""
Main Class File
"""
import discord
from discord.ext import commands
import random
from discord.ext import commands
from discord_slash import ButtonStyle , SlashCommand
from discord_slash.utils.manage_components import *
import os
import TypographieFile as tf
import RpClassFile as rp
import StorageFile as st
import string
import random as rd
import copy
import SkillsTreatmentFile as sktr
nonetxt = "᲼"


class NotTheLolaBot():
        def __init__(self):
                self.bot = commands.Bot(command_prefix = "°", description = "Ceci n'est pas le lolabot , toute ressemblance avec le lolabot est purement fortuite")
                self.slash = SlashCommand(self.bot, sync_commands=True)
notlolabot = NotTheLolaBot()
@notlolabot.bot.event
async def on_ready():
	print("NotLolaBot online")
	await notlolabot.bot.change_presence(activity=discord.Game(name="°help"))







@notlolabot.bot.command()
async def test1(ctx, user:discord.Member ,*txt):
        """partager la sainte parole du non lola bot en mp"""
        def check(m):
                return m.author_id == ctx.author.id and m.origin_message.id == fait_choix.id
        def checkMessage(message):
                return message.author == ctx.message.author
        mess = await ctx.channel.history(limit = 1).flatten()
        await mess[0].delete()
        await user.send(" ".join(txt))
        while True:
                message_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                recieve_message = str(message_input.content)
                await user.send(recieve_message)
@notlolabot.bot.command()
async def say(ctx, *txt):
        """partager la sainte parole du non lola bot"""
        mess = await ctx.channel.history(limit = 1).flatten()
        await mess[0].delete()
        await ctx.send(" ".join(txt))
@notlolabot.bot.command()
async def getdice(ctx):
        """getdice command for dice role"""
        def check(m):
                return m.author_id == ctx.author.id and m.origin_message.id == fait_choix.id
        def checkMessage(message):
                return message.author == ctx.message.author and ctx.message.channel == message.channel
        await ctx.send("`__enter the dice type__` *(exemple : 10 , 2 , 100)*")
        try:
                dice_type_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                dice_type = int(str(dice_type_input.content))
                await ctx.send("__dice type : __**" + str(dice_type) + "**")
        except:
                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                dice_type = 100
        my_buttons = [create_button(style=ButtonStyle.blue,
                                    label="lancer le dé de : " + str(dice_type),
                                    custom_id="dice")]
        button_raw = create_actionrow(*my_buttons)
        fait_choix = await ctx.send("`Push the result : `", components=[button_raw])
        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
        if button_ctx.custom_id == "dice":
                await button_ctx.edit_origin(content=nonetxt)
                result = rd.randint(0,dice_type)
                await ctx.send(":game_die: `the result of the " + str(dice_type) + " dice`  *is : * " + str(result))
@notlolabot.bot.command()
async def register(ctx):
        """register command for classes , races , competences , enchances , weapons , armor , accessory , organisation , lore-information , characters , mass-entity"""
        def check(m):
                return m.author_id == ctx.author.id and m.origin_message.id == fait_choix.id
        def checkMessage(message):
                return message.author == ctx.message.author and ctx.message.channel == message.channel

        
        Selection_List = ["competence","enchance","item","lore informations","organisation","equipement_type","race","classe","character","archetype"]

        
        register_type_select = tf.getListSelection(ctx,"chose the register",Selection_List,Selection_List) 
        fait_choix = await ctx.send("`Chose the register : `", components=[create_actionrow(register_type_select)])
        register_type = await wait_for_component(notlolabot.bot, components=register_type_select, check=check)
        if register_type.values[0] == "competence":
                await register_type.send("`__enter the name of the skill__`")
                try:
                        competence_name_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                        competence_name = str(competence_name_input.content)
                        await ctx.send("__skill name : __`" + competence_name + "`")
                except:
                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                        competence_name = "none"
                competence_type_select_01 = tf.getListSelection(ctx,"chose the skill type",["competence d'arme","competence d'arme a une main","attaque normale","attaque transversale(attaque et skill)","mouvement","competence normale","competence de support","rituel","capacité passive","transformation"],["weapon_attack","one hand weapon_attack","normal_attack","transversal_attack","mouvement_skill","util_skill","massiv_skill","ritual_skill","capacity","transformation"])
                fait_choix = await register_type.send("`Chose the skill type : `", components=[create_actionrow(competence_type_select_01)])
                competence_type_aux_01 = await wait_for_component(notlolabot.bot, components=competence_type_select_01, check=check)
                if competence_type_aux_01.values[0] == "massiv_skill":
                        competence_type = (competence_type_aux_01.values[0],"buff")
                if competence_type_aux_01.values[0] == "transformation":
                        competence_type = (competence_type_aux_01.values[0],"self_buff")
                elif competence_type_aux_01.values[0] == "mouvement_skill" or competence_type_aux_01.values[0] == "ritual_skill":
                        competence_type = (competence_type_aux_01.values[0],"normal")
                elif competence_type_aux_01.values[0] == "weapon_attack" or competence_type_aux_01.values[0] == "normal_attack" or competence_type_aux_01.values[0] == "one hand weapon_attack" or competence_type_aux_01.values[0] == "transversal_attack":
                        competence_type_select_02 = tf.getListSelection(ctx,"chose the if the skill have a buff",["self buff","buff for the target","no buff"],["self_buff","buff","normal"])
                        fait_choix = await competence_type_aux_01.send("`chose the if the skill have a buff : `", components=[create_actionrow(competence_type_select_02)])
                        competence_type_aux_02 = await wait_for_component(notlolabot.bot, components=competence_type_select_02, check=check)
                        competence_type = (competence_type_aux_01.values[0],competence_type_aux_02.values[0])
                        await competence_type_aux_02.send(nonetxt)
                elif competence_type_aux_01.values[0] == "util_skill":
                        competence_type_select_02 = tf.getListSelection(ctx,"chose the if the skill have a buff",["self buff","no buff"],["self_buff","normal"])
                        fait_choix = await competence_type_aux_01.send("`chose the if the skill have a buff : `", components=[create_actionrow(competence_type_select_02)])
                        competence_type_aux_02 = await wait_for_component(notlolabot.bot, components=competence_type_select_02, check=check)
                        competence_type = (competence_type_aux_01.values[0],competence_type_aux_02.values[0])
                        await competence_type_aux_02.send(nonetxt)
                elif competence_type_aux_01.values[0] == "capacity":
                        competence_type = "no buff"
                competence_level_select = tf.getListSelection(ctx,"chose the level of the skill",[str(x) for x in range(0,21)],[str(x) for x in range(0,21)])
                fait_choix = await competence_type_aux_01.send("`chose the level of the skill : `", components=[create_actionrow(competence_level_select)])
                competence_level_aux = await wait_for_component(notlolabot.bot, components=competence_level_select, check=check)
                competence_level = int(competence_level_aux.values[0])               
                await competence_level_aux.send("`__enter the description of the skill__`")
                try:
                        competence_description_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                        competence_descrition = str(competence_description_input.content)
                        await ctx.send("`description register`")
                except:
                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                        competence_descrition = "none"
                if competence_type_aux_01.values[0] == "mouvement_skill":
                        competence_state_01 = "iframe"
                elif competence_type_aux_01.values[0] == "capacity":
                        competence_state_01 = "normal"
                elif competence_type_aux_01.values[0] == "transformation":
                        competence_state_select_01 = tf.getListSelection(ctx,"chose the state of the skill",["block","normal"],["block","normal"])
                        fait_choix = await competence_level_aux.send("`chose the state of the skill : `", components=[create_actionrow(competence_state_select_01)])
                        competence_state_aux_01 = await wait_for_component(notlolabot.bot, components=competence_state_select_01, check=check)
                        competence_state_01 = competence_state_aux_01.values[0]
                        await competence_state_aux_01.send(nonetxt)
                else:
                        competence_state_select_01 = tf.getListSelection(ctx,"chose the state of the skill",["block","iframe","normal"],["block","iframe","normal"])
                        fait_choix = await competence_level_aux.send("`chose the state of the skill : `", components=[create_actionrow(competence_state_select_01)])
                        competence_state_aux_01 = await wait_for_component(notlolabot.bot, components=competence_state_select_01, check=check)
                        competence_state_01 = competence_state_aux_01.values[0]
                        await competence_state_aux_01.send(nonetxt)

                        
                if competence_type_aux_01.values[0] == "ritual_skill":
                        competence_state_select_02 = tf.getListSelection(ctx,"chose the duration of the state",[str(x) for x in range(21)],[str(x) for x in range(21)])
                        fait_choix = await competence_level_aux.send("`chose the duration of the state : `", components=[create_actionrow(competence_state_select_02)])
                        competence_state_aux_02 = await wait_for_component(notlolabot.bot, components=competence_state_select_02, check=check)
                        competence_state = (competence_state_01,int(competence_state_aux_02.values[0]))
                elif competence_type_aux_01.values[0] == "capacity":
                        competence_state = ("normal",0)
                elif competence_type_aux_01.values[0] == "transformation":
                        competence_state_select_02 = tf.getListSelection(ctx,"chose the duration of the state",[str(x) for x in range(21)],[str(x) for x in range(21)])
                        fait_choix = await competence_level_aux.send("`chose the duration of the state : `", components=[create_actionrow(competence_state_select_02)])
                        competence_state_aux_02 = await wait_for_component(notlolabot.bot, components=competence_state_select_02, check=check)
                        competence_state = (competence_state_01,int(competence_state_aux_02.values[0]))
                else:
                        competence_state_select_02 = tf.getListSelection(ctx,"chose the duration of the state",[str(x) for x in range(7)],[str(x) for x in range(7)])
                        fait_choix = await competence_level_aux.send("`chose the duration of the state : `", components=[create_actionrow(competence_state_select_02)])
                        competence_state_aux_02 = await wait_for_component(notlolabot.bot, components=competence_state_select_02, check=check)
                        competence_state = (competence_state_01,int(competence_state_aux_02.values[0]))





                if competence_type_aux_01.values[0] in ["ritual_skill","transformation"]:
                        competence_cooldown_select = tf.getListSelection(ctx,"chose the duration of the cooldown",[str(x) for x in range(20,41)],[str(x) for x in range(20,41)])
                        fait_choix = await competence_state_aux_02.send("`chose the duration of the cooldown : `", components=[create_actionrow(competence_cooldown_select)])
                        competence_cooldown_aux = await wait_for_component(notlolabot.bot, components=competence_cooldown_select, check=check)
                        competence_cooldown = int(competence_cooldown_aux.values[0])
                elif competence_type_aux_01.values[0] in ["capacity"]:
                        competence_cooldown = 0
                else:
                        competence_cooldown_select = tf.getListSelection(ctx,"chose the duration of the cooldown",[str(x) for x in range(21)],[str(x) for x in range(21)])
                        fait_choix = await competence_state_aux_02.send("`chose the duration of the cooldown : `", components=[create_actionrow(competence_cooldown_select)])
                        competence_cooldown_aux = await wait_for_component(notlolabot.bot, components=competence_cooldown_select, check=check)
                        competence_cooldown = int(competence_cooldown_aux.values[0])
                
                self_buffs_constructor = {"strength" : (0,0),"dexterity" : (0,0),"bleeding" : (0,0) ,"posture" : (0,0) ,
                                          "constitution" : (0,0),"evasion" : (0,0),
                                          "intellect" : (0,0),"charisma" : (0,0) ,"wisdom" : (0,0)}
                buffs_constructor = {"strength" : (0,0),"dexterity" : (0,0),"bleeding" : (0,0) ,"posture" : (0,0) ,
                                     "constitution" : (0,0),"evasion" : (0,0),
                                     "intellect" : (0,0),"charisma" : (0,0) ,"wisdom" : (0,0)}
                attack_template_constructor = {"strength" : (0,0),"dexterity" : (0,0),"bleeding" : (0,0) ,"posture" : (0,0) ,
                                               "constitution" : (0,0),"evasion" : (0,0),
                                               "intellect" : (0,0),"charisma" : (0,0) ,"wisdom" : (0,0)}
                if competence_type[1] == "self_buff":
                        await competence_cooldown_aux.send("`__enter the self buff statistiques__`")
                        await competence_cooldown_aux.send("`strength-dice,strength|dexterity-dice,dexterity|posture-dice,posture|bleeding-dice,bleeding|constitution-dice,constitution|evasion-dice,evasion|intellect-dice,intellect|charisma-dice,charisma|wisdom-dice,wisdom`")
                        try:
                                self_buff_statistics_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                self_buff_statistics = str(self_buff_statistics_input.content)
                                self_statistics_list = self_buff_statistics.split("|")
                                await ctx.send("`description register`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                        self_buffs_constructor = {"strength" : tuple([int(x) for x in self_statistics_list[0].split(",")]),
                                                "dexterity" : tuple([int(x) for x in self_statistics_list[1].split(",")]),
                                                "bleeding" : tuple([int(x) for x in self_statistics_list[2].split(",")]) ,
                                                "posture" : tuple([int(x) for x in self_statistics_list[3].split(",")]) ,
                                                "constitution" : tuple([int(x) for x in self_statistics_list[4].split(",")]),
                                                "evasion" : tuple([int(x) for x in self_statistics_list[5].split(",")]),
                                                "intellect" : tuple([int(x) for x in self_statistics_list[6].split(",")]),
                                                "charisma" : tuple([int(x) for x in self_statistics_list[7].split(",")]),
                                                "wisdom" : tuple([int(x) for x in self_statistics_list[8].split(",")])}
                        pass
                if competence_type[1] == "buff":
                        await competence_cooldown_aux.send("`__enter the buff statistiques__`")
                        await competence_cooldown_aux.send("`strength-dice,strength|dexterity-dice,dexterity|bleeding-dice,bleeding|posture-dice,posture|constitution-dice,constitution|evasion-dice,evasion|intellect-dice,intellect|charisma-dice,charisma|wisdom-dice,wisdom`")
                        try:
                                buff_statistics_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                buff_statistics = str(buff_statistics_input.content)
                                statistics_list = buff_statistics.split("|")
                                await ctx.send("`description register`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                        buffs_constructor = {"strength" : tuple([int(x) for x in statistics_list[0].split(",")]),
                                                "dexterity" : tuple([int(x) for x in statistics_list[1].split(",")]),
                                                "bleeding" : tuple([int(x) for x in statistics_list[2].split(",")]) ,
                                                "posture" : tuple([int(x) for x in statistics_list[3].split(",")]) ,
                                                "constitution" : tuple([int(x) for x in statistics_list[4].split(",")]),
                                                "evasion" : tuple([int(x) for x in statistics_list[5].split(",")]),
                                                "intellect" : tuple([int(x) for x in statistics_list[6].split(",")]),
                                                "charisma" : tuple([int(x) for x in statistics_list[7].split(",")]),
                                                "wisdom" : tuple([int(x) for x in statistics_list[8].split(",")])}
                        pass
                if competence_type_aux_01.values[0] == "weapon_attack" or competence_type_aux_01.values[0] == "normal_attack" or competence_type_aux_01.values[0] == "one hand weapon_attack" or competence_type_aux_01.values[0] == "transversal_attack":
                        attack_dice_select = tf.getListSelection(ctx,"chose the damage dice of the skill",[str(x) for x in range(21)],[str(x) for x in range(21)])
                        fait_choix = await competence_cooldown_aux.send("`chose the damage dice of the skill : `", components=[create_actionrow(attack_dice_select)])
                        attack_dice_aux = await wait_for_component(notlolabot.bot, components=attack_dice_select, check=check)
                        attack_constent_select = tf.getListSelection(ctx,"chose the damage of the skill",[str(x) for x in range(11)],[str(x) for x in range(11)])
                        fait_choix = await attack_dice_aux.send("`chose the damage of the skill : `", components=[create_actionrow(attack_constent_select)])
                        attack_constent_aux = await wait_for_component(notlolabot.bot, components=attack_constent_select, check=check)
                        dexterity_dice_select = tf.getListSelection(ctx,"chose the dexterity dice of the skill",[str(x) for x in range(21)],[str(x) for x in range(21)])
                        fait_choix = await attack_constent_aux.send("`chose the dexterity dice of the skill : `", components=[create_actionrow(dexterity_dice_select)])
                        dexterity_dice_aux = await wait_for_component(notlolabot.bot, components=dexterity_dice_select, check=check)
                        dexterity_constent_select = tf.getListSelection(ctx,"chose the dexterity of the skill",[str(x) for x in range(19)],[str(x) for x in range(19)])
                        fait_choix = await dexterity_dice_aux.send("`chose the dexterity of the skill : `", components=[create_actionrow(dexterity_constent_select)])
                        dexterity_constent_aux = await wait_for_component(notlolabot.bot, components=dexterity_constent_select, check=check)
                        bleeding_dice_select = tf.getListSelection(ctx,"chose the bleeding dice of the skill",[str(x) for x in range(14)],[str(x) for x in range(14)])
                        fait_choix = await dexterity_constent_aux.send("`chose the bleeding dice of the skill : `", components=[create_actionrow(bleeding_dice_select)])
                        bleeding_dice_aux = await wait_for_component(notlolabot.bot, components=bleeding_dice_select, check=check)
                        bleeding_constent_select = tf.getListSelection(ctx,"chose the bleeding of the skill",[str(x) for x in range(11)],[str(x) for x in range(11)])
                        fait_choix = await bleeding_dice_aux.send("`chose the bleeding of the skill : `", components=[create_actionrow(bleeding_constent_select)])
                        bleeding_constent_aux = await wait_for_component(notlolabot.bot, components=bleeding_constent_select, check=check)
                        posture_dice_select = tf.getListSelection(ctx,"chose the posture dice of the skill",[str(x) for x in range(21)],[str(x) for x in range(21)])
                        fait_choix = await bleeding_constent_aux.send("`chose the posture dice of the skill : `", components=[create_actionrow(posture_dice_select)])
                        posture_dice_aux = await wait_for_component(notlolabot.bot, components=posture_dice_select, check=check)
                        posture_constent_select = tf.getListSelection(ctx,"chose the posture of the skill",[str(x) for x in range(11)],[str(x) for x in range(11)])
                        fait_choix = await posture_dice_aux.send("`chose the posture of the skill : `", components=[create_actionrow(posture_constent_select)])
                        posture_constent_aux = await wait_for_component(notlolabot.bot, components=posture_constent_select, check=check)
                        await posture_constent_aux.send(nonetxt)
                        attack_template_constructor = {"strength" : (int(attack_dice_aux.values[0]),int(attack_constent_aux.values[0])),
                                    "dexterity" : (int(dexterity_dice_aux.values[0]),int(dexterity_constent_aux.values[0])),
                                    "bleeding" : (int(bleeding_dice_aux.values[0]),int(bleeding_constent_aux.values[0])) ,
                                    "posture" : (int(posture_dice_aux.values[0]),int(posture_constent_aux.values[0])) ,
                                    "constitution" : (0,0),"evasion" : (0,0),"intellect" : (0,0),"charisma" : (0,0) ,"wisdom" : (0,0)}
                if competence_type_aux_01.values[0] == "mouvement_skill":
                        await competence_cooldown_aux.send(nonetxt)
                if competence_type_aux_01.values[0] == "util_skill":
                        await competence_cooldown_aux.send(nonetxt)
                if competence_type_aux_01.values[0] == "ritual_skill":
                        await competence_cooldown_aux.send(nonetxt)
                if competence_type_aux_01.values[0] == "transformation":
                        await competence_cooldown_aux.send(nonetxt)
                new_competence = rp.CompetenceClass(competence_name,competence_descrition,competence_type,competence_cooldown,competence_state,competence_level,attack_template_constructor,rp.StatisticsClass("self_buff",self_buffs_constructor),rp.StatisticsClass("buff",buffs_constructor))
                st.saveCompetence(new_competence)
                display_competence = st.loadCompetence(new_competence.name)
                my_embed = tf.getEmbedImageCompetence(ctx,new_competence.name)
                tf.TypographyCompetenceInterface(ctx,display_competence,my_embed)
                await ctx.send(embed=my_embed)
                pass
        if register_type.values[0] == "enchance":
                enchance_type_select = tf.getListSelection(ctx,"chose the enchance type",["weapon_enchance","accessory_enchance","armor_enchance"],["weapon_enchance","accessory_enchance","armor_enchance"])
                fait_choix = await register_type.send("`Chose the the enchance type : `", components=[create_actionrow(enchance_type_select)])
                enchance_type = await wait_for_component(notlolabot.bot, components=enchance_type_select, check=check)
                await enchance_type.send("`__enter the name of the enchance__`")
                try:
                        enchance_name_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                        enchance_name = str(enchance_name_input.content)
                        await ctx.send("__skill name : __`" + enchance_name + "`")
                except:
                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                        enchance_name = "none"

                my_buttons = [create_button(style=ButtonStyle.green,
                                            label="use a CSV File for the register",
                                            custom_id="csv"),
                              create_button(style=ButtonStyle.green,
                                            label="Dont use a CSV File for the register",
                                            custom_id="not csv")]
                button_raw = create_actionrow(*my_buttons)
                fait_choix = await ctx.send("`Push the register : `", components=[button_raw])
                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                if button_ctx.custom_id == "csv":
                        await button_ctx.edit_origin(content=nonetxt)
                        new_enchance = []
                        await register_type.send("`__enter the csv file of the enchance__`")
                        try:
                                lore_description_input = await notlolabot.bot.wait_for("message", timeout = 800, check=checkMessage)
                                if lore_description_input.attachments != [] and lore_description_input.attachments[0].filename.endswith(".csv"):
                                        await lore_description_input.attachments[0].save(r"files_saves\file_" + lore_description_input.attachments[0].filename)
                                        enchance_stats_dict = st.cvsEnchanceInterpretor(r"files_saves\file_" + lore_description_input.attachments[0].filename)
                                else:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        enchance_stats_dict = st.cvsEnchanceInterpretor("rsc\Basic-Pattern-Enchance-CSV.csv")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                enchance_stats_dict = st.cvsEnchanceInterpretor("rsc\Basic-Pattern-Enchance-CSV.csv")
                        for i in range(len(enchance_stats_dict)):
                                new_enchance.append(rp.StatisticsClass("enchance level " + str(i),enchance_stats_dict[i]))
                if button_ctx.custom_id == "not csv":
                        await button_ctx.edit_origin(content=nonetxt)
                        if enchance_type.values[0] == "weapon_enchance":
                                new_enchance = []
                                for i in range(10):
                                        await register_type.send("`__enter the statistics of the enchance level " + str(i) + "__`")
                                        await register_type.send("`strength-dice,strength|dexterity-dice,dexterity|bleeding-dice,bleeding|posture-dice,posture`")
                                        try:
                                                enchance_statistics_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                                enchance_statistics = str(enchance_statistics_input.content).split("|")
                                        except:
                                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        constructor = {"strength" : tuple([int(x) for x in enchance_statistics[0].split(",")]),
                                                       "dexterity" : tuple([int(x) for x in enchance_statistics[1].split(",")]),
                                                       "bleeding" : tuple([int(x) for x in enchance_statistics[2].split(",")]) ,
                                                       "posture" : tuple([int(x) for x in enchance_statistics[3].split(",")]) ,
                                                       "constitution" : (0,0),"evasion" : (0,0),"intellect" : (0,0),"charisma" : (0,0),"wisdom" : (0,0)}
                                        new_enchance.append(rp.StatisticsClass("enchance level " + str(i),constructor))
                                pass
                        if enchance_type.values[0] == "accessory_enchance":
                                new_enchance = []
                                for i in range(10):
                                        await register_type.send("`__enter the statistics of the enchance level " + str(i) + "__`")
                                        await register_type.send("`strength-dice,strength|dexterity-dice,dexterity|bleeding-dice,bleeding|posture-dice,posture|constitution-dice,constitution|evasion-dice,evasion|intellect-dice,intellect|charisma-dice,charisma|wisdom-dice,wisdom`")
                                        try:
                                                enchance_statistics_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                                enchance_statistics = str(enchance_statistics_input.content).split(" ")
                                        except:
                                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        constructor = {"strength" : tuple([int(x) for x in enchance_statistics[0].split(",")]),
                                                       "dexterity" : tuple([int(x) for x in enchance_statistics[1].split(",")]),
                                                       "bleeding" : tuple([int(x) for x in enchance_statistics[2].split(",")]) ,
                                                       "posture" : tuple([int(x) for x in enchance_statistics[3].split(",")]) ,
                                                       "constitution" : tuple([int(x) for x in enchance_statistics[4].split(",")]),
                                                       "evasion" : tuple([int(x) for x in enchance_statistics[5].split(",")]),
                                                       "intellect" : tuple([int(x) for x in enchance_statistics[6].split(",")]),
                                                       "charisma" : tuple([int(x) for x in enchance_statistics[7].split(",")]),
                                                       "wisdom" : tuple([int(x) for x in enchance_statistics[8].split(",")])}
                                        new_enchance.append(rp.StatisticsClass("enchance level " + str(i),constructor))
                                pass
                        if enchance_type.values[0] == "armor_enchance":
                                new_enchance = []
                                for i in range(10):
                                        await register_type.send("`__enter the statistics of the enchance level " + str(i) + "__`")
                                        await register_type.send("`posture-dice,posture|constitution-dice,constitution|evasion-dice,evasion`")
                                        try:
                                                enchance_statistics_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                                enchance_statistics = str(enchance_statistics_input.content).split(" ")
                                        except:
                                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        constructor = {"strength" : (0,0),"dexterity" : (0,0),"bleeding" : (0,0),
                                                       "posture" : tuple([int(x) for x in enchance_statistics[0].split(",")]),
                                                       "constitution" : tuple([int(x) for x in enchance_statistics[1].split(",")]),
                                                       "evasion" : tuple([int(x) for x in enchance_statistics[2].split(",")]),
                                                       "intellect" : (0,0),"charisma" : (0,0),"wisdom" : (0,0)}                            
                                        new_enchance.append(rp.StatisticsClass("enchance level " + str(i),constructor))
                st.saveEnchance(new_enchance,enchance_name)
                display_enchance = st.loadEnchance(enchance_name)
                first_embed = tf.getFirstEmbedImageEnchance(ctx,enchance_name,display_enchance)
                await ctx.send(embed=first_embed)                
                my_buttons = [create_button(
                        style=ButtonStyle.blue,
                        label="display the evolution",
                        custom_id="display")]
                button_raw = create_actionrow(*my_buttons)
                fait_choix = await ctx.send("`Push for display the evolution : `", components=[button_raw])
                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                if button_ctx.custom_id == "display":
                        await button_ctx.edit_origin(content=nonetxt)
                        my_embed_list = tf.getTheEmbedEnchance(ctx,display_enchance)
                        for x in my_embed_list:
                                await ctx.send(file=x[1], embed=x[0])                         
                pass
        if register_type.values[0] == "organisation":
                await register_type.send("`__enter the name of the organisation__`")
                try:
                        organisation_name_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                        organisation_name = str(organisation_name_input.content)
                        await ctx.send("__organisation name : __ `" + organisation_name + "`")
                except:
                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                        organisation_name = "none"
                await register_type.send("`__enter the description of the organisation__`")
                try:
                        organisation_description_input = await notlolabot.bot.wait_for("message", timeout = 800, check=checkMessage)
                        organisation_description = str(organisation_description_input.content)
                except:
                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                        organisation_description = nonetxt
                await register_type.send("`__enter the image url of the organisation__`")
                try:
                        organisation_image_path_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                        organisation_image_path = str(organisation_image_path_input.content)
                except:
                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                        organisation_image_path = "https://cdn.discordapp.com/attachments/1005626886195527720/1005627343999610910/Inconnu.png"
                await register_type.send("`__enter the capital of the organisation in gold pieces__`")
                try:
                        organisation_capital_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                        organisation_capital = int(str(organisation_capital_input.content))
                except:
                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                        organisation_capital = 0
                await register_type.send("`__enter the max hp value of the organisation__`")
                try:
                        organisation_max_hp_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                        organisation_max_hp = int(str(organisation_max_hp_input.content))
                except:
                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                        organisation_max_hp = 0
                attack_dice_select = tf.getListSelection(ctx,"chose the bonus damage dice of the organisation",[str(x) for x in range(7)],[str(x) for x in range(7)])
                fait_choix = await register_type.send("`chose the bonus damage dice of the organisation : `", components=[create_actionrow(attack_dice_select)])
                attack_dice_aux = await wait_for_component(notlolabot.bot, components=attack_dice_select, check=check)
                attack_constent_select = tf.getListSelection(ctx,"chose the damage bonus of the organisation",[str(x) for x in range(5)],[str(x) for x in range(5)])
                fait_choix = await attack_dice_aux.send("`chose the damage bonus of the organisation : `", components=[create_actionrow(attack_constent_select)])
                attack_constent_aux = await wait_for_component(notlolabot.bot, components=attack_constent_select, check=check)
                dexterity_dice_select = tf.getListSelection(ctx,"chose the bonus dexterity dice of the organisation",[str(x) for x in range(7)],[str(x) for x in range(7)])
                fait_choix = await attack_constent_aux.send("`chose the bonus dexterity dice of the organisation : `", components=[create_actionrow(dexterity_dice_select)])
                dexterity_dice_aux = await wait_for_component(notlolabot.bot, components=dexterity_dice_select, check=check)
                dexterity_constent_select = tf.getListSelection(ctx,"chose the dexterity bonus of the organisation",[str(x) for x in range(5)],[str(x) for x in range(5)])
                fait_choix = await dexterity_dice_aux.send("`chose the dexterity bonus of the organisation : `", components=[create_actionrow(dexterity_constent_select)])
                dexterity_constent_aux = await wait_for_component(notlolabot.bot, components=dexterity_constent_select, check=check)
                bleeding_dice_select = tf.getListSelection(ctx,"chose the bonus bleeding dice of the organisation",[str(x) for x in range(7)],[str(x) for x in range(7)])
                fait_choix = await dexterity_constent_aux.send("`chose the bonus bleeding dice of the organisation : `", components=[create_actionrow(bleeding_dice_select)])
                bleeding_dice_aux = await wait_for_component(notlolabot.bot, components=bleeding_dice_select, check=check)
                bleeding_constent_select = tf.getListSelection(ctx,"chose the bonus bleeding of the organisation",[str(x) for x in range(5)],[str(x) for x in range(5)])
                fait_choix = await bleeding_dice_aux.send("`chose the bonus bleeding of the organisation : `", components=[create_actionrow(bleeding_constent_select)])
                bleeding_constent_aux = await wait_for_component(notlolabot.bot, components=bleeding_constent_select, check=check)
                posture_dice_select = tf.getListSelection(ctx,"chose the bonus posture dice of the organisation",[str(x) for x in range(7)],[str(x) for x in range(7)])
                fait_choix = await bleeding_constent_aux.send("`chose the bonus posture dice of the organisation : `", components=[create_actionrow(posture_dice_select)])
                posture_dice_aux = await wait_for_component(notlolabot.bot, components=posture_dice_select, check=check)
                posture_constent_select = tf.getListSelection(ctx,"chose the posture bonus of the organisation",[str(x) for x in range(5)],[str(x) for x in range(5)])
                fait_choix = await posture_dice_aux.send("`chose the posture bonus of the organisation : `", components=[create_actionrow(posture_constent_select)])
                posture_constent_aux = await wait_for_component(notlolabot.bot, components=posture_constent_select, check=check)
                constitution_dice_select = tf.getListSelection(ctx,"chose the bonus constitution dice of the organisation",[str(x) for x in range(7)],[str(x) for x in range(7)])
                fait_choix = await posture_constent_aux.send("`chose the bonus constitution dice of the organisation : `", components=[create_actionrow(constitution_dice_select)])
                constitution_dice_aux = await wait_for_component(notlolabot.bot, components=constitution_dice_select, check=check)
                constitution_constent_select = tf.getListSelection(ctx,"chose the constitution bonus of the organisation",[str(x) for x in range(5)],[str(x) for x in range(5)])
                fait_choix = await constitution_dice_aux.send("`chose the constitution bonus of the organisation : `", components=[create_actionrow(constitution_constent_select)])
                constitution_constent_aux = await wait_for_component(notlolabot.bot, components=constitution_constent_select, check=check)
                evasion_dice_select = tf.getListSelection(ctx,"chose the bonus evasion dice of the organisation",[str(x) for x in range(7)],[str(x) for x in range(7)])
                fait_choix = await constitution_constent_aux.send("`chose the bonus evasion dice of the organisation : `", components=[create_actionrow(evasion_dice_select)])
                evasion_dice_aux = await wait_for_component(notlolabot.bot, components=evasion_dice_select, check=check)
                evasion_constent_select = tf.getListSelection(ctx,"chose the evasion bonus of the organisation",[str(x) for x in range(5)],[str(x) for x in range(5)])
                fait_choix = await evasion_dice_aux.send("`chose the evasion bonus of the organisation : `", components=[create_actionrow(evasion_constent_select)])
                evasion_constent_aux = await wait_for_component(notlolabot.bot, components=evasion_constent_select, check=check)
                intellect_dice_select = tf.getListSelection(ctx,"chose the bonus intellect dice of the organisation",[str(x) for x in range(7)],[str(x) for x in range(7)])
                fait_choix = await evasion_constent_aux.send("`chose the bonus intellect dice of the organisation : `", components=[create_actionrow(intellect_dice_select)])
                intellect_dice_aux = await wait_for_component(notlolabot.bot, components=intellect_dice_select, check=check)
                intellect_constent_select = tf.getListSelection(ctx,"chose the intellect bonus of the organisation",[str(x) for x in range(5)],[str(x) for x in range(5)])
                fait_choix = await intellect_dice_aux.send("`chose the intellect bonus of the organisation : `", components=[create_actionrow(intellect_constent_select)])
                intellect_constent_aux = await wait_for_component(notlolabot.bot, components=intellect_constent_select, check=check)
                charisma_dice_select = tf.getListSelection(ctx,"chose the bonus charisma dice of the organisation",[str(x) for x in range(7)],[str(x) for x in range(7)])
                fait_choix = await intellect_constent_aux.send("`chose the bonus charisma dice of the organisation : `", components=[create_actionrow(charisma_dice_select)])
                charisma_dice_aux = await wait_for_component(notlolabot.bot, components=charisma_dice_select, check=check)
                charisma_constent_select = tf.getListSelection(ctx,"chose the charisma bonus of the organisation",[str(x) for x in range(5)],[str(x) for x in range(5)])
                fait_choix = await charisma_dice_aux.send("`chose the charisma bonus of the organisation : `", components=[create_actionrow(charisma_constent_select)])
                charisma_constent_aux = await wait_for_component(notlolabot.bot, components=charisma_constent_select, check=check)
                wisdom_dice_select = tf.getListSelection(ctx,"chose the bonus wisdom dice of the organisation",[str(x) for x in range(7)],[str(x) for x in range(7)])
                fait_choix = await charisma_constent_aux.send("`chose the bonus wisdom dice of the organisation : `", components=[create_actionrow(wisdom_dice_select)])
                wisdom_dice_aux = await wait_for_component(notlolabot.bot, components=wisdom_dice_select, check=check)
                wisdom_constent_select = tf.getListSelection(ctx,"chose the wisdom bonus of the organisation",[str(x) for x in range(5)],[str(x) for x in range(5)])
                fait_choix = await wisdom_dice_aux.send("`chose the wisdom bonus of the organisation : `", components=[create_actionrow(wisdom_constent_select)])
                wisdom_constent_aux = await wait_for_component(notlolabot.bot, components=wisdom_constent_select, check=check)                
                await wisdom_constent_aux.send(nonetxt)
                attack_template_constructor = {"strength" : (int(attack_dice_aux.values[0]),int(attack_dice_aux.values[0])),
                                               "dexterity" : (int(dexterity_dice_aux.values[0]),int(dexterity_constent_aux.values[0])),
                                               "bleeding" : (int(bleeding_dice_aux.values[0]),int(bleeding_constent_aux.values[0])) ,
                                               "posture" : (int(posture_dice_aux.values[0]),int(posture_constent_aux.values[0])) ,
                                               "constitution" : (int(constitution_dice_aux.values[0]),int(constitution_constent_aux.values[0])),
                                               "evasion" : (int(evasion_dice_aux.values[0]),int(evasion_constent_aux.values[0])),
                                               "intellect" : (int(intellect_dice_aux.values[0]),int(intellect_constent_aux.values[0])),
                                               "charisma" : (int(charisma_dice_aux.values[0]),int(charisma_constent_aux.values[0])) ,
                                               "wisdom" : (int(wisdom_dice_aux.values[0]),int(wisdom_constent_aux.values[0]))}
                new_organisation = rp.OrganisationClass(organisation_name,organisation_description,organisation_max_hp,organisation_capital,rp.StatisticsClass("",attack_template_constructor),organisation_image_path)
                st.saveOrganisation(new_organisation)
                display_organisation = st.loadOrganisation(organisation_name)
                my_embed = tf.getEmbedImageOrganisation(ctx,display_organisation)
                await ctx.send(embed=my_embed)
        if register_type.values[0] == "lore informations":
                await register_type.send("`__enter the title of the lore information__`")
                try:
                        lore_name_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                        lore_name = str(lore_name_input.content)
                        await ctx.send("__lore name : __ `" + lore_name + "`")
                except:
                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                        lore_name = "none"
                await register_type.send("`__enter the description of the lore information__`")
                try:
                        lore_description_input = await notlolabot.bot.wait_for("message", timeout = 800, check=checkMessage)
                        if lore_description_input.attachments != [] and lore_description_input.attachments[0].filename.endswith(".txt"):
                                await lore_description_input.attachments[0].save(r"files_saves\file_" + lore_description_input.attachments[0].filename)
                                file = open(r"files_saves\file_" + lore_description_input.attachments[0].filename,"r")
                                lore_description = file.read()
                                file.close()
                        else:
                                lore_description = str(lore_description_input.content)
                except:
                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                        lore_description = nonetxt
                await register_type.send("`__enter the image url of the lore information__`")
                try:
                        lore_image_path_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                        lore_image_path = str(lore_image_path_input.content)
                except:
                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                        lore_image_path = "https://cdn.discordapp.com/attachments/1005626886195527720/1005627343999610910/Inconnu.png"
                st.saveLore(rp.LoreClass(lore_name,lore_description,lore_image_path))
                lore_display = st.loadLore(lore_name)
                embed_list = tf.getListEmbedImageLore(ctx,lore_display)
                for my_embed in embed_list:
                        await ctx.send(embed=my_embed)
                pass
        if register_type.values[0] == "equipement_type":
                await register_type.send("`__enter the name of the equipement-type__`")
                try:
                        equipement_type_name_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                        equipement_type_name = str(equipement_type_name_input.content)
                        await ctx.send("__equipement-type name : __ `" + equipement_type_name + "`")
                except:
                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                        equipement_type_name = "none"
                await register_type.send("`__enter the description of the equipement-type(not too long)__`")
                try:
                        equipement_type_description_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                        equipement_type_description = str(equipement_type_description_input.content)
                        await ctx.send("__equipement-type description : __ `" + equipement_type_name + "`")
                except:
                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                        equipement_type_description = "none"
                await register_type.send("`__enter the image url of the equipement-type__`")
                try:
                        equipement_type_image_path_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                        equipement_type_image_path = str(equipement_type_image_path_input.content)
                except:
                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                        equipement_type_image_path = "https://cdn.discordapp.com/attachments/1005626886195527720/1005627343999610910/Inconnu.png"                      
                equipement_type_select = tf.getListSelection(ctx,"chose the equipement type",["weapon type","accessory type","armor type"],["weapon_type","accessory_type","armor_type"])
                fait_choix = await register_type.send("`chose the equipement type : `", components=[create_actionrow(equipement_type_select)])
                equipement_type_aux = await wait_for_component(notlolabot.bot, components=equipement_type_select, check=check)
                if equipement_type_aux.values[0] == "weapon_type":
                        modifier_select = tf.getListSelection(ctx,"chose the modifier of the weapon ",["strength","dexterity","bleeding","posture","constitution","evasion","intellect","charisma","wisdom"],["strength","dexterity","bleeding","posture","constitution","evasion","intellect","charisma","wisdom"])
                        fait_choix = await equipement_type_aux.send("`chose the modifier of the weapon : `", components=[create_actionrow(modifier_select)])
                        modifier_select_aux = await wait_for_component(notlolabot.bot, components=modifier_select, check=check)
                        modifier = modifier_select_aux.values[0]
                        attack_dice_select = tf.getListSelection(ctx,"chose the damage dice of the weapon",[str(x) for x in range(15)],[str(x) for x in range(15)])
                        fait_choix = await modifier_select_aux.send("`chose the damage dice of the weapon : `", components=[create_actionrow(attack_dice_select)])
                        attack_dice_aux = await wait_for_component(notlolabot.bot, components=attack_dice_select, check=check)
                        attack_constent_select = tf.getListSelection(ctx,"chose the damage of the weapon",[str(x) for x in range(5)],[str(x) for x in range(5)])
                        fait_choix = await attack_dice_aux.send("`chose the damage of the weapon : `", components=[create_actionrow(attack_constent_select)])
                        attack_constent_aux = await wait_for_component(notlolabot.bot, components=attack_constent_select, check=check)
                        dexterity_dice_select = tf.getListSelection(ctx,"chose the dexterity dice of the weapon",[str(x) for x in range(15)],[str(x) for x in range(15)])
                        fait_choix = await attack_constent_aux.send("`chose the dexterity dice of the weapon : `", components=[create_actionrow(dexterity_dice_select)])
                        dexterity_dice_aux = await wait_for_component(notlolabot.bot, components=dexterity_dice_select, check=check)
                        dexterity_constent_select = tf.getListSelection(ctx,"chose the dexterity of the weapon",[str(x) for x in range(5)],[str(x) for x in range(5)])
                        fait_choix = await dexterity_dice_aux.send("`chose the dexterity of the weapon : `", components=[create_actionrow(dexterity_constent_select)])
                        dexterity_constent_aux = await wait_for_component(notlolabot.bot, components=dexterity_constent_select, check=check)
                        bleeding_dice_select = tf.getListSelection(ctx,"chose the bleeding dice of the weapon",[str(x) for x in range(15)],[str(x) for x in range(15)])
                        fait_choix = await dexterity_constent_aux.send("`chose the bleeding dice of the weapon : `", components=[create_actionrow(bleeding_dice_select)])
                        bleeding_dice_aux = await wait_for_component(notlolabot.bot, components=bleeding_dice_select, check=check)
                        bleeding_constent_select = tf.getListSelection(ctx,"chose the bleeding of the weapon",[str(x) for x in range(5)],[str(x) for x in range(5)])
                        fait_choix = await bleeding_dice_aux.send("`chose the bleeding of the weapon : `", components=[create_actionrow(bleeding_constent_select)])
                        bleeding_constent_aux = await wait_for_component(notlolabot.bot, components=bleeding_constent_select, check=check)
                        posture_dice_select = tf.getListSelection(ctx,"chose the posture dice of the weapon",[str(x) for x in range(15)],[str(x) for x in range(15)])
                        fait_choix = await bleeding_constent_aux.send("`chose the posture dice of the weapon : `", components=[create_actionrow(posture_dice_select)])
                        posture_dice_aux = await wait_for_component(notlolabot.bot, components=posture_dice_select, check=check)
                        posture_constent_select = tf.getListSelection(ctx,"chose the posture of the weapon",[str(x) for x in range(5)],[str(x) for x in range(5)])
                        fait_choix = await posture_dice_aux.send("`chose the posture of the weapon : `", components=[create_actionrow(posture_constent_select)])
                        posture_constent_aux = await wait_for_component(notlolabot.bot, components=posture_constent_select, check=check)               
                        await posture_constent_aux.send(nonetxt)
                        attack_template_constructor = {"strength" : (int(attack_dice_aux.values[0]),int(attack_dice_aux.values[0])),
                                                       "dexterity" : (int(dexterity_dice_aux.values[0]),int(dexterity_constent_aux.values[0])),
                                                       "bleeding" : (int(bleeding_dice_aux.values[0]),int(bleeding_constent_aux.values[0])) ,
                                                       "posture" : (int(posture_dice_aux.values[0]),int(posture_constent_aux.values[0])) ,
                                                       "constitution" : (0,0),"evasion" : (0,0),"intellect" : (0,0),"charisma" : (0,0) ,"wisdom" : (0,0)}  
                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                    label="display the skill list",
                                                    custom_id="display"),
                                      create_button(style=ButtonStyle.blue,
                                                    label="not display the skill list",
                                                    custom_id="not_display")]
                        button_raw = create_actionrow(*my_buttons)
                        fait_choix = await ctx.send("`Push for the skill list : `", components=[button_raw])
                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                        if button_ctx.custom_id == "display":
                                await button_ctx.edit_origin(content=nonetxt)
                                skill_list = st.filterCompetences(["weapon_attack","one hand weapon_attack"])
                                skill_embed_list = tf.getListEmbedSkillsList(ctx,skill_list,"weapon attack")
                                for skill_embed in skill_embed_list:
                                        await ctx.send(embed=skill_embed)
                                await ctx.send("`skill01`|`skill02`|`skill03`|`skill04`,`........`")
                                try:
                                        string_skill_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        string_skill = str(string_skill_input.content)
                                        await ctx.send("__skill list : __ `" + string_skill + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        string_skill = "none"
                                skill_names_list = string_skill.split("|")
                                skill_dict = {}
                                if skill_names_list == ["none"]:
                                        skill_dict = {}
                                else:
                                        for name in skill_names_list:
                                                skill_dict[name] = st.loadCompetence(name)
                        if button_ctx.custom_id == "not_display":
                                await button_ctx.edit_origin(content=nonetxt)
                                await ctx.send("`skill01`|`skill02`|`skill03`|`skill04`,`........`")
                                try:
                                        string_skill_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        string_skill = str(string_skill_input.content)
                                        await ctx.send("__skill list : __ `" + string_skill + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        string_skill = "none"
                                skill_names_list = string_skill.split("|")
                                skill_dict = {}
                                if skill_names_list == ["none"]:
                                        skill_dict = {}
                                else:
                                        for name in skill_names_list:
                                                skill_dict[name] = st.loadCompetence(name)
                        new_weapon_type = rp.WeaponTypeClass(equipement_type_name,equipement_type_description,rp.StatisticsClass("",attack_template_constructor),skill_dict,modifier,equipement_type_image_path)
                        st.saveEquipement(new_weapon_type,equipement_type_name)
                        pass
                if equipement_type_aux.values[0] == "accessory_type":
                        modifier_select = tf.getListSelection(ctx,"chose the modifier of the weapon ",["strength","dexterity","bleeding","posture","constitution","evasion","intellect","charisma","wisdom"],["strength","dexterity","bleeding","posture","constitution","evasion","intellect","charisma","wisdom"])
                        fait_choix = await equipement_type_aux.send("`chose the modifier of the weapon : `", components=[create_actionrow(modifier_select)])
                        modifier_select_aux = await wait_for_component(notlolabot.bot, components=modifier_select, check=check)
                        modifier = modifier_select_aux.values[0]
                        await modifier_select_aux.send("`__enter the list of the competences__`")
                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                    label="display the skill list",
                                                    custom_id="display"),
                                      create_button(style=ButtonStyle.blue,
                                                    label="not display the skill list",
                                                    custom_id="not_display")]
                        button_raw = create_actionrow(*my_buttons)
                        fait_choix = await ctx.send("`Push for the skill list : `", components=[button_raw])
                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                        if button_ctx.custom_id == "display":
                                await button_ctx.edit_origin(content=nonetxt)
                                skill_list = st.antiFilterCompetences(["weapon_attack","one hand weapon_attack"])
                                skill_embed_list = tf.getListEmbedSkillsList(ctx,skill_list,"weapon attack")
                                for skill_embed in skill_embed_list:
                                        await ctx.send(embed=skill_embed)
                                await modifier_select_aux.send("`skill01`|`skill02`|`skill03`|`skill04`,`........`")
                                try:
                                        string_skill_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        string_skill = str(string_skill_input.content)
                                        await ctx.send("__skill list : __ `" + string_skill + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        string_skill = "none"
                                skill_names_list = string_skill.split("|")
                                skill_dict = {}
                                if skill_names_list == ["none"]:
                                        skill_dict = {}
                                else:
                                        for name in skill_names_list:
                                                skill_dict[name] = st.loadCompetence(name)
                        if button_ctx.custom_id == "not_display":
                                await button_ctx.edit_origin(content=nonetxt)
                                await modifier_select_aux.send("`skill01`|`skill02`|`skill03`|`skill04`,`........`")
                                try:
                                        string_skill_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        string_skill = str(string_skill_input.content)
                                        await ctx.send("__skill list : __ `" + string_skill + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        string_skill = "none"
                                skill_names_list = string_skill.split("|")
                                skill_dict = {}
                                if skill_names_list == ["none"]:
                                        skill_dict = {}
                                else:
                                        for name in skill_names_list:
                                                skill_dict[name] = st.loadCompetence(name)
                        new_accessory_type = rp.AccessoryClassTypeClass(equipement_type_name,equipement_type_description,skill_dict,modifier,equipement_type_image_path)
                        st.saveEquipement(new_accessory_type,equipement_type_name)
                        pass
                if equipement_type_aux.values[0] == "armor_type":
                        posture_dice_select = tf.getListSelection(ctx,"chose the posture dice of the armor",[str(x) for x in range(15)],[str(x) for x in range(15)])
                        fait_choix = await equipement_type_aux.send("`chose the posture dice of the armor : `", components=[create_actionrow(posture_dice_select)])
                        posture_dice_aux = await wait_for_component(notlolabot.bot, components=posture_dice_select, check=check)
                        posture_constent_select = tf.getListSelection(ctx,"chose the posture of the armor",[str(x) for x in range(8)],[str(x) for x in range(8)])
                        fait_choix = await posture_dice_aux.send("`chose the posture of the armor : `", components=[create_actionrow(posture_constent_select)])
                        posture_constent_aux = await wait_for_component(notlolabot.bot, components=posture_constent_select, check=check)
                        constitution_dice_select = tf.getListSelection(ctx,"chose the constitution dice of the armor",[str(x) for x in range(15)],[str(x) for x in range(15)])
                        fait_choix = await posture_constent_aux.send("`chose the constitution dice of the armor : `", components=[create_actionrow(constitution_dice_select)])
                        constitution_dice_aux = await wait_for_component(notlolabot.bot, components=constitution_dice_select, check=check)
                        constitution_constent_select = tf.getListSelection(ctx,"chose the constitution of the armor",[str(x) for x in range(8)],[str(x) for x in range(8)])
                        fait_choix = await constitution_dice_aux.send("`chose the constitution of the armor : `", components=[create_actionrow(constitution_constent_select)])
                        constitution_constent_aux = await wait_for_component(notlolabot.bot, components=constitution_constent_select, check=check)
                        evasion_dice_select = tf.getListSelection(ctx,"chose the evasion dice of the armor",[str(x) for x in range(15)],[str(x) for x in range(15)])
                        fait_choix = await constitution_constent_aux.send("`chose the evasion dice of the armor : `", components=[create_actionrow(evasion_dice_select)])
                        evasion_dice_aux = await wait_for_component(notlolabot.bot, components=evasion_dice_select, check=check)
                        evasion_constent_select = tf.getListSelection(ctx,"chose the evasion of the armor",[str(x) for x in range(8)],[str(x) for x in range(8)])
                        fait_choix = await evasion_dice_aux.send("`chose the evasion of the armor : `", components=[create_actionrow(evasion_constent_select)])
                        evasion_constent_aux = await wait_for_component(notlolabot.bot, components=evasion_constent_select, check=check)                
                        await evasion_constent_aux.send(nonetxt)
                        attack_template_constructor = {"strength" : (0,0),"dexterity" : (0,0),"bleeding" : (0,0) ,
                                                       "posture" : (int(posture_dice_aux.values[0]),int(posture_constent_aux.values[0])) ,
                                                       "constitution" : (int(constitution_dice_aux.values[0]),int(constitution_constent_aux.values[0])),
                                                       "evasion" : (int(evasion_dice_aux.values[0]),int(evasion_constent_aux.values[0])),
                                                       "intellect" : (0,0),"charisma" : (0,0) ,"wisdom" : (0,0)}
                        new_armor_type = rp.ArmorClassTypeClass(equipement_type_name,equipement_type_description,rp.StatisticsClass("",attack_template_constructor),equipement_type_image_path)
                        st.saveEquipement(new_armor_type,equipement_type_name)
                        pass
                display_equipement_type = st.loadEquipement(equipement_type_name)
                my_embed = tf.getEmbedEquipementType(ctx,display_equipement_type)
                await ctx.send(embed=my_embed)
                pass
        if register_type.values[0] == "race":
                await register_type.send("`__enter the name of the race__`")
                try:
                        race_name_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                        race_name = str(race_name_input.content)
                        await ctx.send("__race name : __ `" + race_name + "`")
                except:
                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                        race_name = "none"
                await register_type.send("`__enter the description of the race__`")
                try:
                        race_description_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                        race_description = str(race_description_input.content)
                        await ctx.send("__race description : __ `" + race_description + "`")
                except:
                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                        race_description = "none"
                await register_type.send("`__enter the image url of the race__`")
                try:
                        race_image_path_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                        race_image_path = str(race_image_path_input.content)
                except:
                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                        race_image_path = "https://cdn.discordapp.com/attachments/1005626886195527720/1005627343999610910/Inconnu.png"
                await ctx.send("`__enter the list of the competences__`")
                my_buttons = [create_button(style=ButtonStyle.blue,
                                            label="display the skill list",
                                            custom_id="display"),
                              create_button(style=ButtonStyle.blue,
                                            label="not display the skill list",
                                            custom_id="not_display")]
                button_raw = create_actionrow(*my_buttons)
                fait_choix = await ctx.send("`Push for the skill list : `", components=[button_raw])
                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                if button_ctx.custom_id == "display":
                        await button_ctx.edit_origin(content=nonetxt)
                        skill_list = st.antiFilterCompetences(["weapon_attack","one hand weapon_attack"])
                        skill_embed_list = tf.getListEmbedSkillsList(ctx,skill_list,"weapon attack")
                        for skill_embed in skill_embed_list:
                                await ctx.send(embed=skill_embed)
                        await ctx.send("`skill01`|`skill02`|`skill03`|`skill04`,`........`")
                        try:
                                string_skill_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                string_skill = str(string_skill_input.content)
                                await ctx.send("__skill list : __ `" + string_skill + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                string_skill = "none"
                        skill_names_list = string_skill.split("|")
                        skill_dict = {}
                        if skill_names_list == ["none"]:
                                skill_dict = {}
                        else:
                                for name in skill_names_list:
                                        skill_dict[name] = st.loadCompetence(name)
                if button_ctx.custom_id == "not_display":
                        await button_ctx.edit_origin(content=nonetxt)
                        await ctx.send("`skill01`|`skill02`|`skill03`|`skill04`,`........`")
                        try:
                                string_skill_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                string_skill = str(string_skill_input.content)
                                await ctx.send("__skill list : __ `" + string_skill + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                string_skill = "none"
                        skill_names_list = string_skill.split("|")
                        skill_dict = {}
                        if skill_names_list == ["none"]:
                                skill_dict = {}
                        else:
                                for name in skill_names_list:
                                        skill_dict[name] = st.loadCompetence(name)
                new_race = rp.RaceClass(race_name,race_description,race_image_path,skill_dict)
                st.saveRace(new_race)
                display_race = st.loadRace(race_name)
                my_embed_list = tf.getListEmbedImageRace(ctx ,display_race)
                for my_embed in my_embed_list:
                        await ctx.send(embed=my_embed)
                pass
        if register_type.values[0] == "classe":
                await register_type.send("`__enter the name of the classe__`")
                try:
                        classe_name_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                        classe_name = str(classe_name_input.content)
                        await ctx.send("__classe name : __ `" + classe_name + "`")
                except:
                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                        classe_name = "none"
                await register_type.send("`__enter the description of the classe__`")
                try:
                        classe_description_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                        classe_description = str(classe_description_input.content)
                        await ctx.send("__classe description : __ `" + classe_description + "`")
                except:
                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                        classe_description = "none"
                await register_type.send("`__enter the image url of the classe__`")
                try:
                        classe_image_path_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                        classe_image_path = str(classe_image_path_input.content)
                except:
                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                        classe_image_path = "https://cdn.discordapp.com/attachments/1005626886195527720/1005627343999610910/Inconnu.png"
                modifier_select = tf.getListSelection(ctx,"chose the modifier of the class ",["strength","dexterity","bleeding","posture","constitution","evasion","intellect","charisma","wisdom"],["strength","dexterity","bleeding","posture","constitution","evasion","intellect","charisma","wisdom"])
                fait_choix = await register_type.send("`chose the modifier of the class : `", components=[create_actionrow(modifier_select)])
                modifier_select_aux = await wait_for_component(notlolabot.bot, components=modifier_select, check=check)
                modifier = modifier_select_aux.values[0]
                await modifier_select_aux.send("`__enter the list of the competences__`")
                my_buttons = [create_button(style=ButtonStyle.blue,
                                            label="display the skill list",
                                            custom_id="display"),
                              create_button(style=ButtonStyle.blue,
                                            label="not display the skill list",
                                            custom_id="not_display")]
                button_raw = create_actionrow(*my_buttons)
                fait_choix = await ctx.send("`Push for the skill list : `", components=[button_raw])
                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                if button_ctx.custom_id == "display":
                        await button_ctx.edit_origin(content=nonetxt)
                        skill_list = st.antiFilterCompetences(["weapon_attack","one hand weapon_attack"])
                        skill_embed_list = tf.getListEmbedSkillsList(ctx,skill_list,"weapon attack")
                        for skill_embed in skill_embed_list:
                                await ctx.send(embed=skill_embed)
                        await modifier_select_aux.send("`skill01`|`skill02`|`skill03`|`skill04`,`........`")
                        try:
                                string_skill_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                string_skill = str(string_skill_input.content)
                                await ctx.send("__skill list : __ `" + string_skill + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                string_skill = "none"
                        skill_names_list = string_skill.split("|")
                        skill_dict = {}
                        if skill_names_list == ["none"]:
                                skill_dict = {}
                        else:
                                for name in skill_names_list:
                                        skill_dict[name] = st.loadCompetence(name)
                if button_ctx.custom_id == "not_display":
                        await button_ctx.edit_origin(content=nonetxt)
                        await modifier_select_aux.send("`skill01`|`skill02`|`skill03`|`skill04`,`........`")
                        try:
                                string_skill_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                string_skill = str(string_skill_input.content)
                                await ctx.send("__skill list : __ `" + string_skill + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                string_skill = "none"
                        skill_names_list = string_skill.split("|")
                        skill_dict = {}
                        if skill_names_list == ["none"]:
                                skill_dict = {}
                        else:
                                for name in skill_names_list:
                                        skill_dict[name] = st.loadCompetence(name)
                new_classe = rp.ClasseClass(classe_name,classe_description,classe_image_path,skill_dict,modifier)
                st.saveClasse(new_classe)
                display_classe = st.loadClasse(classe_name)
                my_embed_list = tf.getListEmbedImageClasse(ctx ,display_classe)
                for my_embed in my_embed_list:
                        await ctx.send(embed=my_embed)   
                pass
        if register_type.values[0] == "character":
                display_name = ctx.author.display_name
                user_name = ctx.author.name
                await register_type.send("`__enter the name of the character__`")
                try:
                        char_name_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                        char_name = str(char_name_input.content)
                        await ctx.send("__name of the character : __ `" + char_name + "`")
                except:
                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                        char_name = "none"
                await register_type.send("`__enter the physical description of the character__`")
                try:
                        char_description_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                        char_description = str(char_description_input.content)
                        await ctx.send("__physical description of the character : __ `" + char_description + "`")
                except:
                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                        char_description = nonetxt
                await register_type.send("`__enter the image url of the character__`")
                try:
                        char_image_path_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                        char_image_path = str(char_image_path_input.content)
                        await ctx.send("` image load`")
                except:
                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                        char_image_path = ctx.author.avatar_url
                if char_image_path == "none":
                        char_image_path = ctx.author.avatar_url
                await register_type.send("`__enter the nickname of the character (if your character dont have a nickname writte 'none')__`")
                try:
                        char_nick_name_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                        char_nick_name = str(char_nick_name_input.content)
                        await ctx.send("__nickname of the character : __ `" + char_nick_name + "`")
                except:
                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                        char_nick_name = nonetxt
                if char_nick_name == "none":
                        char_nick_name = nonetxt
                await register_type.send("`__enter the history of the character__`")
                try:
                        char_history_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                        if char_history_input.attachments != [] and char_history_input.attachments[0].filename.endswith(".txt"):
                                await char_history_input.attachments[0].save(r"files_saves\file_" + char_history_input.attachments[0].filename)
                                file = open(r"files_saves\file_" + char_history_input.attachments[0].filename,"r")
                                char_history = file.read()
                                file.close()
                        else:
                                char_history = str(char_history_input.content)
                        await ctx.send("`lore load`")
                except:
                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                        char_history = nonetxt
                await register_type.send("`__enter the titles of the character(like master of the mercenary guild)(if your character dont have titles writte 'none')__`")
                await ctx.send("title01|title02|.......|title0n")
                try:
                        char_titles_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                        if char_titles_input.content == "none":
                                char_titles = []
                        else:
                                char_titles = (str(char_titles_input.content)).split("|")
                        await ctx.send("`titles load`")
                except:
                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                        char_tiles = []
                await register_type.send("`__enter the languages of the character__`")
                await ctx.send("language01|language02|.......|language0n")
                try:
                        char_languages_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                        if char_languages_input.content == "none":
                                char_languages = []
                        else:
                                char_languages = (str(char_languages_input.content)).split("|")
                        await ctx.send("`languages load`")
                except:
                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                        char_languages = []
                backgrounds_list = ["soldat","guerrier","mercenaire","officier","vaguabon","noble","espion","assassin","escroc","voleur","sorcier","academiste","acolyte",
                                    "esclave","mage","maitre d'arme","inspincteur","truand","chercheur","habitant des forets","bourgeois","experience ratée"]
                char_background_selection = tf.getListSelection(ctx,"chose the background",backgrounds_list,backgrounds_list,1,4)
                fait_choix = await register_type.send("`Chose the background : `", components=[create_actionrow(char_background_selection)])
                char_background_aux = await wait_for_component(notlolabot.bot, components=char_background_selection, check=check)
                await char_background_aux.send(nonetxt)
                char_background_list = char_background_aux.values
                allignement_list = ["loyal bon","neutre bon","chaotique bon","loyal neutre","neutre","chaotique neutre","loyal mauvais","neutre mauvais","chaotique mauvais"]
                char_allignement_selection = tf.getListSelection(ctx,"chose the allignement",allignement_list,allignement_list)
                fait_choix = await register_type.send("`Chose the allignement : `", components=[create_actionrow(char_allignement_selection)])
                char_allignement_aux = await wait_for_component(notlolabot.bot, components=char_allignement_selection, check=check)
                await char_allignement_aux.send(nonetxt)
                char_allignement = char_allignement_aux.values[0]
                await register_type.send("`__enter the capital in gold piece of the character__`")
                try:
                        char_capital_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                        char_capital = int(str(char_capital_input.content))
                        await ctx.send("__capital of the character : __ `" + str(char_capital) + " golds`")
                except:
                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                        char_capital = 10
                await register_type.send("`__enter the level of the character__`")
                try:
                        char_level_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                        char_level = int(str(char_level_input.content))
                        await ctx.send("__level of the character : __ `" + str(char_level) + "`")
                except:
                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                        char_level = 1
                char_max_hp_selection = tf.getListSelection(ctx,"chose the max_hp of the character",["caster","dps","mid tank","tank"],["150","200","250","280"])
                fait_choix = await char_background_aux.send("`Chose the background : `", components=[create_actionrow(char_max_hp_selection)])
                char_max_hp_aux = await wait_for_component(notlolabot.bot, components=char_max_hp_selection, check=check)
                await char_max_hp_aux.send(nonetxt)
                char_max_hp = int(char_max_hp_aux.values[0])
                await register_type.send("`__enter the race name of the character__`")
                my_buttons = [create_button(style=ButtonStyle.blue,
                                            label="display the race list",
                                            custom_id="display"),
                              create_button(style=ButtonStyle.blue,
                                            label="not display the race list",
                                            custom_id="not_display")]
                button_raw = create_actionrow(*my_buttons)
                fait_choix = await ctx.send("`Push for the race list : `", components=[button_raw])
                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                if button_ctx.custom_id == "display":
                        await button_ctx.edit_origin(content=nonetxt)
                        race_list = list((st.loadDict("database\RacesDatabase.obj")).keys())
                        race_embed_list = tf.getListEmbedRaceList(ctx,race_list)
                        for race_embed in race_embed_list:
                                await ctx.send(embed=race_embed)
                        await register_type.send("`race chose`")
                        try:
                                string_race_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                race_name = str(string_race_input.content)
                                await ctx.send("__race : __ `" + race_name + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                race_name = "none"
                elif button_ctx.custom_id == "not_display":
                        await button_ctx.edit_origin(content=nonetxt)
                        await register_type.send("`race chose`")
                        try:
                                string_race_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                race_name = str(string_race_input.content)
                                await ctx.send("__race : __ `" + race_name + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                race_name = "none"
                if race_name != "none":
                        char_race = st.loadRace(race_name)
                else:
                        char_race = rp.RaceClass("","","",{})
                await register_type.send("`__enter the classe name of the character__`")
                my_buttons = [create_button(style=ButtonStyle.blue,
                                            label="display the classe list",
                                            custom_id="display"),
                              create_button(style=ButtonStyle.blue,
                                            label="not display the classe list",
                                            custom_id="not_display")]
                button_raw = create_actionrow(*my_buttons)
                fait_choix = await ctx.send("`Push for the classe list : `", components=[button_raw])
                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                if button_ctx.custom_id == "display":
                        await button_ctx.edit_origin(content=nonetxt)
                        classe_list = list((st.loadDict("database\ClassDatabase.obj")).keys())
                        classe_embed_list = tf.getListEmbedClasseList(ctx,classe_list)
                        for classe_embed in classe_embed_list:
                                await ctx.send(embed=classe_embed)
                        await register_type.send("`classe chose`")
                        try:
                                string_classe_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                classe_name = str(string_classe_input.content)
                                await ctx.send("__classe : __ `" + classe_name + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                classe_name = "none"
                elif button_ctx.custom_id == "not_display":
                        await button_ctx.edit_origin(content=nonetxt)
                        await register_type.send("`classe chose`")
                        try:
                                string_classe_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                classe_name = str(string_classe_input.content)
                                await ctx.send("__classe : __ `" + classe_name + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                classe_name = "none"
                if classe_name != "none":
                        char_classe = st.loadClasse(classe_name)
                else:
                        char_classe = rp.ClasseClass("","","",{},"")
                await register_type.send("`__enter the organisation name of the character(if your character dont have a organisation writte 'none')__`")
                my_buttons = [create_button(style=ButtonStyle.blue,
                                            label="display the organisation list",
                                            custom_id="display"),
                              create_button(style=ButtonStyle.blue,
                                            label="not display the organisation list",
                                            custom_id="not_display")]
                button_raw = create_actionrow(*my_buttons)
                fait_choix = await ctx.send("`Push for the organisation list : `", components=[button_raw])
                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                if button_ctx.custom_id == "display":
                        await button_ctx.edit_origin(content=nonetxt)
                        organisation_list = list((st.loadDict("database\OrganisationsDatabase.obj")).keys())
                        organisation_embed_list = tf.getListEmbedOrganisationList(ctx,organisation_list)
                        for organisation_embed in organisation_embed_list:
                                await ctx.send(embed=organisation_embed)
                        await register_type.send("`organisation chose`")
                        try:
                                string_organisation_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                organisation_name = str(string_organisation_input.content)
                                await ctx.send("__Organisation : __ `" + organisation_name + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                organisation_name = "none"
                elif button_ctx.custom_id == "not_display":
                        await button_ctx.edit_origin(content=nonetxt)
                        await register_type.send("`Organisation chose`")
                        try:
                                string_organisation_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                organisation_name = str(string_organisation_input.content)
                                await ctx.send("__Organisation : __ `" + organisation_name + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                organisation_name = "none"
                if organisation_name != "none":
                        char_organisation = st.loadOrganisation(organisation_name)
                else:
                        char_organisation = rp.OrganisationClass("","",0,0,rp.StatisticsClass(""),"")
                await ctx.send(":exclamation: __Ne vous trompez pas sur les valeurs que vous voulez choisir , car il faudra recommencé la creation du personnage!.__")
                attack_dice_select = tf.getListSelection(ctx,"chose the bonus damage dice of the character",[str(x) for x in range(15)],[str(x) for x in range(15)])
                fait_choix = await register_type.send("`chose the bonus damage dice of the character : `", components=[create_actionrow(attack_dice_select)])
                attack_dice_aux = await wait_for_component(notlolabot.bot, components=attack_dice_select, check=check)
                attack_constent_select = tf.getListSelection(ctx,"chose the damage bonus of the character",[str(x) for x in range(5)],[str(x) for x in range(5)])
                fait_choix = await attack_dice_aux.send("`chose the damage bonus of the character : `", components=[create_actionrow(attack_constent_select)])
                attack_constent_aux = await wait_for_component(notlolabot.bot, components=attack_constent_select, check=check)
                dexterity_dice_select = tf.getListSelection(ctx,"chose the bonus dexterity dice of the character",[str(x) for x in range(15)],[str(x) for x in range(15)])
                fait_choix = await attack_constent_aux.send("`chose the bonus dexterity dice of the character : `", components=[create_actionrow(dexterity_dice_select)])
                dexterity_dice_aux = await wait_for_component(notlolabot.bot, components=dexterity_dice_select, check=check)
                dexterity_constent_select = tf.getListSelection(ctx,"chose the dexterity bonus of the character",[str(x) for x in range(5)],[str(x) for x in range(5)])
                fait_choix = await dexterity_dice_aux.send("`chose the dexterity bonus of the character : `", components=[create_actionrow(dexterity_constent_select)])
                dexterity_constent_aux = await wait_for_component(notlolabot.bot, components=dexterity_constent_select, check=check)
                bleeding_dice_select = tf.getListSelection(ctx,"chose the bonus bleeding dice of the character",[str(x) for x in range(15)],[str(x) for x in range(15)])
                fait_choix = await dexterity_constent_aux.send("`chose the bonus bleeding dice of the character : `", components=[create_actionrow(bleeding_dice_select)])
                bleeding_dice_aux = await wait_for_component(notlolabot.bot, components=bleeding_dice_select, check=check)
                bleeding_constent_select = tf.getListSelection(ctx,"chose the bonus bleeding of the character",[str(x) for x in range(5)],[str(x) for x in range(5)])
                fait_choix = await bleeding_dice_aux.send("`chose the bonus bleeding of the character : `", components=[create_actionrow(bleeding_constent_select)])
                bleeding_constent_aux = await wait_for_component(notlolabot.bot, components=bleeding_constent_select, check=check)
                posture_dice_select = tf.getListSelection(ctx,"chose the bonus posture dice of the character",[str(x) for x in range(15)],[str(x) for x in range(15)])
                fait_choix = await bleeding_constent_aux.send("`chose the bonus posture dice of the character : `", components=[create_actionrow(posture_dice_select)])
                posture_dice_aux = await wait_for_component(notlolabot.bot, components=posture_dice_select, check=check)
                posture_constent_select = tf.getListSelection(ctx,"chose the posture bonus of the character",[str(x) for x in range(5)],[str(x) for x in range(5)])
                fait_choix = await posture_dice_aux.send("`chose the posture bonus of the character : `", components=[create_actionrow(posture_constent_select)])
                posture_constent_aux = await wait_for_component(notlolabot.bot, components=posture_constent_select, check=check)
                constitution_dice_select = tf.getListSelection(ctx,"chose the bonus constitution dice of the character",[str(x) for x in range(15)],[str(x) for x in range(15)])
                fait_choix = await posture_constent_aux.send("`chose the bonus constitution dice of the character : `", components=[create_actionrow(constitution_dice_select)])
                constitution_dice_aux = await wait_for_component(notlolabot.bot, components=constitution_dice_select, check=check)
                constitution_constent_select = tf.getListSelection(ctx,"chose the constitution bonus of the character",[str(x) for x in range(5)],[str(x) for x in range(5)])
                fait_choix = await constitution_dice_aux.send("`chose the constitution bonus of the character : `", components=[create_actionrow(constitution_constent_select)])
                constitution_constent_aux = await wait_for_component(notlolabot.bot, components=constitution_constent_select, check=check)
                evasion_dice_select = tf.getListSelection(ctx,"chose the bonus evasion dice of the character",[str(x) for x in range(15)],[str(x) for x in range(15)])
                fait_choix = await constitution_constent_aux.send("`chose the bonus evasion dice of the character : `", components=[create_actionrow(evasion_dice_select)])
                evasion_dice_aux = await wait_for_component(notlolabot.bot, components=evasion_dice_select, check=check)
                evasion_constent_select = tf.getListSelection(ctx,"chose the evasion bonus of the character",[str(x) for x in range(5)],[str(x) for x in range(5)])
                fait_choix = await evasion_dice_aux.send("`chose the evasion bonus of the character : `", components=[create_actionrow(evasion_constent_select)])
                evasion_constent_aux = await wait_for_component(notlolabot.bot, components=evasion_constent_select, check=check)
                intellect_dice_select = tf.getListSelection(ctx,"chose the bonus intellect dice of the character",[str(x) for x in range(15)],[str(x) for x in range(15)])
                fait_choix = await evasion_constent_aux.send("`chose the bonus intellect dice of the character : `", components=[create_actionrow(intellect_dice_select)])
                intellect_dice_aux = await wait_for_component(notlolabot.bot, components=intellect_dice_select, check=check)
                intellect_constent_select = tf.getListSelection(ctx,"chose the intellect bonus of the character",[str(x) for x in range(5)],[str(x) for x in range(5)])
                fait_choix = await intellect_dice_aux.send("`chose the intellect bonus of the character : `", components=[create_actionrow(intellect_constent_select)])
                intellect_constent_aux = await wait_for_component(notlolabot.bot, components=intellect_constent_select, check=check)
                charisma_dice_select = tf.getListSelection(ctx,"chose the bonus charisma dice of the character",[str(x) for x in range(15)],[str(x) for x in range(15)])
                fait_choix = await intellect_constent_aux.send("`chose the bonus charisma dice of the character : `", components=[create_actionrow(charisma_dice_select)])
                charisma_dice_aux = await wait_for_component(notlolabot.bot, components=charisma_dice_select, check=check)
                charisma_constent_select = tf.getListSelection(ctx,"chose the charisma bonus of the character",[str(x) for x in range(5)],[str(x) for x in range(5)])
                fait_choix = await charisma_dice_aux.send("`chose the charisma bonus of the character : `", components=[create_actionrow(charisma_constent_select)])
                charisma_constent_aux = await wait_for_component(notlolabot.bot, components=charisma_constent_select, check=check)
                wisdom_dice_select = tf.getListSelection(ctx,"chose the bonus wisdom dice of the character",[str(x) for x in range(15)],[str(x) for x in range(15)])
                fait_choix = await charisma_constent_aux.send("`chose the bonus wisdom dice of the character : `", components=[create_actionrow(wisdom_dice_select)])
                wisdom_dice_aux = await wait_for_component(notlolabot.bot, components=wisdom_dice_select, check=check)
                wisdom_constent_select = tf.getListSelection(ctx,"chose the wisdom bonus of the character",[str(x) for x in range(5)],[str(x) for x in range(5)])
                fait_choix = await wisdom_dice_aux.send("`chose the wisdom bonus of the character : `", components=[create_actionrow(wisdom_constent_select)])
                wisdom_constent_aux = await wait_for_component(notlolabot.bot, components=wisdom_constent_select, check=check)                
                await wisdom_constent_aux.send(nonetxt)
                attack_template_constructor = {"strength" : (int(attack_dice_aux.values[0]),int(attack_dice_aux.values[0])),
                                               "dexterity" : (int(dexterity_dice_aux.values[0]),int(dexterity_constent_aux.values[0])),
                                               "bleeding" : (int(bleeding_dice_aux.values[0]),int(bleeding_constent_aux.values[0])) ,
                                               "posture" : (int(posture_dice_aux.values[0]),int(posture_constent_aux.values[0])) ,
                                               "constitution" : (int(constitution_dice_aux.values[0]),int(constitution_constent_aux.values[0])),
                                               "evasion" : (int(evasion_dice_aux.values[0]),int(evasion_constent_aux.values[0])),
                                               "intellect" : (int(intellect_dice_aux.values[0]),int(intellect_constent_aux.values[0])),
                                               "charisma" : (int(charisma_dice_aux.values[0]),int(charisma_constent_aux.values[0])) ,
                                               "wisdom" : (int(wisdom_dice_aux.values[0]),int(wisdom_constent_aux.values[0]))}
                arcanes_select = tf.getListSelection(ctx,"chose the arcanes value of the character",[str(x) for x in range(21)],[str(x) for x in range(21)])
                fait_choix = await register_type.send("`chose the arcanes value of the character : `", components=[create_actionrow(arcanes_select)])
                arcanes_aux = await wait_for_component(notlolabot.bot, components=arcanes_select, check=check)
                athletism_select = tf.getListSelection(ctx,"chose the athletism value of the character",[str(x) for x in range(21)],[str(x) for x in range(21)])
                fait_choix = await arcanes_aux.send("`chose the athletism value of the character : `", components=[create_actionrow(athletism_select)])
                athletism_aux = await wait_for_component(notlolabot.bot, components=athletism_select, check=check)
                discretion_select = tf.getListSelection(ctx,"chose the discretion value of the character",[str(x) for x in range(21)],[str(x) for x in range(21)])
                fait_choix = await athletism_aux.send("`chose the discretion value of the character : `", components=[create_actionrow(discretion_select)])
                discretion_aux = await wait_for_component(notlolabot.bot, components=discretion_select, check=check)
                history_select = tf.getListSelection(ctx,"chose the history value of the character",[str(x) for x in range(21)],[str(x) for x in range(21)])
                fait_choix = await discretion_aux.send("`chose the history value of the character : `", components=[create_actionrow(history_select)])
                history_aux = await wait_for_component(notlolabot.bot, components=history_select, check=check)
                intimidation_select = tf.getListSelection(ctx,"chose the intimidation value of the character",[str(x) for x in range(21)],[str(x) for x in range(21)])
                fait_choix = await history_aux.send("`chose the intimidation value of the character : `", components=[create_actionrow(intimidation_select)])
                intimidation_aux = await wait_for_component(notlolabot.bot, components=intimidation_select, check=check)
                investigation_select = tf.getListSelection(ctx,"chose the investigation value of the character",[str(x) for x in range(21)],[str(x) for x in range(21)])
                fait_choix = await intimidation_aux.send("`chose the investigation value of the character : `", components=[create_actionrow(investigation_select)])
                investigation_aux = await wait_for_component(notlolabot.bot, components=investigation_select, check=check)
                medicine_select = tf.getListSelection(ctx,"chose the medicine value of the character",[str(x) for x in range(21)],[str(x) for x in range(21)])
                fait_choix = await investigation_aux.send("`chose the medicine value of the character : `", components=[create_actionrow(medicine_select)])
                medicine_aux = await wait_for_component(notlolabot.bot, components=medicine_select, check=check)
                religion_select = tf.getListSelection(ctx,"chose the religion value of the character",[str(x) for x in range(21)],[str(x) for x in range(21)])
                fait_choix = await medicine_aux.send("`chose the religion value of the character : `", components=[create_actionrow(religion_select)])
                religion_aux = await wait_for_component(notlolabot.bot, components=religion_select, check=check)
                survive_select = tf.getListSelection(ctx,"chose the survive value of the character",[str(x) for x in range(21)],[str(x) for x in range(21)])
                fait_choix = await religion_aux.send("`chose the survive value of the character : `", components=[create_actionrow(survive_select)])
                survive_aux = await wait_for_component(notlolabot.bot, components=survive_select, check=check)
                occultism_select = tf.getListSelection(ctx,"chose the occultism value of the character",[str(x) for x in range(21)],[str(x) for x in range(21)])
                fait_choix = await survive_aux.send("`chose the occultism value of the character : `", components=[create_actionrow(occultism_select)])
                occultism_aux = await wait_for_component(notlolabot.bot, components=occultism_select, check=check)
                calm_select = tf.getListSelection(ctx,"chose the calm value of the character",[str(x) for x in range(21)],[str(x) for x in range(21)])
                fait_choix = await occultism_aux.send("`chose the calm value of the character : `", components=[create_actionrow(calm_select)])
                calm_aux = await wait_for_component(notlolabot.bot, components=calm_select, check=check)
                await calm_aux.send(nonetxt)
                other_statistics_pattern = {"arcanes" : int(arcanes_aux.values[0]),
                                            "athletics" : int(athletism_aux.values[0]),
                                            "discretion" : int(discretion_aux.values[0]),
                                            "history" : int(history_aux.values[0]),
                                            "intimidation" : int(intimidation_aux.values[0]),
                                            "investigation" : int(investigation_aux.values[0]),
                                            "medicine" : int(medicine_aux.values[0]),
                                            "religion" : int(religion_aux.values[0]),
                                            "survive" : int(survive_aux.values[0]),
                                            "occultism" : int(occultism_aux.values[0]),
                                            "calm" : int(calm_aux.values[0])}
                await ctx.send(":exclamation: __Vous avez droit d'avoir entre 0 a 3 armes maximum.__")
                await ctx.send(":exclamation: __Soyez rp , un lanceur de sorts pure et dure , ne maitrise pas 3 types d'armes.__")
                await ctx.send(":exclamation: `Pour des raisons d'equilibrage , si votre personnage lance beaucoup de sorts , veuillez vous limité a un nombre d'armes variant de 0 a 2 armes(donc en moyenne 1).`")
                await register_type.send("`do you want to generate a new weapon`")
                my_buttons = [create_button(style=ButtonStyle.blue,
                                            label="generate a new weapon",
                                            custom_id="generate"),
                              create_button(style=ButtonStyle.blue,
                                            label="dont generate a new weapon",
                                            custom_id="not_generate")]
                button_raw = create_actionrow(*my_buttons)
                fait_choix = await ctx.send("`Push for generation : `", components=[button_raw])
                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                if button_ctx.custom_id == "generate":
                        await button_ctx.edit_origin(content=nonetxt)
                        await ctx.send("`__enter the name of the 1st weapon(not the type of the weapon , the name)__`")
                        try:
                                first_weapon_name_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                first_weapon_name = str(first_weapon_name_input.content)
                                await ctx.send("__name of the 1st weapon : __ `" + first_weapon_name + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                first_weapon_name = nonetxt
                        await ctx.send("`__enter the description of the 1st weapon__`")
                        try:
                                first_weapon_description_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                first_weapon_description = str(first_weapon_description_input.content)
                                await ctx.send("__descrition of the 1st weapon : __ `" + first_weapon_description + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                first_weapon_description = nonetxt
                        await ctx.send("`__enter the level of the 1st weapon__`")
                        try:
                                first_weapon_level_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                first_weapon_level = int(first_weapon_level_input.content)
                                await ctx.send("__level of the 1st weapon : __ `" + str(first_weapon_level) + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                first_weapon_level = 0
                        await ctx.send("`__enter the type of the 1st weapon__`")
                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                    label="display the equipement-type list",
                                                    custom_id="display"),
                                      create_button(style=ButtonStyle.blue,
                                                    label="not display the equipement-type list",
                                                    custom_id="not_display")]
                        button_raw = create_actionrow(*my_buttons)
                        fait_choix = await ctx.send("`Push for the equipement-type list : `", components=[button_raw])
                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                        if button_ctx.custom_id == "display":
                                await button_ctx.edit_origin(content=nonetxt)
                                equipement_list = list(st.filterEquipementType("weapon_type"))
                                equipement_embed_list = tf.getListEmbedEquipementList(ctx,equipement_list)
                                for equipement_embed in equipement_embed_list:
                                        await ctx.send(embed=equipement_embed)
                                await ctx.send("`equipement chose`")
                                try:
                                        string_equipement_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        equipement_name = str(string_equipement_input.content)
                                        await ctx.send("__equipement-type : __ `" + equipement_name + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        equipement_name = "none"
                        elif button_ctx.custom_id == "not_display":
                                await button_ctx.edit_origin(content=nonetxt)
                                await view_type.send("`equipement-type chose`")
                                try:
                                        string_equipement_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        equipement_name = str(string_equipement_input.content)
                                        await ctx.send("__equipement-type : __ `" + equipement_name + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        equipement_name = "none"
                        first_weapon_type = st.loadEquipement(equipement_name)
                        await ctx.send("`__enter the enchance of the 1st weapon__`")
                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                    label="display the enchance list",
                                                    custom_id="display"),
                                      create_button(style=ButtonStyle.blue,
                                                    label="not display the enchance list",
                                                    custom_id="not_display")]
                        button_raw = create_actionrow(*my_buttons)
                        fait_choix = await ctx.send("`Push for the enchance list : `", components=[button_raw])
                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                        if button_ctx.custom_id == "display":
                                await button_ctx.edit_origin(content=nonetxt)
                                enchance_list = list((st.loadDict("database\EnchancesDatabase.obj")).keys())
                                enchance_embed_list = tf.getListEmbedEnchancesList(ctx,enchance_list)
                                for enchance_embed in enchance_embed_list:
                                        await ctx.send(embed=enchance_embed)
                                await ctx.send("`enchance chose`")
                                try:
                                        string_enchance_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        enchance = str(string_enchance_input.content)
                                        await ctx.send("__enchance : __ `" + enchance + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        enchance = "none"
                        elif button_ctx.custom_id == "not_display":
                                await button_ctx.edit_origin(content=nonetxt)
                                await button_ctx.edit_origin(content=nonetxt)
                                await ctx.send("`enchance chose`")
                                try:
                                        string_enchance_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        enchance = str(string_enchance_input.content)
                                        await ctx.send("__enchance : __ `" + enchance + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        enchance = "none"
                        first_weapon_enchance = st.loadEnchance(enchance)
                        weapon_constructor01 = {"name" : first_weapon_name,
                                                "description": first_weapon_description,
                                                "level": first_weapon_level,
                                                "type" : first_weapon_type ,
                                                "enchance" : first_weapon_enchance,
                                                "enchance_name" : enchance}
                if button_ctx.custom_id == "not_generate":
                        await button_ctx.edit_origin(content=nonetxt)
                        weapon_constructor01 = {"name" : nonetxt,
                                                "description": nonetxt,
                                                "level": 0,
                                                "type" : rp.WeaponTypeClass("none","none") ,
                                                "enchance" : [rp.StatisticsClass("") for x in range(9)],
                                                "enchance_name" : nonetxt}
                await register_type.send("`do you want to generate a new weapon`")
                my_buttons = [create_button(style=ButtonStyle.blue,
                                            label="generate a new weapon",
                                            custom_id="generate"),
                              create_button(style=ButtonStyle.blue,
                                            label="dont generate a new weapon",
                                            custom_id="not_generate")]
                button_raw = create_actionrow(*my_buttons)
                fait_choix = await ctx.send("`Push for generation : `", components=[button_raw])
                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                if button_ctx.custom_id == "generate":
                        await button_ctx.edit_origin(content=nonetxt)
                        await ctx.send("`__enter the name of the 2nd weapon(not the type of the weapon , the name)__`")
                        try:
                                second_weapon_name_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                second_weapon_name = str(second_weapon_name_input.content)
                                await ctx.send("__name of the 2nd weapon : __ `" + second_weapon_name + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                second_weapon_name = nonetxt
                        await ctx.send("`__enter the description of the 2nd weapon__`")
                        try:
                                second_weapon_description_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                second_weapon_description = str(second_weapon_description_input.content)
                                await ctx.send("__descrition of the 2nd weapon : __ `" + second_weapon_description + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                second_weapon_description = nonetxt
                        await ctx.send("`__enter the level of the 2nd weapon__`")
                        try:
                                second_weapon_level_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                second_weapon_level = int(second_weapon_level_input.content)
                                await ctx.send("__level of the 2st weapon : __ `" + str(second_weapon_level) + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                second_weapon_level = 0
                        await ctx.send("`__enter the type of the 2nd weapon__`")
                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                    label="display the equipement-type list",
                                                    custom_id="display"),
                                      create_button(style=ButtonStyle.blue,
                                                    label="not display the equipement-type list",
                                                    custom_id="not_display")]
                        button_raw = create_actionrow(*my_buttons)
                        fait_choix = await ctx.send("`Push for the equipement-type list : `", components=[button_raw])
                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                        if button_ctx.custom_id == "display":
                                await button_ctx.edit_origin(content=nonetxt)
                                equipement_list = list(st.filterEquipementType("weapon_type"))
                                equipement_embed_list = tf.getListEmbedEquipementList(ctx,equipement_list)
                                for equipement_embed in equipement_embed_list:
                                        await ctx.send(embed=equipement_embed)
                                await ctx.send("`equipement chose`")
                                try:
                                        string_equipement_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        equipement_name = str(string_equipement_input.content)
                                        await ctx.send("__equipement-type : __ `" + equipement_name + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        equipement_name = "none"
                        elif button_ctx.custom_id == "not_display":
                                await button_ctx.edit_origin(content=nonetxt)
                                await view_type.send("`equipement-type chose`")
                                try:
                                        string_equipement_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        equipement_name = str(string_equipement_input.content)
                                        await ctx.send("__equipement-type : __ `" + equipement_name + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        equipement_name = "none"
                        second_weapon_type = st.loadEquipement(equipement_name)
                        await ctx.send("`__enter the enchance of the 2nd weapon__`")
                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                    label="display the enchance list",
                                                    custom_id="display"),
                                      create_button(style=ButtonStyle.blue,
                                                    label="not display the enchance list",
                                                    custom_id="not_display")]
                        button_raw = create_actionrow(*my_buttons)
                        fait_choix = await ctx.send("`Push for the enchance list : `", components=[button_raw])
                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                        if button_ctx.custom_id == "display":
                                await button_ctx.edit_origin(content=nonetxt)
                                enchance_list = list((st.loadDict("database\EnchancesDatabase.obj")).keys())
                                enchance_embed_list = tf.getListEmbedEnchancesList(ctx,enchance_list)
                                for enchance_embed in enchance_embed_list:
                                        await ctx.send(embed=enchance_embed)
                                await ctx.send("`enchance chose`")
                                try:
                                        string_enchance_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        enchance = str(string_enchance_input.content)
                                        await ctx.send("__enchance : __ `" + enchance + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        enchance = "none"
                        elif button_ctx.custom_id == "not_display":
                                await button_ctx.edit_origin(content=nonetxt)
                                await button_ctx.edit_origin(content=nonetxt)
                                await ctx.send("`enchance chose`")
                                try:
                                        string_enchance_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        enchance = str(string_enchance_input.content)
                                        await ctx.send("__enchance : __ `" + enchance + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        enchance = "none"
                        second_weapon_enchance = st.loadEnchance(enchance)
                        weapon_constructor02 = {"name" : second_weapon_name,
                                                "description": second_weapon_description,
                                                "level": second_weapon_level,
                                                "type" : second_weapon_type ,
                                                "enchance" : second_weapon_enchance,
                                                "enchance_name" : enchance}
                if button_ctx.custom_id == "not_generate":
                        await button_ctx.edit_origin(content=nonetxt)
                        weapon_constructor02 = {"name" : nonetxt,
                                                "description": nonetxt,
                                                "level": 0,
                                                "type" : rp.WeaponTypeClass("none","none") ,
                                                "enchance" : [rp.StatisticsClass("") for x in range(9)],
                                                "enchance_name" : nonetxt}
                await register_type.send("`do you want to generate a new weapon`")
                my_buttons = [create_button(style=ButtonStyle.blue,
                                            label="generate a new weapon",
                                            custom_id="generate"),
                              create_button(style=ButtonStyle.blue,
                                            label="dont generate a new weapon",
                                            custom_id="not_generate")]
                button_raw = create_actionrow(*my_buttons)
                fait_choix = await ctx.send("`Push for generation : `", components=[button_raw])
                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                if button_ctx.custom_id == "generate":
                        await button_ctx.edit_origin(content=nonetxt)
                        await ctx.send("`__enter the name of the 3st weapon(not the type of the weapon , the name)__`")
                        try:
                                third_weapon_name_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                third_weapon_name = str(third_weapon_name_input.content)
                                await ctx.send("__name of the 3st weapon : __ `" + third_weapon_name + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                third_weapon_name = nonetxt
                        await ctx.send("`__enter the description of the 3st weapon__`")
                        try:
                                third_weapon_description_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                third_weapon_description = str(third_weapon_description_input.content)
                                await ctx.send("__descrition of the 3st weapon : __ `" + third_weapon_description + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                third_weapon_description = nonetxt
                        await ctx.send("`__enter the level of the 3st weapon__`")
                        try:
                                thirs_weapon_level_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                thirs_weapon_level = int(thirs_weapon_level_input.content)
                                await ctx.send("__level of the 3st weapon : __ `" + str(thirs_weapon_level) + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                thirs_weapon_level = 0
                        await ctx.send("`__enter the type of the 3st weapon__`")
                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                    label="display the equipement-type list",
                                                    custom_id="display"),
                                      create_button(style=ButtonStyle.blue,
                                                    label="not display the equipement-type list",
                                                    custom_id="not_display")]
                        button_raw = create_actionrow(*my_buttons)
                        fait_choix = await ctx.send("`Push for the equipement-type list : `", components=[button_raw])
                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                        if button_ctx.custom_id == "display":
                                await button_ctx.edit_origin(content=nonetxt)
                                equipement_list = list(st.filterEquipementType("weapon_type"))
                                equipement_embed_list = tf.getListEmbedEquipementList(ctx,equipement_list)
                                for equipement_embed in equipement_embed_list:
                                        await ctx.send(embed=equipement_embed)
                                await ctx.send("`equipement chose`")
                                try:
                                        string_equipement_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        equipement_name = str(string_equipement_input.content)
                                        await ctx.send("__equipement-type : __ `" + equipement_name + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        equipement_name = "none"
                        elif button_ctx.custom_id == "not_display":
                                await button_ctx.edit_origin(content=nonetxt)
                                await view_type.send("`equipement-type chose`")
                                try:
                                        string_equipement_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        equipement_name = str(string_equipement_input.content)
                                        await ctx.send("__equipement-type : __ `" + equipement_name + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        equipement_name = "none"
                        third_weapon_type = st.loadEquipement(equipement_name)
                        await ctx.send("`__enter the enchance of the 3st weapon__`")
                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                    label="display the enchance list",
                                                    custom_id="display"),
                                      create_button(style=ButtonStyle.blue,
                                                    label="not display the enchance list",
                                                    custom_id="not_display")]
                        button_raw = create_actionrow(*my_buttons)
                        fait_choix = await ctx.send("`Push for the enchance list : `", components=[button_raw])
                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                        if button_ctx.custom_id == "display":
                                await button_ctx.edit_origin(content=nonetxt)
                                enchance_list = list((st.loadDict("database\EnchancesDatabase.obj")).keys())
                                enchance_embed_list = tf.getListEmbedEnchancesList(ctx,enchance_list)
                                for enchance_embed in enchance_embed_list:
                                        await ctx.send(embed=enchance_embed)
                                await ctx.send("`enchance chose`")
                                try:
                                        string_enchance_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        enchance = str(string_enchance_input.content)
                                        await ctx.send("__enchance : __ `" + enchance + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        enchance = "none"
                        elif button_ctx.custom_id == "not_display":
                                await button_ctx.edit_origin(content=nonetxt)
                                await button_ctx.edit_origin(content=nonetxt)
                                await ctx.send("`enchance chose`")
                                try:
                                        string_enchance_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        enchance = str(string_enchance_input.content)
                                        await ctx.send("__enchance : __ `" + enchance + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        enchance = "none"
                        third_weapon_enchance = st.loadEnchance(enchance)
                        weapon_constructor03 = {"name" : third_weapon_name,
                                                "description": third_weapon_description,
                                                "level": third_weapon_level,
                                                "type" : third_weapon_type ,
                                                "enchance" : third_weapon_enchance,
                                                "enchance_name" : enchance}
                if button_ctx.custom_id == "not_generate":
                        await button_ctx.edit_origin(content=nonetxt)
                        weapon_constructor03 = {"name" : nonetxt,
                                                "description": nonetxt,
                                                "level": 0,
                                                "type" : rp.WeaponTypeClass("none","none") ,
                                                "enchance" : [rp.StatisticsClass("") for x in range(9)],
                                                "enchance_name" : nonetxt}    
                await ctx.send(":exclamation: __Vous avez droit d'avoir entre 0 a 2 accessoires.__")
                await register_type.send("`do you want to generate a new accessory`")
                my_buttons = [create_button(style=ButtonStyle.blue,
                                            label="generate a new accessory",
                                            custom_id="generate"),
                              create_button(style=ButtonStyle.blue,
                                            label="dont generate a new accessory",
                                            custom_id="not_generate")]
                button_raw = create_actionrow(*my_buttons)
                fait_choix = await ctx.send("`Push for generation : `", components=[button_raw])
                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                if button_ctx.custom_id == "generate":
                        await button_ctx.edit_origin(content=nonetxt)
                        await ctx.send("`__enter the name of the 1st accessory(not the type of the accessory , the name)__`")
                        try:
                                first_accessory_name_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                first_accessory_name = str(first_accessory_name_input.content)
                                await ctx.send("__name of the 1st accessory : __ `" + first_accessory_name + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                first_accessory_name = nonetxt
                        await ctx.send("`__enter the description of the 1st accessory__`")
                        try:
                                first_accessory_description_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                first_accessory_description = str(first_accessory_description_input.content)
                                await ctx.send("__descrition of the 1st accessory : __ `" + first_accessory_description + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                first_accessory_description = nonetxt
                        await ctx.send("`__enter the level of the 1st accessory__`")
                        try:
                                first_accessory_level_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                first_accessory_level = int(first_accessory_level_input.content)
                                await ctx.send("__level of the 1st accessory : __ `" + str(first_accessory_level) + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                first_accessory_level = 0
                        await ctx.send("`__enter the type of the 1st accessory__`")
                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                    label="display the equipement-type list",
                                                    custom_id="display"),
                                      create_button(style=ButtonStyle.blue,
                                                    label="not display the equipement-type list",
                                                    custom_id="not_display")]
                        button_raw = create_actionrow(*my_buttons)
                        fait_choix = await ctx.send("`Push for the equipement-type list : `", components=[button_raw])
                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                        if button_ctx.custom_id == "display":
                                await button_ctx.edit_origin(content=nonetxt)
                                equipement_list = list(st.filterEquipementType("accessory_type"))
                                equipement_embed_list = tf.getListEmbedEquipementList(ctx,equipement_list)
                                for equipement_embed in equipement_embed_list:
                                        await ctx.send(embed=equipement_embed)
                                await ctx.send("`equipement chose`")
                                try:
                                        string_equipement_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        equipement_name = str(string_equipement_input.content)
                                        await ctx.send("__equipement-type : __ `" + equipement_name + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        equipement_name = "none"
                        elif button_ctx.custom_id == "not_display":
                                await button_ctx.edit_origin(content=nonetxt)
                                await view_type.send("`equipement-type chose`")
                                try:
                                        string_equipement_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        equipement_name = str(string_equipement_input.content)
                                        await ctx.send("__equipement-type : __ `" + equipement_name + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        equipement_name = "none"
                        first_accessory_type = st.loadEquipement(equipement_name)
                        await ctx.send("`__enter the enchance of the 1st accessory__`")
                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                    label="display the enchance list",
                                                    custom_id="display"),
                                      create_button(style=ButtonStyle.blue,
                                                    label="not display the enchance list",
                                                    custom_id="not_display")]
                        button_raw = create_actionrow(*my_buttons)
                        fait_choix = await ctx.send("`Push for the enchance list : `", components=[button_raw])
                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                        if button_ctx.custom_id == "display":
                                await button_ctx.edit_origin(content=nonetxt)
                                enchance_list = list((st.loadDict("database\EnchancesDatabase.obj")).keys())
                                enchance_embed_list = tf.getListEmbedEnchancesList(ctx,enchance_list)
                                for enchance_embed in enchance_embed_list:
                                        await ctx.send(embed=enchance_embed)
                                await ctx.send("`enchance chose`")
                                try:
                                        string_enchance_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        enchance = str(string_enchance_input.content)
                                        await ctx.send("__enchance : __ `" + enchance + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        enchance = "none"
                        elif button_ctx.custom_id == "not_display":
                                await button_ctx.edit_origin(content=nonetxt)
                                await button_ctx.edit_origin(content=nonetxt)
                                await ctx.send("`enchance chose`")
                                try:
                                        string_enchance_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        enchance = str(string_enchance_input.content)
                                        await ctx.send("__enchance : __ `" + enchance + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        enchance = "none"
                        first_accessory_enchance = st.loadEnchance(enchance)
                        accessory_constructor01 = {"name" : first_accessory_name,
                                                   "description": first_accessory_description,
                                                   "level": first_accessory_level,
                                                   "type" : first_accessory_type ,
                                                   "enchance" : first_accessory_enchance,
                                                   "enchance_name" : enchance}
                if button_ctx.custom_id == "not_generate":
                        await button_ctx.edit_origin(content=nonetxt)
                        accessory_constructor01 = {"name" : nonetxt,
                                                   "description": nonetxt,
                                                   "level": 0,
                                                   "type" : rp.AccessoryClassTypeClass("none","none") ,
                                                   "enchance" : [rp.StatisticsClass("") for x in range(9)],
                                                   "enchance_name" : nonetxt}
                await register_type.send("`do you want to generate a new accessory`")
                my_buttons = [create_button(style=ButtonStyle.blue,
                                            label="generate a new accessory",
                                            custom_id="generate"),
                              create_button(style=ButtonStyle.blue,
                                            label="dont generate a new accessory",
                                            custom_id="not_generate")]
                button_raw = create_actionrow(*my_buttons)
                fait_choix = await ctx.send("`Push for generation : `", components=[button_raw])
                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                if button_ctx.custom_id == "generate":
                        await button_ctx.edit_origin(content=nonetxt)
                        await ctx.send("`__enter the name of the 2nd accessory(not the type of the accessory , the name)__`")
                        try:
                                second_accessory_name_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                second_accessory_name = str(second_accessory_name_input.content)
                                await ctx.send("__name of the 2nd accessory : __ `" + second_accessory_name + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                second_accessory_name = nonetxt
                        await ctx.send("`__enter the description of the 2nd accessory__`")
                        try:
                                second_accessory_description_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                second_accessory_description = str(second_accessory_description_input.content)
                                await ctx.send("__descrition of the 2nd accessory : __ `" + second_accessory_description + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                second_accessory_description = nonetxt
                        await ctx.send("`__enter the level of the 2nd accessory__`")
                        try:
                                second_accessory_level_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                second_accessory_level = int(second_accessory_level_input.content)
                                await ctx.send("__level of the 2nd accessory : __ `" + str(second_accessory_level) + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                second_accessory_level = 0
                        await ctx.send("`__enter the type of the 2nd accessory__`")
                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                    label="display the equipement-type list",
                                                    custom_id="display"),
                                      create_button(style=ButtonStyle.blue,
                                                    label="not display the equipement-type list",
                                                    custom_id="not_display")]
                        button_raw = create_actionrow(*my_buttons)
                        fait_choix = await ctx.send("`Push for the equipement-type list : `", components=[button_raw])
                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                        if button_ctx.custom_id == "display":
                                await button_ctx.edit_origin(content=nonetxt)
                                equipement_list = st.filterEquipementType("accessory_type")
                                equipement_embed_list = tf.getListEmbedEquipementList(ctx,equipement_list)
                                for equipement_embed in equipement_embed_list:
                                        await ctx.send(embed=equipement_embed)
                                await ctx.send("`equipement chose`")
                                try:
                                        string_equipement_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        equipement_name = str(string_equipement_input.content)
                                        await ctx.send("__equipement-type : __ `" + equipement_name + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        equipement_name = "none"
                        elif button_ctx.custom_id == "not_display":
                                await button_ctx.edit_origin(content=nonetxt)
                                await view_type.send("`equipement-type chose`")
                                try:
                                        string_equipement_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        equipement_name = str(string_equipement_input.content)
                                        await ctx.send("__equipement-type : __ `" + equipement_name + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        equipement_name = "none"
                        second_accessory_type = st.loadEquipement(equipement_name)
                        await ctx.send("`__enter the enchance of the 2nd accessory__`")
                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                    label="display the enchance list",
                                                    custom_id="display"),
                                      create_button(style=ButtonStyle.blue,
                                                    label="not display the enchance list",
                                                    custom_id="not_display")]
                        button_raw = create_actionrow(*my_buttons)
                        fait_choix = await ctx.send("`Push for the enchance list : `", components=[button_raw])
                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                        if button_ctx.custom_id == "display":
                                await button_ctx.edit_origin(content=nonetxt)
                                enchance_list = list((st.loadDict("database\EnchancesDatabase.obj")).keys())
                                enchance_embed_list = tf.getListEmbedEnchancesList(ctx,enchance_list)
                                for enchance_embed in enchance_embed_list:
                                        await ctx.send(embed=enchance_embed)
                                await ctx.send("`enchance chose`")
                                try:
                                        string_enchance_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        enchance = str(string_enchance_input.content)
                                        await ctx.send("__enchance : __ `" + enchance + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        enchance = "none"
                        elif button_ctx.custom_id == "not_display":
                                await button_ctx.edit_origin(content=nonetxt)
                                await button_ctx.edit_origin(content=nonetxt)
                                await ctx.send("`enchance chose`")
                                try:
                                        string_enchance_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        enchance = str(string_enchance_input.content)
                                        await ctx.send("__enchance : __ `" + enchance + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        enchance = "none"
                        second_accessory_enchance = st.loadEnchance(enchance)
                        accessory_constructor02 = {"name" : second_accessory_name,
                                                   "description": second_accessory_description,
                                                   "level": second_accessory_level,
                                                   "type" : second_accessory_type ,
                                                   "enchance" : second_accessory_enchance,
                                                   "enchance_name" : enchance}
                if button_ctx.custom_id == "not_generate":
                        await button_ctx.edit_origin(content=nonetxt)
                        accessory_constructor02 = {"name" : nonetxt,
                                                   "description": nonetxt,
                                                   "level": 0,
                                                   "type" : rp.AccessoryClassTypeClass("none","none") ,
                                                   "enchance" : [rp.StatisticsClass("") for x in range(9)],
                                                   "enchance_name" : nonetxt}
                await ctx.send(":exclamation: `enregistrement de l'armure`")
                await register_type.send("`do you want to generate a new armor`")
                my_buttons = [create_button(style=ButtonStyle.blue,
                                            label="generate a new armor",
                                            custom_id="generate"),
                              create_button(style=ButtonStyle.blue,
                                            label="dont generate a new armor",
                                            custom_id="not_generate")]
                button_raw = create_actionrow(*my_buttons)
                fait_choix = await ctx.send("`Push for generation : `", components=[button_raw])
                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                if button_ctx.custom_id == "generate":
                        await button_ctx.edit_origin(content=nonetxt)
                        await ctx.send("`__enter the name of the armor(not the type of the armor , the name)__`")
                        try:
                                armor_name_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                armor_name = str(armor_name_input.content)
                                await ctx.send("__name of the armor : __ `" + armor_name + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                armor_name = nonetxt
                        await ctx.send("`__enter the description of the armor__`")
                        try:
                                armor_description_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                armor_description = str(armor_description_input.content)
                                await ctx.send("__descrition of the armor : __ `" + armor_description + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                armor_description = nonetxt
                        await ctx.send("`__enter the level of the armor__`")
                        try:
                                armor_level_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                armor_level = int(armor_level_input.content)
                                await ctx.send("__level of the armor : __ `" + str(armor_level) + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                armor_level = 0
                        await ctx.send("`__enter the type of the armor__`")
                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                    label="display the equipement-type list",
                                                    custom_id="display"),
                                      create_button(style=ButtonStyle.blue,
                                                    label="not display the equipement-type list",
                                                    custom_id="not_display")]
                        button_raw = create_actionrow(*my_buttons)
                        fait_choix = await ctx.send("`Push for the equipement-type list : `", components=[button_raw])
                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                        if button_ctx.custom_id == "display":
                                await button_ctx.edit_origin(content=nonetxt)
                                equipement_list = st.filterEquipementType("armor_type")
                                equipement_embed_list = tf.getListEmbedEquipementList(ctx,equipement_list)
                                for equipement_embed in equipement_embed_list:
                                        await ctx.send(embed=equipement_embed)
                                await ctx.send("`equipement chose`")
                                try:
                                        string_equipement_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        equipement_name = str(string_equipement_input.content)
                                        await ctx.send("__equipement-type : __ `" + equipement_name + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        equipement_name = "none"
                        elif button_ctx.custom_id == "not_display":
                                await button_ctx.edit_origin(content=nonetxt)
                                await view_type.send("`equipement-type chose`")
                                try:
                                        string_equipement_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        equipement_name = str(string_equipement_input.content)
                                        await ctx.send("__equipement-type : __ `" + equipement_name + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        equipement_name = "none"
                        armor_type = st.loadEquipement(equipement_name)
                        await ctx.send("`__enter the enchance of the armor__`")
                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                    label="display the enchance list",
                                                    custom_id="display"),
                                      create_button(style=ButtonStyle.blue,
                                                    label="not display the enchance list",
                                                    custom_id="not_display")]
                        button_raw = create_actionrow(*my_buttons)
                        fait_choix = await ctx.send("`Push for the enchance list : `", components=[button_raw])
                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                        if button_ctx.custom_id == "display":
                                await button_ctx.edit_origin(content=nonetxt)
                                enchance_list = list((st.loadDict("database\EnchancesDatabase.obj")).keys())
                                enchance_embed_list = tf.getListEmbedEnchancesList(ctx,enchance_list)
                                for enchance_embed in enchance_embed_list:
                                        await ctx.send(embed=enchance_embed)
                                await ctx.send("`enchance chose`")
                                try:
                                        string_enchance_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        enchance = str(string_enchance_input.content)
                                        await ctx.send("__enchance : __ `" + enchance + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        enchance = "none"
                        elif button_ctx.custom_id == "not_display":
                                await button_ctx.edit_origin(content=nonetxt)
                                await button_ctx.edit_origin(content=nonetxt)
                                await ctx.send("`enchance chose`")
                                try:
                                        string_enchance_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        enchance = str(string_enchance_input.content)
                                        await ctx.send("__enchance : __ `" + enchance + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        enchance = "none"
                        armor_enchance = st.loadEnchance(enchance)
                        armor_constructor = {"name" : armor_name,
                                             "description": armor_description,
                                             "level": armor_level,
                                             "type" : armor_type ,
                                             "enchance" : armor_enchance,
                                             "enchance_name" : enchance}
                if button_ctx.custom_id == "not_generate":
                        await button_ctx.edit_origin(content=nonetxt)
                        armor_constructor = {"name" : nonetxt,
                                             "description": nonetxt,
                                             "level": 0,
                                             "type" : rp.ArmorClassTypeClass("none","none") ,
                                             "enchance" : [rp.StatisticsClass("") for x in range(9)],
                                             "enchance_name" : nonetxt}


                await ctx.send(":exclamation: `enregistrement de vos connaissances de craft(cela reduit le prix d'achat des items de vos connaissances a 1/8 de leurs prix d'origine)`")
                my_buttons = [create_button(style=ButtonStyle.blue,
                                            label="display the item list",
                                            custom_id="display"),
                              create_button(style=ButtonStyle.blue,
                                            label="not display the item list",
                                            custom_id="not_display")]
                button_raw = create_actionrow(*my_buttons)
                fait_choix = await ctx.send("`Push for the item list : `", components=[button_raw])
                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                if button_ctx.custom_id == "display":
                        await button_ctx.edit_origin(content=nonetxt)
                        item_list = list((st.loadDict(r"database\ItemsDatabase.obj")).keys())
                        item_embed_list = tf.getListItemEmbedImageList(ctx,item_list)
                        for item_embed in item_embed_list:
                                await ctx.send(embed=item_embed)
                        await ctx.send("`item01`|`item02`|.....|`itemN`")
                        try:
                                item_name_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                item_names = str(item_name_input.content)
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                item_names = "none"
                elif button_ctx.custom_id == "not_display":
                        await button_ctx.edit_origin(content=nonetxt)
                        await ctx.send("`item01`|`item02`|.....|`itemN`")
                        try:
                                item_name_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                item_names = str(item_name_input.content)
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                item_names = "none"
                if item_names != "none":
                        knoledge_list = item_names.split("|")
                else:
                        knoledge_list = []
                new_character = rp.CharacterClass(char_name,char_description,char_history,char_nick_name,char_titles,char_background_list,char_allignement,char_max_hp,char_level,char_race,char_classe,rp.StatisticsClass("",attack_template_constructor),weapon_constructor01,weapon_constructor02,weapon_constructor03,accessory_constructor01,accessory_constructor02, armor_constructor,other_statistics_pattern,char_image_path,{},char_capital,char_languages,rp.OrganisationClass("","",0,0),char_organisation,knoledge_list)
                st.saveCharacter(new_character,user_name,display_name)
                display_character = st.loadCharacter(user_name,display_name,char_name)
                first_embed = tf.getFirstEmbedImageCharacter(ctx,display_character)
                second_embed = tf.getSecondEmbedImageCharacter(ctx,display_character)
                await ctx.send(embed=first_embed)
                await ctx.send(embed=second_embed)

                
                pass
        if register_type.values[0] == "item":
                await register_type.send("`__enter the name of the item__`")
                try:
                        item_name_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                        item_name = str(item_name_input.content)
                        await ctx.send("__item name : __`" + item_name + "`")
                except:
                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                        item_name = nonetxt
                await register_type.send("`__enter the description of the item__`")
                try:
                        item_description_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                        item_description = str(item_description_input.content)
                        await ctx.send("__item description : __`" + item_description + "`")
                except:
                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                        item_description = nonetxt
                await register_type.send("`__enter the image url of the item__`")
                try:
                        item_image_path_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                        item_image_path = str(item_image_path_input.content)
                        await ctx.send("register`")
                except:
                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                        item_image_path = "https://cdn.discordapp.com/attachments/1005626886195527720/1005627343999610910/Inconnu.png"
                if item_image_path == "none":
                        item_image_path = "https://cdn.discordapp.com/attachments/1005626886195527720/1005627343999610910/Inconnu.png"
                await register_type.send("`__enter the price of the item__`")
                try:
                        item_price_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                        item_price = int(item_price_input.content)
                        await ctx.send("register`")
                except:
                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                        item_price = 0
                consummable_select = tf.getListSelection(ctx,"it is cosummable ?",["not consummable","consummable","magic consummable","magic item"],["not consummable","consummable","magic consummable","magic item"]) 
                fait_choix = await ctx.send("`it is cosummable ? : `", components=[create_actionrow(consummable_select)])
                isconsummable = await wait_for_component(notlolabot.bot, components=consummable_select, check=check)
                await isconsummable.send(nonetxt)
                if isconsummable.values[0] == "consummable":
                        consummable_life_select = tf.getListSelection(ctx,"chose life regen",[str(x) for x in range(21)],[str(x) for x in range(21)]) 
                        fait_choix = await ctx.send("`chose life regen : `", components=[create_actionrow(consummable_life_select)])
                        consummable_life = await wait_for_component(notlolabot.bot, components=consummable_life_select, check=check)
                        await consummable_life.send(nonetxt)
                        new_item = rp.ConsumableClass(item_name,item_description,int(consummable_life.values[0]),item_image_path,1,item_price)
                if isconsummable.values[0] == "magic consummable":
                        consummable_life_select = tf.getListSelection(ctx,"chose life regen",[str(x) for x in range(21)],[str(x) for x in range(21)]) 
                        fait_choix = await ctx.send("`chose life regen : `", components=[create_actionrow(consummable_life_select)])
                        consummable_life = await wait_for_component(notlolabot.bot, components=consummable_life_select, check=check)

                        await modifier_select_aux.send("`__enter the list of the competences__`")
                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                    label="display the skill list",
                                                    custom_id="display"),
                                      create_button(style=ButtonStyle.blue,
                                                    label="not display the skill list",
                                                    custom_id="not_display")]
                        button_raw = create_actionrow(*my_buttons)
                        fait_choix = await ctx.send("`Push for the skill list : `", components=[button_raw])
                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                        if button_ctx.custom_id == "display":
                                await button_ctx.edit_origin(content=nonetxt)
                                skill_list = st.filterCompetences(["transversal_attack","mouvement_skill","massiv_skill"])
                                skill_embed_list = tf.getListEmbedSkillsList(ctx,skill_list,"weapon attack")
                                for skill_embed in skill_embed_list:
                                        await ctx.send(embed=skill_embed)
                                await modifier_select_aux.send("`enter the skill name : `")
                                try:
                                        skill_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        skill_name = str(skill_input.content)
                                        await ctx.send("__skill name : __ `" + skill_name + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        skill_name = "none"
                                if skill_name != "none":
                                        competence = st.loadCompetence(skill_name)
                                else:
                                        competence = rp.CompetenceClass("","",("","") ,0,("",0),0)
                        if button_ctx.custom_id == "not_display":
                                await button_ctx.edit_origin(content=nonetxt)
                                await modifier_select_aux.send("`enter the skill name : `")
                                try:
                                        skill_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        skill_name = str(skill_input.content)
                                        await ctx.send("__skill name : __ `" + skill_name + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        skill_name = "none"
                                if skill_name != "none":
                                        competence = st.loadCompetence(skill_name)
                                else:
                                        competence = rp.CompetenceClass("","",("","") ,0,("",0),0)

                        
                        await consummable_life.send(nonetxt)
                        new_item = rp.MagicalConsumableClass(item_name,item_description,int(consummable_life.values[0]),competence,item_image_path,1,item_price)
                if isconsummable.values[0] == "not consummable":
                        new_item = rp.NewItemClass(item_name,item_description,item_image_path,1,item_price)
                if isconsummable.values[0] == "magic item":
                        await modifier_select_aux.send("`__enter the list of the competences__`")
                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                    label="display the skill list",
                                                    custom_id="display"),
                                      create_button(style=ButtonStyle.blue,
                                                    label="not display the skill list",
                                                    custom_id="not_display")]
                        button_raw = create_actionrow(*my_buttons)
                        fait_choix = await ctx.send("`Push for the skill list : `", components=[button_raw])
                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                        if button_ctx.custom_id == "display":
                                await button_ctx.edit_origin(content=nonetxt)
                                skill_list = st.filterCompetences(["transversal_attack","mouvement_skill","massiv_skill"])
                                skill_embed_list = tf.getListEmbedSkillsList(ctx,skill_list,"weapon attack")
                                for skill_embed in skill_embed_list:
                                        await ctx.send(embed=skill_embed)
                                await modifier_select_aux.send("`enter the skill name : `")
                                try:
                                        skill_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        skill_name = str(skill_input.content)
                                        await ctx.send("__skill name : __ `" + skill_name + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        skill_name = "none"
                                if skill_name != "none":
                                        competence = st.loadCompetence(skill_name)
                                else:
                                        competence = rp.CompetenceClass("","",("","") ,0,("",0),0)
                        if button_ctx.custom_id == "not_display":
                                await button_ctx.edit_origin(content=nonetxt)
                                await modifier_select_aux.send("`enter the skill name : `")
                                try:
                                        skill_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        skill_name = str(skill_input.content)
                                        await ctx.send("__skill name : __ `" + skill_name + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        skill_name = "none"
                                if skill_name != "none":
                                        competence = st.loadCompetence(skill_name)
                                else:
                                        competence = rp.CompetenceClass("","",("","") ,0,("",0),0)
                        new_item = rp.MagicalItemClass(item_name,item_description,competence,item_image_path,1,item_price)
                st.saveItem(new_item)
                display_item = st.loadItem(item_name)
                my_embed = tf.getEmbedImageItem(ctx,display_item)
                await ctx.send(embed=my_embed)
                pass
        if register_type.values[0] == "archetype":
                await register_type.send("`__enter the name of the character__`")
                try:
                        char_name_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                        char_name = str(char_name_input.content)
                        await ctx.send("__name of the character : __ `" + char_name + "`")
                except:
                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                        char_name = "none"
                await register_type.send("`__enter the physical description of the character__`")
                try:
                        char_description_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                        char_description = str(char_description_input.content)
                        await ctx.send("__physical description of the character : __ `" + char_description + "`")
                except:
                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                        char_description = nonetxt
                await register_type.send("`__enter the image url of the character__`")
                try:
                        char_image_path_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                        char_image_path = str(char_image_path_input.content)
                        await ctx.send("` image load`")
                except:
                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                        char_image_path = ctx.author.avatar_url
                if char_image_path == "none":
                        char_image_path = ctx.author.avatar_url
                await register_type.send("`__enter the nickname of the character (if your character dont have a nickname writte 'none')__`")
                try:
                        char_nick_name_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                        char_nick_name = str(char_nick_name_input.content)
                        await ctx.send("__nickname of the character : __ `" + char_nick_name + "`")
                except:
                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                        char_nick_name = nonetxt
                if char_nick_name == "none":
                        char_nick_name = nonetxt
                await register_type.send("`__enter the history of the character__`")
                try:
                        char_history_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                        if char_history_input.attachments != [] and char_history_input.attachments[0].filename.endswith(".txt"):
                                await char_history_input.attachments[0].save(r"files_saves\file_" + char_history_input.attachments[0].filename)
                                file = open(r"files_saves\file_" + char_history_input.attachments[0].filename,"r")
                                char_history = file.read()
                                file.close()
                        else:
                                char_history = str(char_history_input.content)
                        await ctx.send("`lore load`")
                except:
                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                        char_history = nonetxt
                await register_type.send("`__enter the titles of the character(like master of the mercenary guild)(if your character dont have titles writte 'none')__`")
                await ctx.send("title01|title02|.......|title0n")
                try:
                        char_titles_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                        if char_titles_input.content == "none":
                                char_titles = []
                        else:
                                char_titles = (str(char_titles_input.content)).split("|")
                        await ctx.send("`titles load`")
                except:
                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                        char_tiles = []
                await register_type.send("`__enter the languages of the character__`")
                await ctx.send("language01|language02|.......|language0n")
                try:
                        char_languages_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                        if char_languages_input.content == "none":
                                char_languages = []
                        else:
                                char_languages = (str(char_languages_input.content)).split("|")
                        await ctx.send("`languages load`")
                except:
                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                        char_languages = []
                backgrounds_list = ["soldat","guerrier","mercenaire","officier","vaguabon","noble","espion","assassin","escroc","voleur","sorcier","academiste","acolyte",
                                    "esclave","mage","maitre d'arme","inspincteur","truand","chercheur","habitant des forets","bourgeois","experience ratée"]
                char_background_selection = tf.getListSelection(ctx,"chose the background",backgrounds_list,backgrounds_list,1,4)
                fait_choix = await register_type.send("`Chose the background : `", components=[create_actionrow(char_background_selection)])
                char_background_aux = await wait_for_component(notlolabot.bot, components=char_background_selection, check=check)
                await char_background_aux.send(nonetxt)
                char_background_list = char_background_aux.values
                allignement_list = ["loyal bon","neutre bon","chaotique bon","loyal neutre","neutre","chaotique neutre","loyal mauvais","neutre mauvais","chaotique mauvais"]
                char_allignement_selection = tf.getListSelection(ctx,"chose the allignement",allignement_list,allignement_list)
                fait_choix = await register_type.send("`Chose the allignement : `", components=[create_actionrow(char_allignement_selection)])
                char_allignement_aux = await wait_for_component(notlolabot.bot, components=char_allignement_selection, check=check)
                await char_allignement_aux.send(nonetxt)
                char_allignement = char_allignement_aux.values[0]
                await register_type.send("`__enter the capital in gold piece of the character__`")
                try:
                        char_capital_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                        char_capital = int(str(char_capital_input.content))
                        await ctx.send("__capital of the character : __ `" + str(char_capital) + " golds`")
                except:
                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                        char_capital = 10
                await register_type.send("`__enter the level of the character__`")
                try:
                        char_level_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                        char_level = int(str(char_level_input.content))
                        await ctx.send("__level of the character : __ `" + str(char_level) + "`")
                except:
                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                        char_level = 1




                await register_type.send("`__enter the max hp of the archetype__`")
                try:
                        char_max_hp_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                        char_max_hp = int(str(char_max_hp_input.content))
                        await ctx.send("__max hp of the archetype : __ `" + str(char_max_hp) + "`")
                except:
                        await ctx.send("`Erreur sur la commande valeure de base fixée a 100hp , si cela ne vous convient pas , veuillez reiterer la commande.`")
                        char_max_hp = 100





                
                await register_type.send("`__enter the race name of the character__`")
                my_buttons = [create_button(style=ButtonStyle.blue,
                                            label="display the race list",
                                            custom_id="display"),
                              create_button(style=ButtonStyle.blue,
                                            label="not display the race list",
                                            custom_id="not_display")]
                button_raw = create_actionrow(*my_buttons)
                fait_choix = await ctx.send("`Push for the race list : `", components=[button_raw])
                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                if button_ctx.custom_id == "display":
                        await button_ctx.edit_origin(content=nonetxt)
                        race_list = list((st.loadDict("database\RacesDatabase.obj")).keys())
                        race_embed_list = tf.getListEmbedRaceList(ctx,race_list)
                        for race_embed in race_embed_list:
                                await ctx.send(embed=race_embed)
                        await register_type.send("`race chose`")
                        try:
                                string_race_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                race_name = str(string_race_input.content)
                                await ctx.send("__race : __ `" + race_name + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                race_name = "none"
                elif button_ctx.custom_id == "not_display":
                        await button_ctx.edit_origin(content=nonetxt)
                        await register_type.send("`race chose`")
                        try:
                                string_race_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                race_name = str(string_race_input.content)
                                await ctx.send("__race : __ `" + race_name + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                race_name = "none"
                if race_name != "none":
                        char_race = st.loadRace(race_name)
                else:
                        char_race = rp.RaceClass("","","",{})
                await register_type.send("`__enter the classe name of the character(enter none if your archetype dont have a class)__`")
                my_buttons = [create_button(style=ButtonStyle.blue,
                                            label="display the classe list",
                                            custom_id="display"),
                              create_button(style=ButtonStyle.blue,
                                            label="not display the classe list",
                                            custom_id="not_display")]
                button_raw = create_actionrow(*my_buttons)
                fait_choix = await ctx.send("`Push for the classe list : `", components=[button_raw])
                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                if button_ctx.custom_id == "display":
                        await button_ctx.edit_origin(content=nonetxt)
                        classe_list = list((st.loadDict("database\ClassDatabase.obj")).keys())
                        classe_embed_list = tf.getListEmbedClasseList(ctx,classe_list)
                        for classe_embed in classe_embed_list:
                                await ctx.send(embed=classe_embed)
                        await register_type.send("`classe chose`")
                        try:
                                string_classe_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                classe_name = str(string_classe_input.content)
                                await ctx.send("__classe : __ `" + classe_name + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                classe_name = "none"
                elif button_ctx.custom_id == "not_display":
                        await button_ctx.edit_origin(content=nonetxt)
                        await register_type.send("`classe chose`")
                        try:
                                string_classe_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                classe_name = str(string_classe_input.content)
                                await ctx.send("__classe : __ `" + classe_name + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                classe_name = "none"
                if classe_name != "none":
                        char_classe = st.loadClasse(classe_name)
                else:
                        char_classe = rp.ClasseClass("","","",{},"")
                await register_type.send("`__enter the organisation name of the character(if your character dont have a organisation writte 'none')__`")
                my_buttons = [create_button(style=ButtonStyle.blue,
                                            label="display the organisation list",
                                            custom_id="display"),
                              create_button(style=ButtonStyle.blue,
                                            label="not display the organisation list",
                                            custom_id="not_display")]
                button_raw = create_actionrow(*my_buttons)
                fait_choix = await ctx.send("`Push for the organisation list : `", components=[button_raw])
                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                if button_ctx.custom_id == "display":
                        await button_ctx.edit_origin(content=nonetxt)
                        organisation_list = list((st.loadDict("database\OrganisationsDatabase.obj")).keys())
                        organisation_embed_list = tf.getListEmbedOrganisationList(ctx,organisation_list)
                        for organisation_embed in organisation_embed_list:
                                await ctx.send(embed=organisation_embed)
                        await register_type.send("`organisation chose`")
                        try:
                                string_organisation_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                organisation_name = str(string_organisation_input.content)
                                await ctx.send("__Organisation : __ `" + organisation_name + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                organisation_name = "none"
                elif button_ctx.custom_id == "not_display":
                        await button_ctx.edit_origin(content=nonetxt)
                        await register_type.send("`Organisation chose`")
                        try:
                                string_organisation_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                organisation_name = str(string_organisation_input.content)
                                await ctx.send("__Organisation : __ `" + organisation_name + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                organisation_name = "none"
                if organisation_name != "none":
                        char_organisation = st.loadOrganisation(organisation_name)
                else:
                        char_organisation = rp.OrganisationClass("","",0,0,rp.StatisticsClass(""),"")
                await ctx.send(":exclamation: __Ne vous trompez pas sur les valeurs que vous voulez choisir , car il faudra recommencé la creation du personnage!.__")
                attack_dice_select = tf.getListSelection(ctx,"chose the bonus damage dice of the character",[str(x) for x in range(15)],[str(x) for x in range(15)])
                fait_choix = await register_type.send("`chose the bonus damage dice of the character : `", components=[create_actionrow(attack_dice_select)])
                attack_dice_aux = await wait_for_component(notlolabot.bot, components=attack_dice_select, check=check)
                attack_constent_select = tf.getListSelection(ctx,"chose the damage bonus of the character",[str(x) for x in range(5)],[str(x) for x in range(5)])
                fait_choix = await attack_dice_aux.send("`chose the damage bonus of the character : `", components=[create_actionrow(attack_constent_select)])
                attack_constent_aux = await wait_for_component(notlolabot.bot, components=attack_constent_select, check=check)
                dexterity_dice_select = tf.getListSelection(ctx,"chose the bonus dexterity dice of the character",[str(x) for x in range(15)],[str(x) for x in range(15)])
                fait_choix = await attack_constent_aux.send("`chose the bonus dexterity dice of the character : `", components=[create_actionrow(dexterity_dice_select)])
                dexterity_dice_aux = await wait_for_component(notlolabot.bot, components=dexterity_dice_select, check=check)
                dexterity_constent_select = tf.getListSelection(ctx,"chose the dexterity bonus of the character",[str(x) for x in range(5)],[str(x) for x in range(5)])
                fait_choix = await dexterity_dice_aux.send("`chose the dexterity bonus of the character : `", components=[create_actionrow(dexterity_constent_select)])
                dexterity_constent_aux = await wait_for_component(notlolabot.bot, components=dexterity_constent_select, check=check)
                bleeding_dice_select = tf.getListSelection(ctx,"chose the bonus bleeding dice of the character",[str(x) for x in range(15)],[str(x) for x in range(15)])
                fait_choix = await dexterity_constent_aux.send("`chose the bonus bleeding dice of the character : `", components=[create_actionrow(bleeding_dice_select)])
                bleeding_dice_aux = await wait_for_component(notlolabot.bot, components=bleeding_dice_select, check=check)
                bleeding_constent_select = tf.getListSelection(ctx,"chose the bonus bleeding of the character",[str(x) for x in range(5)],[str(x) for x in range(5)])
                fait_choix = await bleeding_dice_aux.send("`chose the bonus bleeding of the character : `", components=[create_actionrow(bleeding_constent_select)])
                bleeding_constent_aux = await wait_for_component(notlolabot.bot, components=bleeding_constent_select, check=check)
                posture_dice_select = tf.getListSelection(ctx,"chose the bonus posture dice of the character",[str(x) for x in range(15)],[str(x) for x in range(15)])
                fait_choix = await bleeding_constent_aux.send("`chose the bonus posture dice of the character : `", components=[create_actionrow(posture_dice_select)])
                posture_dice_aux = await wait_for_component(notlolabot.bot, components=posture_dice_select, check=check)
                posture_constent_select = tf.getListSelection(ctx,"chose the posture bonus of the character",[str(x) for x in range(5)],[str(x) for x in range(5)])
                fait_choix = await posture_dice_aux.send("`chose the posture bonus of the character : `", components=[create_actionrow(posture_constent_select)])
                posture_constent_aux = await wait_for_component(notlolabot.bot, components=posture_constent_select, check=check)
                constitution_dice_select = tf.getListSelection(ctx,"chose the bonus constitution dice of the character",[str(x) for x in range(15)],[str(x) for x in range(15)])
                fait_choix = await posture_constent_aux.send("`chose the bonus constitution dice of the character : `", components=[create_actionrow(constitution_dice_select)])
                constitution_dice_aux = await wait_for_component(notlolabot.bot, components=constitution_dice_select, check=check)
                constitution_constent_select = tf.getListSelection(ctx,"chose the constitution bonus of the character",[str(x) for x in range(5)],[str(x) for x in range(5)])
                fait_choix = await constitution_dice_aux.send("`chose the constitution bonus of the character : `", components=[create_actionrow(constitution_constent_select)])
                constitution_constent_aux = await wait_for_component(notlolabot.bot, components=constitution_constent_select, check=check)
                evasion_dice_select = tf.getListSelection(ctx,"chose the bonus evasion dice of the character",[str(x) for x in range(15)],[str(x) for x in range(15)])
                fait_choix = await constitution_constent_aux.send("`chose the bonus evasion dice of the character : `", components=[create_actionrow(evasion_dice_select)])
                evasion_dice_aux = await wait_for_component(notlolabot.bot, components=evasion_dice_select, check=check)
                evasion_constent_select = tf.getListSelection(ctx,"chose the evasion bonus of the character",[str(x) for x in range(5)],[str(x) for x in range(5)])
                fait_choix = await evasion_dice_aux.send("`chose the evasion bonus of the character : `", components=[create_actionrow(evasion_constent_select)])
                evasion_constent_aux = await wait_for_component(notlolabot.bot, components=evasion_constent_select, check=check)
                intellect_dice_select = tf.getListSelection(ctx,"chose the bonus intellect dice of the character",[str(x) for x in range(15)],[str(x) for x in range(15)])
                fait_choix = await evasion_constent_aux.send("`chose the bonus intellect dice of the character : `", components=[create_actionrow(intellect_dice_select)])
                intellect_dice_aux = await wait_for_component(notlolabot.bot, components=intellect_dice_select, check=check)
                intellect_constent_select = tf.getListSelection(ctx,"chose the intellect bonus of the character",[str(x) for x in range(5)],[str(x) for x in range(5)])
                fait_choix = await intellect_dice_aux.send("`chose the intellect bonus of the character : `", components=[create_actionrow(intellect_constent_select)])
                intellect_constent_aux = await wait_for_component(notlolabot.bot, components=intellect_constent_select, check=check)
                charisma_dice_select = tf.getListSelection(ctx,"chose the bonus charisma dice of the character",[str(x) for x in range(15)],[str(x) for x in range(15)])
                fait_choix = await intellect_constent_aux.send("`chose the bonus charisma dice of the character : `", components=[create_actionrow(charisma_dice_select)])
                charisma_dice_aux = await wait_for_component(notlolabot.bot, components=charisma_dice_select, check=check)
                charisma_constent_select = tf.getListSelection(ctx,"chose the charisma bonus of the character",[str(x) for x in range(5)],[str(x) for x in range(5)])
                fait_choix = await charisma_dice_aux.send("`chose the charisma bonus of the character : `", components=[create_actionrow(charisma_constent_select)])
                charisma_constent_aux = await wait_for_component(notlolabot.bot, components=charisma_constent_select, check=check)
                wisdom_dice_select = tf.getListSelection(ctx,"chose the bonus wisdom dice of the character",[str(x) for x in range(15)],[str(x) for x in range(15)])
                fait_choix = await charisma_constent_aux.send("`chose the bonus wisdom dice of the character : `", components=[create_actionrow(wisdom_dice_select)])
                wisdom_dice_aux = await wait_for_component(notlolabot.bot, components=wisdom_dice_select, check=check)
                wisdom_constent_select = tf.getListSelection(ctx,"chose the wisdom bonus of the character",[str(x) for x in range(5)],[str(x) for x in range(5)])
                fait_choix = await wisdom_dice_aux.send("`chose the wisdom bonus of the character : `", components=[create_actionrow(wisdom_constent_select)])
                wisdom_constent_aux = await wait_for_component(notlolabot.bot, components=wisdom_constent_select, check=check)                
                await wisdom_constent_aux.send(nonetxt)
                attack_template_constructor = {"strength" : (int(attack_dice_aux.values[0]),int(attack_dice_aux.values[0])),
                                               "dexterity" : (int(dexterity_dice_aux.values[0]),int(dexterity_constent_aux.values[0])),
                                               "bleeding" : (int(bleeding_dice_aux.values[0]),int(bleeding_constent_aux.values[0])) ,
                                               "posture" : (int(posture_dice_aux.values[0]),int(posture_constent_aux.values[0])) ,
                                               "constitution" : (int(constitution_dice_aux.values[0]),int(constitution_constent_aux.values[0])),
                                               "evasion" : (int(evasion_dice_aux.values[0]),int(evasion_constent_aux.values[0])),
                                               "intellect" : (int(intellect_dice_aux.values[0]),int(intellect_constent_aux.values[0])),
                                               "charisma" : (int(charisma_dice_aux.values[0]),int(charisma_constent_aux.values[0])) ,
                                               "wisdom" : (int(wisdom_dice_aux.values[0]),int(wisdom_constent_aux.values[0]))}
                arcanes_select = tf.getListSelection(ctx,"chose the arcanes value of the character",[str(x) for x in range(21)],[str(x) for x in range(21)])
                fait_choix = await register_type.send("`chose the arcanes value of the character : `", components=[create_actionrow(arcanes_select)])
                arcanes_aux = await wait_for_component(notlolabot.bot, components=arcanes_select, check=check)
                athletism_select = tf.getListSelection(ctx,"chose the athletism value of the character",[str(x) for x in range(21)],[str(x) for x in range(21)])
                fait_choix = await arcanes_aux.send("`chose the athletism value of the character : `", components=[create_actionrow(athletism_select)])
                athletism_aux = await wait_for_component(notlolabot.bot, components=athletism_select, check=check)
                discretion_select = tf.getListSelection(ctx,"chose the discretion value of the character",[str(x) for x in range(21)],[str(x) for x in range(21)])
                fait_choix = await athletism_aux.send("`chose the discretion value of the character : `", components=[create_actionrow(discretion_select)])
                discretion_aux = await wait_for_component(notlolabot.bot, components=discretion_select, check=check)
                history_select = tf.getListSelection(ctx,"chose the history value of the character",[str(x) for x in range(21)],[str(x) for x in range(21)])
                fait_choix = await discretion_aux.send("`chose the history value of the character : `", components=[create_actionrow(history_select)])
                history_aux = await wait_for_component(notlolabot.bot, components=history_select, check=check)
                intimidation_select = tf.getListSelection(ctx,"chose the intimidation value of the character",[str(x) for x in range(21)],[str(x) for x in range(21)])
                fait_choix = await history_aux.send("`chose the intimidation value of the character : `", components=[create_actionrow(intimidation_select)])
                intimidation_aux = await wait_for_component(notlolabot.bot, components=intimidation_select, check=check)
                investigation_select = tf.getListSelection(ctx,"chose the investigation value of the character",[str(x) for x in range(21)],[str(x) for x in range(21)])
                fait_choix = await intimidation_aux.send("`chose the investigation value of the character : `", components=[create_actionrow(investigation_select)])
                investigation_aux = await wait_for_component(notlolabot.bot, components=investigation_select, check=check)
                medicine_select = tf.getListSelection(ctx,"chose the medicine value of the character",[str(x) for x in range(21)],[str(x) for x in range(21)])
                fait_choix = await investigation_aux.send("`chose the medicine value of the character : `", components=[create_actionrow(medicine_select)])
                medicine_aux = await wait_for_component(notlolabot.bot, components=medicine_select, check=check)
                religion_select = tf.getListSelection(ctx,"chose the religion value of the character",[str(x) for x in range(21)],[str(x) for x in range(21)])
                fait_choix = await medicine_aux.send("`chose the religion value of the character : `", components=[create_actionrow(religion_select)])
                religion_aux = await wait_for_component(notlolabot.bot, components=religion_select, check=check)
                survive_select = tf.getListSelection(ctx,"chose the survive value of the character",[str(x) for x in range(21)],[str(x) for x in range(21)])
                fait_choix = await religion_aux.send("`chose the survive value of the character : `", components=[create_actionrow(survive_select)])
                survive_aux = await wait_for_component(notlolabot.bot, components=survive_select, check=check)
                occultism_select = tf.getListSelection(ctx,"chose the occultism value of the character",[str(x) for x in range(21)],[str(x) for x in range(21)])
                fait_choix = await survive_aux.send("`chose the occultism value of the character : `", components=[create_actionrow(occultism_select)])
                occultism_aux = await wait_for_component(notlolabot.bot, components=occultism_select, check=check)
                calm_select = tf.getListSelection(ctx,"chose the calm value of the character",[str(x) for x in range(21)],[str(x) for x in range(21)])
                fait_choix = await occultism_aux.send("`chose the calm value of the character : `", components=[create_actionrow(calm_select)])
                calm_aux = await wait_for_component(notlolabot.bot, components=calm_select, check=check)
                await calm_aux.send(nonetxt)
                other_statistics_pattern = {"arcanes" : int(arcanes_aux.values[0]),
                                            "athletics" : int(athletism_aux.values[0]),
                                            "discretion" : int(discretion_aux.values[0]),
                                            "history" : int(history_aux.values[0]),
                                            "intimidation" : int(intimidation_aux.values[0]),
                                            "investigation" : int(investigation_aux.values[0]),
                                            "medicine" : int(medicine_aux.values[0]),
                                            "religion" : int(religion_aux.values[0]),
                                            "survive" : int(survive_aux.values[0]),
                                            "occultism" : int(occultism_aux.values[0]),
                                            "calm" : int(calm_aux.values[0])}
                await ctx.send(":exclamation: __Vous avez droit d'avoir entre 0 a 3 armes maximum.__")
                await ctx.send(":exclamation: __Soyez rp , un lanceur de sorts pure et dure , ne maitrise pas 3 types d'armes.__")
                await ctx.send(":exclamation: `Pour des raisons d'equilibrage , si votre personnage lance beaucoup de sorts , veuillez vous limité a un nombre d'armes variant de 0 a 2 armes(donc en moyenne 1).`")
                await register_type.send("`do you want to generate a new weapon`")
                my_buttons = [create_button(style=ButtonStyle.blue,
                                            label="generate a new weapon",
                                            custom_id="generate"),
                              create_button(style=ButtonStyle.blue,
                                            label="dont generate a new weapon",
                                            custom_id="not_generate")]
                button_raw = create_actionrow(*my_buttons)
                fait_choix = await ctx.send("`Push for generation : `", components=[button_raw])
                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                if button_ctx.custom_id == "generate":
                        await button_ctx.edit_origin(content=nonetxt)
                        await ctx.send("`__enter the name of the 1st weapon(not the type of the weapon , the name)__`")
                        try:
                                first_weapon_name_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                first_weapon_name = str(first_weapon_name_input.content)
                                await ctx.send("__name of the 1st weapon : __ `" + first_weapon_name + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                first_weapon_name = nonetxt
                        await ctx.send("`__enter the description of the 1st weapon__`")
                        try:
                                first_weapon_description_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                first_weapon_description = str(first_weapon_description_input.content)
                                await ctx.send("__descrition of the 1st weapon : __ `" + first_weapon_description + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                first_weapon_description = nonetxt
                        await ctx.send("`__enter the level of the 1st weapon__`")
                        try:
                                first_weapon_level_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                first_weapon_level = int(first_weapon_level_input.content)
                                await ctx.send("__level of the 1st weapon : __ `" + str(first_weapon_level) + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                first_weapon_level = 0
                        await ctx.send("`__enter the type of the 1st weapon__`")
                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                    label="display the equipement-type list",
                                                    custom_id="display"),
                                      create_button(style=ButtonStyle.blue,
                                                    label="not display the equipement-type list",
                                                    custom_id="not_display")]
                        button_raw = create_actionrow(*my_buttons)
                        fait_choix = await ctx.send("`Push for the equipement-type list : `", components=[button_raw])
                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                        if button_ctx.custom_id == "display":
                                await button_ctx.edit_origin(content=nonetxt)
                                equipement_list = st.filterEquipementType("weapon_type")
                                equipement_embed_list = tf.getListEmbedEquipementList(ctx,equipement_list)
                                for equipement_embed in equipement_embed_list:
                                        await ctx.send(embed=equipement_embed)
                                await ctx.send("`equipement chose`")
                                try:
                                        string_equipement_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        equipement_name = str(string_equipement_input.content)
                                        await ctx.send("__equipement-type : __ `" + equipement_name + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        equipement_name = "none"
                        elif button_ctx.custom_id == "not_display":
                                await button_ctx.edit_origin(content=nonetxt)
                                await view_type.send("`equipement-type chose`")
                                try:
                                        string_equipement_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        equipement_name = str(string_equipement_input.content)
                                        await ctx.send("__equipement-type : __ `" + equipement_name + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        equipement_name = "none"
                        first_weapon_type = st.loadEquipement(equipement_name)
                        await ctx.send("`__enter the enchance of the 1st weapon__`")
                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                    label="display the enchance list",
                                                    custom_id="display"),
                                      create_button(style=ButtonStyle.blue,
                                                    label="not display the enchance list",
                                                    custom_id="not_display")]
                        button_raw = create_actionrow(*my_buttons)
                        fait_choix = await ctx.send("`Push for the enchance list : `", components=[button_raw])
                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                        if button_ctx.custom_id == "display":
                                await button_ctx.edit_origin(content=nonetxt)
                                enchance_list = list((st.loadDict("database\EnchancesDatabase.obj")).keys())
                                enchance_embed_list = tf.getListEmbedEnchancesList(ctx,enchance_list)
                                for enchance_embed in enchance_embed_list:
                                        await ctx.send(embed=enchance_embed)
                                await ctx.send("`enchance chose`")
                                try:
                                        string_enchance_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        enchance = str(string_enchance_input.content)
                                        await ctx.send("__enchance : __ `" + enchance + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        enchance = "none"
                        elif button_ctx.custom_id == "not_display":
                                await button_ctx.edit_origin(content=nonetxt)
                                await button_ctx.edit_origin(content=nonetxt)
                                await ctx.send("`enchance chose`")
                                try:
                                        string_enchance_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        enchance = str(string_enchance_input.content)
                                        await ctx.send("__enchance : __ `" + enchance + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        enchance = "none"
                        first_weapon_enchance = st.loadEnchance(enchance)
                        weapon_constructor01 = {"name" : first_weapon_name,
                                                "description": first_weapon_description,
                                                "level": first_weapon_level,
                                                "type" : first_weapon_type ,
                                                "enchance" : first_weapon_enchance,
                                                "enchance_name" : enchance}
                if button_ctx.custom_id == "not_generate":
                        await button_ctx.edit_origin(content=nonetxt)
                        weapon_constructor01 = {"name" : nonetxt,
                                                "description": nonetxt,
                                                "level": 0,
                                                "type" : rp.WeaponTypeClass("none","none") ,
                                                "enchance" : [rp.StatisticsClass("") for x in range(9)],
                                                "enchance_name" : nonetxt}
                await register_type.send("`do you want to generate a new weapon`")
                my_buttons = [create_button(style=ButtonStyle.blue,
                                            label="generate a new weapon",
                                            custom_id="generate"),
                              create_button(style=ButtonStyle.blue,
                                            label="dont generate a new weapon",
                                            custom_id="not_generate")]
                button_raw = create_actionrow(*my_buttons)
                fait_choix = await ctx.send("`Push for generation : `", components=[button_raw])
                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                if button_ctx.custom_id == "generate":
                        await button_ctx.edit_origin(content=nonetxt)
                        await ctx.send("`__enter the name of the 2nd weapon(not the type of the weapon , the name)__`")
                        try:
                                second_weapon_name_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                second_weapon_name = str(second_weapon_name_input.content)
                                await ctx.send("__name of the 2nd weapon : __ `" + second_weapon_name + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                second_weapon_name = nonetxt
                        await ctx.send("`__enter the description of the 2nd weapon__`")
                        try:
                                second_weapon_description_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                second_weapon_description = str(second_weapon_description_input.content)
                                await ctx.send("__descrition of the 2nd weapon : __ `" + second_weapon_description + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                second_weapon_description = nonetxt
                        await ctx.send("`__enter the level of the 2nd weapon__`")
                        try:
                                second_weapon_level_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                second_weapon_level = int(second_weapon_level_input.content)
                                await ctx.send("__level of the 2st weapon : __ `" + str(second_weapon_level) + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                second_weapon_level = 0
                        await ctx.send("`__enter the type of the 2nd weapon__`")
                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                    label="display the equipement-type list",
                                                    custom_id="display"),
                                      create_button(style=ButtonStyle.blue,
                                                    label="not display the equipement-type list",
                                                    custom_id="not_display")]
                        button_raw = create_actionrow(*my_buttons)
                        fait_choix = await ctx.send("`Push for the equipement-type list : `", components=[button_raw])
                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                        if button_ctx.custom_id == "display":
                                await button_ctx.edit_origin(content=nonetxt)
                                equipement_list = st.filterEquipementType("weapon_type")
                                equipement_embed_list = tf.getListEmbedEquipementList(ctx,equipement_list)
                                for equipement_embed in equipement_embed_list:
                                        await ctx.send(embed=equipement_embed)
                                await ctx.send("`equipement chose`")
                                try:
                                        string_equipement_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        equipement_name = str(string_equipement_input.content)
                                        await ctx.send("__equipement-type : __ `" + equipement_name + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        equipement_name = "none"
                        elif button_ctx.custom_id == "not_display":
                                await button_ctx.edit_origin(content=nonetxt)
                                await view_type.send("`equipement-type chose`")
                                try:
                                        string_equipement_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        equipement_name = str(string_equipement_input.content)
                                        await ctx.send("__equipement-type : __ `" + equipement_name + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        equipement_name = "none"
                        second_weapon_type = st.loadEquipement(equipement_name)
                        await ctx.send("`__enter the enchance of the 2nd weapon__`")
                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                    label="display the enchance list",
                                                    custom_id="display"),
                                      create_button(style=ButtonStyle.blue,
                                                    label="not display the enchance list",
                                                    custom_id="not_display")]
                        button_raw = create_actionrow(*my_buttons)
                        fait_choix = await ctx.send("`Push for the enchance list : `", components=[button_raw])
                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                        if button_ctx.custom_id == "display":
                                await button_ctx.edit_origin(content=nonetxt)
                                enchance_list = list((st.loadDict("database\EnchancesDatabase.obj")).keys())
                                enchance_embed_list = tf.getListEmbedEnchancesList(ctx,enchance_list)
                                for enchance_embed in enchance_embed_list:
                                        await ctx.send(embed=enchance_embed)
                                await ctx.send("`enchance chose`")
                                try:
                                        string_enchance_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        enchance = str(string_enchance_input.content)
                                        await ctx.send("__enchance : __ `" + enchance + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        enchance = "none"
                        elif button_ctx.custom_id == "not_display":
                                await button_ctx.edit_origin(content=nonetxt)
                                await button_ctx.edit_origin(content=nonetxt)
                                await ctx.send("`enchance chose`")
                                try:
                                        string_enchance_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        enchance = str(string_enchance_input.content)
                                        await ctx.send("__enchance : __ `" + enchance + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        enchance = "none"
                        second_weapon_enchance = st.loadEnchance(enchance)
                        weapon_constructor02 = {"name" : second_weapon_name,
                                                "description": second_weapon_description,
                                                "level": second_weapon_level,
                                                "type" : second_weapon_type ,
                                                "enchance" : second_weapon_enchance,
                                                "enchance_name" : enchance}
                if button_ctx.custom_id == "not_generate":
                        await button_ctx.edit_origin(content=nonetxt)
                        weapon_constructor02 = {"name" : nonetxt,
                                                "description": nonetxt,
                                                "level": 0,
                                                "type" : rp.WeaponTypeClass("none","none") ,
                                                "enchance" : [rp.StatisticsClass("") for x in range(9)],
                                                "enchance_name" : nonetxt}
                await register_type.send("`do you want to generate a new weapon`")
                my_buttons = [create_button(style=ButtonStyle.blue,
                                            label="generate a new weapon",
                                            custom_id="generate"),
                              create_button(style=ButtonStyle.blue,
                                            label="dont generate a new weapon",
                                            custom_id="not_generate")]
                button_raw = create_actionrow(*my_buttons)
                fait_choix = await ctx.send("`Push for generation : `", components=[button_raw])
                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                if button_ctx.custom_id == "generate":
                        await button_ctx.edit_origin(content=nonetxt)
                        await ctx.send("`__enter the name of the 3st weapon(not the type of the weapon , the name)__`")
                        try:
                                third_weapon_name_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                third_weapon_name = str(third_weapon_name_input.content)
                                await ctx.send("__name of the 3st weapon : __ `" + third_weapon_name + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                third_weapon_name = nonetxt
                        await ctx.send("`__enter the description of the 3st weapon__`")
                        try:
                                third_weapon_description_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                third_weapon_description = str(third_weapon_description_input.content)
                                await ctx.send("__descrition of the 3st weapon : __ `" + third_weapon_description + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                third_weapon_description = nonetxt
                        await ctx.send("`__enter the level of the 3st weapon__`")
                        try:
                                thirs_weapon_level_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                thirs_weapon_level = int(thirs_weapon_level_input.content)
                                await ctx.send("__level of the 3st weapon : __ `" + str(thirs_weapon_level) + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                thirs_weapon_level = 0
                        await ctx.send("`__enter the type of the 3st weapon__`")
                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                    label="display the equipement-type list",
                                                    custom_id="display"),
                                      create_button(style=ButtonStyle.blue,
                                                    label="not display the equipement-type list",
                                                    custom_id="not_display")]
                        button_raw = create_actionrow(*my_buttons)
                        fait_choix = await ctx.send("`Push for the equipement-type list : `", components=[button_raw])
                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                        if button_ctx.custom_id == "display":
                                await button_ctx.edit_origin(content=nonetxt)
                                equipement_list = st.filterEquipementType("weapon_type")
                                equipement_embed_list = tf.getListEmbedEquipementList(ctx,equipement_list)
                                for equipement_embed in equipement_embed_list:
                                        await ctx.send(embed=equipement_embed)
                                await ctx.send("`equipement chose`")
                                try:
                                        string_equipement_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        equipement_name = str(string_equipement_input.content)
                                        await ctx.send("__equipement-type : __ `" + equipement_name + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        equipement_name = "none"
                        elif button_ctx.custom_id == "not_display":
                                await button_ctx.edit_origin(content=nonetxt)
                                await view_type.send("`equipement-type chose`")
                                try:
                                        string_equipement_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        equipement_name = str(string_equipement_input.content)
                                        await ctx.send("__equipement-type : __ `" + equipement_name + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        equipement_name = "none"
                        third_weapon_type = st.loadEquipement(equipement_name)
                        await ctx.send("`__enter the enchance of the 3st weapon__`")
                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                    label="display the enchance list",
                                                    custom_id="display"),
                                      create_button(style=ButtonStyle.blue,
                                                    label="not display the enchance list",
                                                    custom_id="not_display")]
                        button_raw = create_actionrow(*my_buttons)
                        fait_choix = await ctx.send("`Push for the enchance list : `", components=[button_raw])
                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                        if button_ctx.custom_id == "display":
                                await button_ctx.edit_origin(content=nonetxt)
                                enchance_list = list((st.loadDict("database\EnchancesDatabase.obj")).keys())
                                enchance_embed_list = tf.getListEmbedEnchancesList(ctx,enchance_list)
                                for enchance_embed in enchance_embed_list:
                                        await ctx.send(embed=enchance_embed)
                                await ctx.send("`enchance chose`")
                                try:
                                        string_enchance_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        enchance = str(string_enchance_input.content)
                                        await ctx.send("__enchance : __ `" + enchance + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        enchance = "none"
                        elif button_ctx.custom_id == "not_display":
                                await button_ctx.edit_origin(content=nonetxt)
                                await button_ctx.edit_origin(content=nonetxt)
                                await ctx.send("`enchance chose`")
                                try:
                                        string_enchance_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        enchance = str(string_enchance_input.content)
                                        await ctx.send("__enchance : __ `" + enchance + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        enchance = "none"
                        third_weapon_enchance = st.loadEnchance(enchance)
                        weapon_constructor03 = {"name" : third_weapon_name,
                                                "description": third_weapon_description,
                                                "level": third_weapon_level,
                                                "type" : third_weapon_type ,
                                                "enchance" : third_weapon_enchance,
                                                "enchance_name" : enchance}
                if button_ctx.custom_id == "not_generate":
                        await button_ctx.edit_origin(content=nonetxt)
                        weapon_constructor03 = {"name" : nonetxt,
                                                "description": nonetxt,
                                                "level": 0,
                                                "type" : rp.WeaponTypeClass("none","none") ,
                                                "enchance" : [rp.StatisticsClass("") for x in range(9)],
                                                "enchance_name" : nonetxt}    
                await ctx.send(":exclamation: __Vous avez droit d'avoir entre 0 a 2 accessoires.__")
                await register_type.send("`do you want to generate a new accessory`")
                my_buttons = [create_button(style=ButtonStyle.blue,
                                            label="generate a new accessory",
                                            custom_id="generate"),
                              create_button(style=ButtonStyle.blue,
                                            label="dont generate a new accessory",
                                            custom_id="not_generate")]
                button_raw = create_actionrow(*my_buttons)
                fait_choix = await ctx.send("`Push for generation : `", components=[button_raw])
                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                if button_ctx.custom_id == "generate":
                        await button_ctx.edit_origin(content=nonetxt)
                        await ctx.send("`__enter the name of the 1st accessory(not the type of the accessory , the name)__`")
                        try:
                                first_accessory_name_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                first_accessory_name = str(first_accessory_name_input.content)
                                await ctx.send("__name of the 1st accessory : __ `" + first_accessory_name + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                first_accessory_name = nonetxt
                        await ctx.send("`__enter the description of the 1st accessory__`")
                        try:
                                first_accessory_description_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                first_accessory_description = str(first_accessory_description_input.content)
                                await ctx.send("__descrition of the 1st accessory : __ `" + first_accessory_description + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                first_accessory_description = nonetxt
                        await ctx.send("`__enter the level of the 1st accessory__`")
                        try:
                                first_accessory_level_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                first_accessory_level = int(first_accessory_level_input.content)
                                await ctx.send("__level of the 1st accessory : __ `" + str(first_accessory_level) + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                first_accessory_level = 0
                        await ctx.send("`__enter the type of the 1st accessory__`")
                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                    label="display the equipement-type list",
                                                    custom_id="display"),
                                      create_button(style=ButtonStyle.blue,
                                                    label="not display the equipement-type list",
                                                    custom_id="not_display")]
                        button_raw = create_actionrow(*my_buttons)
                        fait_choix = await ctx.send("`Push for the equipement-type list : `", components=[button_raw])
                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                        if button_ctx.custom_id == "display":
                                await button_ctx.edit_origin(content=nonetxt)
                                equipement_list = st.filterEquipementType("accessory_type")
                                equipement_embed_list = tf.getListEmbedEquipementList(ctx,equipement_list)
                                for equipement_embed in equipement_embed_list:
                                        await ctx.send(embed=equipement_embed)
                                await ctx.send("`equipement chose`")
                                try:
                                        string_equipement_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        equipement_name = str(string_equipement_input.content)
                                        await ctx.send("__equipement-type : __ `" + equipement_name + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        equipement_name = "none"
                        elif button_ctx.custom_id == "not_display":
                                await button_ctx.edit_origin(content=nonetxt)
                                await view_type.send("`equipement-type chose`")
                                try:
                                        string_equipement_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        equipement_name = str(string_equipement_input.content)
                                        await ctx.send("__equipement-type : __ `" + equipement_name + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        equipement_name = "none"
                        first_accessory_type = st.loadEquipement(equipement_name)
                        await ctx.send("`__enter the enchance of the 1st accessory__`")
                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                    label="display the enchance list",
                                                    custom_id="display"),
                                      create_button(style=ButtonStyle.blue,
                                                    label="not display the enchance list",
                                                    custom_id="not_display")]
                        button_raw = create_actionrow(*my_buttons)
                        fait_choix = await ctx.send("`Push for the enchance list : `", components=[button_raw])
                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                        if button_ctx.custom_id == "display":
                                await button_ctx.edit_origin(content=nonetxt)
                                enchance_list = list((st.loadDict("database\EnchancesDatabase.obj")).keys())
                                enchance_embed_list = tf.getListEmbedEnchancesList(ctx,enchance_list)
                                for enchance_embed in enchance_embed_list:
                                        await ctx.send(embed=enchance_embed)
                                await ctx.send("`enchance chose`")
                                try:
                                        string_enchance_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        enchance = str(string_enchance_input.content)
                                        await ctx.send("__enchance : __ `" + enchance + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        enchance = "none"
                        elif button_ctx.custom_id == "not_display":
                                await button_ctx.edit_origin(content=nonetxt)
                                await button_ctx.edit_origin(content=nonetxt)
                                await ctx.send("`enchance chose`")
                                try:
                                        string_enchance_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        enchance = str(string_enchance_input.content)
                                        await ctx.send("__enchance : __ `" + enchance + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        enchance = "none"
                        first_accessory_enchance = st.loadEnchance(enchance)
                        accessory_constructor01 = {"name" : first_accessory_name,
                                                   "description": first_accessory_description,
                                                   "level": first_accessory_level,
                                                   "type" : first_accessory_type ,
                                                   "enchance" : first_accessory_enchance,
                                                   "enchance_name" : enchance}
                if button_ctx.custom_id == "not_generate":
                        await button_ctx.edit_origin(content=nonetxt)
                        accessory_constructor01 = {"name" : nonetxt,
                                                   "description": nonetxt,
                                                   "level": 0,
                                                   "type" : rp.AccessoryClassTypeClass("none","none") ,
                                                   "enchance" : [rp.StatisticsClass("") for x in range(9)],
                                                   "enchance_name" : nonetxt}
                await register_type.send("`do you want to generate a new accessory`")
                my_buttons = [create_button(style=ButtonStyle.blue,
                                            label="generate a new accessory",
                                            custom_id="generate"),
                              create_button(style=ButtonStyle.blue,
                                            label="dont generate a new accessory",
                                            custom_id="not_generate")]
                button_raw = create_actionrow(*my_buttons)
                fait_choix = await ctx.send("`Push for generation : `", components=[button_raw])
                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                if button_ctx.custom_id == "generate":
                        await button_ctx.edit_origin(content=nonetxt)
                        await ctx.send("`__enter the name of the 2nd accessory(not the type of the accessory , the name)__`")
                        try:
                                second_accessory_name_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                second_accessory_name = str(second_accessory_name_input.content)
                                await ctx.send("__name of the 2nd accessory : __ `" + second_accessory_name + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                second_accessory_name = nonetxt
                        await ctx.send("`__enter the description of the 2nd accessory__`")
                        try:
                                second_accessory_description_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                second_accessory_description = str(second_accessory_description_input.content)
                                await ctx.send("__descrition of the 2nd accessory : __ `" + second_accessory_description + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                second_accessory_description = nonetxt
                        await ctx.send("`__enter the level of the 2nd accessory__`")
                        try:
                                second_accessory_level_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                second_accessory_level = int(second_accessory_level_input.content)
                                await ctx.send("__level of the 2nd accessory : __ `" + str(second_accessory_level) + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                second_accessory_level = 0
                        await ctx.send("`__enter the type of the 2nd accessory__`")
                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                    label="display the equipement-type list",
                                                    custom_id="display"),
                                      create_button(style=ButtonStyle.blue,
                                                    label="not display the equipement-type list",
                                                    custom_id="not_display")]
                        button_raw = create_actionrow(*my_buttons)
                        fait_choix = await ctx.send("`Push for the equipement-type list : `", components=[button_raw])
                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                        if button_ctx.custom_id == "display":
                                await button_ctx.edit_origin(content=nonetxt)
                                equipement_list = st.filterEquipementType("accessory_type")
                                equipement_embed_list = tf.getListEmbedEquipementList(ctx,equipement_list)
                                for equipement_embed in equipement_embed_list:
                                        await ctx.send(embed=equipement_embed)
                                await ctx.send("`equipement chose`")
                                try:
                                        string_equipement_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        equipement_name = str(string_equipement_input.content)
                                        await ctx.send("__equipement-type : __ `" + equipement_name + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        equipement_name = "none"
                        elif button_ctx.custom_id == "not_display":
                                await button_ctx.edit_origin(content=nonetxt)
                                await view_type.send("`equipement-type chose`")
                                try:
                                        string_equipement_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        equipement_name = str(string_equipement_input.content)
                                        await ctx.send("__equipement-type : __ `" + equipement_name + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        equipement_name = "none"
                        second_accessory_type = st.loadEquipement(equipement_name)
                        await ctx.send("`__enter the enchance of the 2nd accessory__`")
                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                    label="display the enchance list",
                                                    custom_id="display"),
                                      create_button(style=ButtonStyle.blue,
                                                    label="not display the enchance list",
                                                    custom_id="not_display")]
                        button_raw = create_actionrow(*my_buttons)
                        fait_choix = await ctx.send("`Push for the enchance list : `", components=[button_raw])
                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                        if button_ctx.custom_id == "display":
                                await button_ctx.edit_origin(content=nonetxt)
                                enchance_list = list((st.loadDict("database\EnchancesDatabase.obj")).keys())
                                enchance_embed_list = tf.getListEmbedEnchancesList(ctx,enchance_list)
                                for enchance_embed in enchance_embed_list:
                                        await ctx.send(embed=enchance_embed)
                                await ctx.send("`enchance chose`")
                                try:
                                        string_enchance_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        enchance = str(string_enchance_input.content)
                                        await ctx.send("__enchance : __ `" + enchance + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        enchance = "none"
                        elif button_ctx.custom_id == "not_display":
                                await button_ctx.edit_origin(content=nonetxt)
                                await button_ctx.edit_origin(content=nonetxt)
                                await ctx.send("`enchance chose`")
                                try:
                                        string_enchance_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        enchance = str(string_enchance_input.content)
                                        await ctx.send("__enchance : __ `" + enchance + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        enchance = "none"
                        second_accessory_enchance = st.loadEnchance(enchance)
                        accessory_constructor02 = {"name" : second_accessory_name,
                                                   "description": second_accessory_description,
                                                   "level": second_accessory_level,
                                                   "type" : second_accessory_type ,
                                                   "enchance" : second_accessory_enchance,
                                                   "enchance_name" : enchance}
                if button_ctx.custom_id == "not_generate":
                        await button_ctx.edit_origin(content=nonetxt)
                        accessory_constructor02 = {"name" : nonetxt,
                                                   "description": nonetxt,
                                                   "level": 0,
                                                   "type" : rp.AccessoryClassTypeClass("none","none") ,
                                                   "enchance" : [rp.StatisticsClass("") for x in range(9)],
                                                   "enchance_name" : nonetxt}
                await ctx.send(":exclamation: `enregistrement de l'armure`")
                await register_type.send("`do you want to generate a new armor`")
                my_buttons = [create_button(style=ButtonStyle.blue,
                                            label="generate a new armor",
                                            custom_id="generate"),
                              create_button(style=ButtonStyle.blue,
                                            label="dont generate a new armor",
                                            custom_id="not_generate")]
                button_raw = create_actionrow(*my_buttons)
                fait_choix = await ctx.send("`Push for generation : `", components=[button_raw])
                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                if button_ctx.custom_id == "generate":
                        await button_ctx.edit_origin(content=nonetxt)
                        await ctx.send("`__enter the name of the armor(not the type of the armor , the name)__`")
                        try:
                                armor_name_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                armor_name = str(armor_name_input.content)
                                await ctx.send("__name of the armor : __ `" + armor_name + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                armor_name = nonetxt
                        await ctx.send("`__enter the description of the armor__`")
                        try:
                                armor_description_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                armor_description = str(armor_description_input.content)
                                await ctx.send("__descrition of the armor : __ `" + armor_description + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                armor_description = nonetxt
                        await ctx.send("`__enter the level of the armor__`")
                        try:
                                armor_level_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                armor_level = int(armor_level_input.content)
                                await ctx.send("__level of the armor : __ `" + str(armor_level) + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                armor_level = 0
                        await ctx.send("`__enter the type of the armor__`")
                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                    label="display the equipement-type list",
                                                    custom_id="display"),
                                      create_button(style=ButtonStyle.blue,
                                                    label="not display the equipement-type list",
                                                    custom_id="not_display")]
                        button_raw = create_actionrow(*my_buttons)
                        fait_choix = await ctx.send("`Push for the equipement-type list : `", components=[button_raw])
                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                        if button_ctx.custom_id == "display":
                                await button_ctx.edit_origin(content=nonetxt)
                                equipement_list = st.filterEquipementType("armor_type")
                                equipement_embed_list = tf.getListEmbedEquipementList(ctx,equipement_list)
                                for equipement_embed in equipement_embed_list:
                                        await ctx.send(embed=equipement_embed)
                                await ctx.send("`equipement chose`")
                                try:
                                        string_equipement_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        equipement_name = str(string_equipement_input.content)
                                        await ctx.send("__equipement-type : __ `" + equipement_name + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        equipement_name = "none"
                        elif button_ctx.custom_id == "not_display":
                                await button_ctx.edit_origin(content=nonetxt)
                                await view_type.send("`equipement-type chose`")
                                try:
                                        string_equipement_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        equipement_name = str(string_equipement_input.content)
                                        await ctx.send("__equipement-type : __ `" + equipement_name + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        equipement_name = "none"
                        armor_type = st.loadEquipement(equipement_name)
                        await ctx.send("`__enter the enchance of the armor__`")
                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                    label="display the enchance list",
                                                    custom_id="display"),
                                      create_button(style=ButtonStyle.blue,
                                                    label="not display the enchance list",
                                                    custom_id="not_display")]
                        button_raw = create_actionrow(*my_buttons)
                        fait_choix = await ctx.send("`Push for the enchance list : `", components=[button_raw])
                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                        if button_ctx.custom_id == "display":
                                await button_ctx.edit_origin(content=nonetxt)
                                enchance_list = list((st.loadDict("database\EnchancesDatabase.obj")).keys())
                                enchance_embed_list = tf.getListEmbedEnchancesList(ctx,enchance_list)
                                for enchance_embed in enchance_embed_list:
                                        await ctx.send(embed=enchance_embed)
                                await ctx.send("`enchance chose`")
                                try:
                                        string_enchance_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        enchance = str(string_enchance_input.content)
                                        await ctx.send("__enchance : __ `" + enchance + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        enchance = "none"
                        elif button_ctx.custom_id == "not_display":
                                await button_ctx.edit_origin(content=nonetxt)
                                await button_ctx.edit_origin(content=nonetxt)
                                await ctx.send("`enchance chose`")
                                try:
                                        string_enchance_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        enchance = str(string_enchance_input.content)
                                        await ctx.send("__enchance : __ `" + enchance + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        enchance = "none"
                        armor_enchance = st.loadEnchance(enchance)
                        armor_constructor = {"name" : armor_name,
                                             "description": armor_description,
                                             "level": armor_level,
                                             "type" : armor_type ,
                                             "enchance" : armor_enchance,
                                             "enchance_name" : enchance}
                if button_ctx.custom_id == "not_generate":
                        await button_ctx.edit_origin(content=nonetxt)
                        armor_constructor = {"name" : nonetxt,
                                             "description": nonetxt,
                                             "level": 0,
                                             "type" : rp.ArmorClassTypeClass("none","none") ,
                                             "enchance" : [rp.StatisticsClass("") for x in range(9)],
                                             "enchance_name" : nonetxt}
                await ctx.send(":exclamation: `enregistrement de vos connaissances de craft(cela reduit le prix d'achat des items de vos connaissances a 1/8 de leurs prix d'origine)`")
                my_buttons = [create_button(style=ButtonStyle.blue,
                                            label="display the item list",
                                            custom_id="display"),
                              create_button(style=ButtonStyle.blue,
                                            label="not display the item list",
                                            custom_id="not_display")]
                button_raw = create_actionrow(*my_buttons)
                fait_choix = await ctx.send("`Push for the item list : `", components=[button_raw])
                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                if button_ctx.custom_id == "display":
                        await button_ctx.edit_origin(content=nonetxt)
                        item_list = (st.loadDict(r"database\ItemsDatabase.obj")).keys()
                        item_embed_list = tf.getListItemEmbedImageList(ctx,item_list)
                        for item_embed in item_embed_list:
                                await ctx.send(embed=item_embed)
                        await ctx.send("`item01`|`item02`|.....|`itemN`")
                        try:
                                item_name_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                item_names = str(item_name_input.content)
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                item_names = "none"
                elif button_ctx.custom_id == "not_display":
                        await button_ctx.edit_origin(content=nonetxt)
                        await ctx.send("`item01`|`item02`|.....|`itemN`")
                        try:
                                item_name_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                item_names = str(item_name_input.content)
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                item_names = "none"
                if item_names != "none":
                        knoledge_list = item_names.split("|")
                else:
                        knoledge_list = []
                new_character = rp.CharacterClass(char_name,char_description,char_history,char_nick_name,char_titles,char_background_list,char_allignement,char_max_hp,char_level,char_race,char_classe,rp.StatisticsClass("",attack_template_constructor),weapon_constructor01,weapon_constructor02,weapon_constructor03,accessory_constructor01,accessory_constructor02, armor_constructor,other_statistics_pattern,char_image_path,{},char_capital,char_languages,rp.OrganisationClass("","",0,0),char_organisation,knoledge_list)
                st.saveArchetype(new_character)
                display_character = st.loadArchetype(char_name)
                first_embed = tf.getFirstEmbedImageCharacter(ctx,display_character)
                second_embed = tf.getSecondEmbedImageCharacter(ctx,display_character)
                await ctx.send(embed=first_embed)
                await ctx.send(embed=second_embed)
        if register_type.values[0] == "mass_entity_type":
                pass
        
@notlolabot.bot.command()
async def view(ctx):
        """view command for classes , races , competences , enchances , equipement , organisation , lore-information , characters , mass-entity"""
        def check(m):
                return m.author_id == ctx.author.id and m.origin_message.id == fait_choix.id
        def checkMessage(message):
                return message.author == ctx.message.author and ctx.message.channel == message.channel

        Selection_List = ["competence","enchance","lore informations","organisation","race","classe","equipement_type","archetype","item"]

        
        view_type_select = tf.getListSelection(ctx,"chose the view",Selection_List,Selection_List) 
        fait_choix = await ctx.send("`Chose the view : `", components=[create_actionrow(view_type_select)])
        view_type = await wait_for_component(notlolabot.bot, components=view_type_select, check=check)
        if view_type.values[0] == "competence":
                await view_type.send("`__enter the competences__`")
                my_buttons = [create_button(style=ButtonStyle.blue,
                                            label="display the skill list",
                                            custom_id="display"),
                              create_button(style=ButtonStyle.blue,
                                            label="not display the skill list",
                                            custom_id="not_display")]
                button_raw = create_actionrow(*my_buttons)
                fait_choix = await ctx.send("`Push for the skill list : `", components=[button_raw])
                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                if button_ctx.custom_id == "display":
                        await button_ctx.edit_origin(content=nonetxt)
                        skill_list = list(st.filterCompetences(""))
                        skill_embed_list = tf.getListEmbedSkillsList(ctx,skill_list,"none")
                        for skill_embed in skill_embed_list:
                                await ctx.send(embed=skill_embed)
                        await view_type.send("`skill`")
                        try:
                                string_skill_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                skill = str(string_skill_input.content)
                                await ctx.send("__skill : __ `" + skill + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                skill = "none"
                elif button_ctx.custom_id == "not_display":
                        await button_ctx.edit_origin(content=nonetxt)
                        await view_type.send("`skill`")
                        try:
                                string_skill_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                skill = str(string_skill_input.content)
                                await ctx.send("__skill : __ `" + skill + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                skill = "none"
                if skill != "none":
                        display_competence = st.loadCompetence(skill)
                        my_embed = tf.getEmbedImageCompetence(ctx,skill)
                        tf.TypographyCompetenceInterface(ctx,display_competence,my_embed)
                        await ctx.send(embed=my_embed)
        if view_type.values[0] == "enchance":
                await view_type.send("`__enter the enchance__`")
                my_buttons = [create_button(style=ButtonStyle.blue,
                                            label="display the enchance list",
                                            custom_id="display"),
                              create_button(style=ButtonStyle.blue,
                                            label="not display the enchance list",
                                            custom_id="not_display")]
                button_raw = create_actionrow(*my_buttons)
                fait_choix = await ctx.send("`Push for the enchance list : `", components=[button_raw])
                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                if button_ctx.custom_id == "display":
                        await button_ctx.edit_origin(content=nonetxt)
                        enchance_list = list((st.loadDict("database\EnchancesDatabase.obj")).keys())
                        enchance_embed_list = tf.getListEmbedEnchancesList(ctx,enchance_list)
                        for enchance_embed in enchance_embed_list:
                                await ctx.send(embed=enchance_embed)
                        await view_type.send("`enchance chose`")
                        try:
                                string_enchance_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                enchance = str(string_enchance_input.content)
                                await ctx.send("__enchance : __ `" + enchance + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                enchance = "none"
                elif button_ctx.custom_id == "not_display":
                        await button_ctx.edit_origin(content=nonetxt)
                        await view_type.send("`enchance chose`")
                        try:
                                string_enchance_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                enchance = str(string_enchance_input.content)
                                await ctx.send("__enchance : __ `" + enchance + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                enchance = "none"
                if enchance != "none":
                        display_enchance = st.loadEnchance(enchance)
                        first_embed = tf.getFirstEmbedImageEnchance(ctx,enchance,display_enchance)
                        await ctx.send(embed=first_embed)                
                        my_buttons = [create_button(
                                style=ButtonStyle.blue,
                                label="display the evolution",
                                custom_id="display")]
                        button_raw = create_actionrow(*my_buttons)
                        fait_choix = await ctx.send("`Push for display the evolution : `", components=[button_raw])
                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                        if button_ctx.custom_id == "display":
                                await button_ctx.edit_origin(content=nonetxt)
                                my_embed_list = tf.getTheEmbedEnchance(ctx,display_enchance)
                                for x in my_embed_list:
                                        await ctx.send(file=x[1], embed=x[0])
                pass
        if view_type.values[0] == "lore informations":
                await view_type.send("`__enter the lore name__`")
                my_buttons = [create_button(style=ButtonStyle.blue,
                                            label="display the lore event list",
                                            custom_id="display"),
                              create_button(style=ButtonStyle.blue,
                                            label="not display the lore event list",
                                            custom_id="not_display")]
                button_raw = create_actionrow(*my_buttons)
                fait_choix = await ctx.send("`Push for the lore list : `", components=[button_raw])
                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                if button_ctx.custom_id == "display":
                        await button_ctx.edit_origin(content=nonetxt)
                        lore_list = list((st.loadDict("database\LoresDatabase.obj")).keys())
                        lore_embed_list = tf.getListEmbedLoreList(ctx,lore_list)
                        for lore_embed in lore_embed_list:
                                await ctx.send(embed=lore_embed)
                        await view_type.send("`lore chose`")
                        try:
                                string_lore_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                lore_name = str(string_lore_input.content)
                                await ctx.send("__Lore : __ `" + lore_name + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                lore_name = "none"
                elif button_ctx.custom_id == "not_display":
                        await button_ctx.edit_origin(content=nonetxt)
                        await view_type.send("`lore chose`")
                        try:
                                string_lore_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                lore_name = str(string_lore_input.content)
                                await ctx.send("__Lore : __ `" + lore_name + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                lore_name = "none"
                if lore_name != "none":
                        lore_display = st.loadLore(lore_name)
                        embed_list = tf.getListEmbedImageLore(ctx,lore_display)
                        for my_embed in embed_list:
                                await ctx.send(embed=my_embed)
                pass
        if view_type.values[0] == "organisation":
                await view_type.send("`__enter the organisation name__`")
                my_buttons = [create_button(style=ButtonStyle.blue,
                                            label="display the organisation list",
                                            custom_id="display"),
                              create_button(style=ButtonStyle.blue,
                                            label="not display the organisation list",
                                            custom_id="not_display")]
                button_raw = create_actionrow(*my_buttons)
                fait_choix = await ctx.send("`Push for the organisation list : `", components=[button_raw])
                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                if button_ctx.custom_id == "display":
                        await button_ctx.edit_origin(content=nonetxt)
                        organisation_list = list((st.loadDict("database\OrganisationsDatabase.obj")).keys())
                        organisation_embed_list = tf.getListEmbedOrganisationList(ctx,organisation_list)
                        for organisation_embed in organisation_embed_list:
                                await ctx.send(embed=organisation_embed)
                        await view_type.send("`organisation chose`")
                        try:
                                string_organisation_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                organisation_name = str(string_organisation_input.content)
                                await ctx.send("__Organisation : __ `" + organisation_name + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                organisation_name = "none"
                elif button_ctx.custom_id == "not_display":
                        await button_ctx.edit_origin(content=nonetxt)
                        await view_type.send("`Organisation chose`")
                        try:
                                string_organisation_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                organisation_name = str(string_organisation_input.content)
                                await ctx.send("__Organisation : __ `" + organisation_name + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                organisation_name = "none"
                if organisation_name != "none":
                        display_organisation = st.loadOrganisation(organisation_name)
                        my_embeds = tf.getListEmbedImageOrganisation(ctx,display_organisation)
                        for my_embed in my_embeds:
                                await ctx.send(embed=my_embed)
                pass
        if view_type.values[0] == "race":
                await view_type.send("`__enter the race name__`")
                my_buttons = [create_button(style=ButtonStyle.blue,
                                            label="display the race list",
                                            custom_id="display"),
                              create_button(style=ButtonStyle.blue,
                                            label="not display the race list",
                                            custom_id="not_display")]
                button_raw = create_actionrow(*my_buttons)
                fait_choix = await ctx.send("`Push for the race list : `", components=[button_raw])
                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                if button_ctx.custom_id == "display":
                        await button_ctx.edit_origin(content=nonetxt)
                        race_list = list((st.loadDict("database\RacesDatabase.obj")).keys())
                        race_embed_list = tf.getListEmbedRaceList(ctx,race_list)
                        for race_embed in race_embed_list:
                                await ctx.send(embed=race_embed)
                        await view_type.send("`race chose`")
                        try:
                                string_race_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                race_name = str(string_race_input.content)
                                await ctx.send("__race : __ `" + race_name + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                race_name = "none"
                elif button_ctx.custom_id == "not_display":
                        await button_ctx.edit_origin(content=nonetxt)
                        await view_type.send("`race chose`")
                        try:
                                string_race_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                race_name = str(string_race_input.content)
                                await ctx.send("__race : __ `" + race_name + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                race_name = "none"
                if race_name != "none":
                        display_race = st.loadRace(race_name)
                        my_embed_list = tf.getListEmbedImageRace(ctx ,display_race)
                        for my_embed in my_embed_list:
                                await ctx.send(embed=my_embed)
                pass
        if view_type.values[0] == "classe":
                await view_type.send("`__enter the classe name__`")
                my_buttons = [create_button(style=ButtonStyle.blue,
                                            label="display the classe list",
                                            custom_id="display"),
                              create_button(style=ButtonStyle.blue,
                                            label="not display the classe list",
                                            custom_id="not_display")]
                button_raw = create_actionrow(*my_buttons)
                fait_choix = await ctx.send("`Push for the classe list : `", components=[button_raw])
                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                if button_ctx.custom_id == "display":
                        await button_ctx.edit_origin(content=nonetxt)
                        classe_list = list((st.loadDict("database\ClassDatabase.obj")).keys())
                        classe_embed_list = tf.getListEmbedClasseList(ctx,classe_list)
                        for classe_embed in classe_embed_list:
                                await ctx.send(embed=classe_embed)
                        await view_type.send("`classe chose`")
                        try:
                                string_classe_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                classe_name = str(string_classe_input.content)
                                await ctx.send("__classe : __ `" + classe_name + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                classe_name = "none"
                elif button_ctx.custom_id == "not_display":
                        await button_ctx.edit_origin(content=nonetxt)
                        await view_type.send("`classe chose`")
                        try:
                                string_classe_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                classe_name = str(string_classe_input.content)
                                await ctx.send("__classe : __ `" + classe_name + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                classe_name = "none"
                if classe_name != "none":
                        display_classe = st.loadClasse(classe_name)
                        my_embed_list = tf.getListEmbedImageClasse(ctx ,display_classe)
                        for my_embed in my_embed_list:
                                await ctx.send(embed=my_embed)
        if view_type.values[0] == "equipement_type":
                await view_type.send("`__enter the equipement-type name__`")
                my_buttons = [create_button(style=ButtonStyle.blue,
                                            label="display the equipement-type list",
                                            custom_id="display"),
                              create_button(style=ButtonStyle.blue,
                                            label="not display the equipement-type list",
                                            custom_id="not_display")]
                button_raw = create_actionrow(*my_buttons)
                fait_choix = await ctx.send("`Push for the equipement-type list : `", components=[button_raw])
                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                if button_ctx.custom_id == "display":
                        await button_ctx.edit_origin(content=nonetxt)
                        equipement_list = list((st.loadDict("database\EquipementsDatabase.obj")).keys())
                        equipement_embed_list = tf.getListEmbedEquipementList(ctx,equipement_list)
                        for equipement_embed in equipement_embed_list:
                                await ctx.send(embed=equipement_embed)
                        await view_type.send("`equipement chose`")
                        try:
                                string_equipement_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                equipement_name = str(string_equipement_input.content)
                                await ctx.send("__equipement-type : __ `" + equipement_name + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                equipement_name = "none"
                elif button_ctx.custom_id == "not_display":
                        await button_ctx.edit_origin(content=nonetxt)
                        await view_type.send("`equipement-type chose`")
                        try:
                                string_equipement_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                equipement_name = str(string_equipement_input.content)
                                await ctx.send("__equipement-type : __ `" + equipement_name + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                equipement_name = "none"
                if equipement_name != "none":
                        display_equipement_type = st.loadEquipement(equipement_name)
                        my_embed = tf.getEmbedEquipementType(ctx,display_equipement_type)
                        await ctx.send(embed=my_embed)
                pass
        if view_type.values[0] == "archetype":
                await view_type.send("`__enter the archetype name__`")
                my_buttons = [create_button(style=ButtonStyle.blue,
                                            label="display the archetype list",
                                            custom_id="display"),
                              create_button(style=ButtonStyle.blue,
                                            label="not display the archetype list",
                                            custom_id="not_display")]
                button_raw = create_actionrow(*my_buttons)
                fait_choix = await ctx.send("`Push for the archetype list : `", components=[button_raw])
                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                if button_ctx.custom_id == "display":
                        await button_ctx.edit_origin(content=nonetxt)
                        list_of_archetype = list((st.loadDict(r"database\archetypes_database.obj")).keys())
                        archetype_embed_list = tf.getListArchetypesEmbedImageList(ctx,list_of_archetype)
                        for archetype_embed in archetype_embed_list:
                                await ctx.send(embed=archetype_embed)
                        await ctx.send("`chose the archetype (none for cancel this action): `")
                        try:
                                archetype_name_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                archetype_name = str(archetype_name_input.content)
                                await ctx.send("__name : __ `" + archetype_name + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                archetype_name = "none"
                elif button_ctx.custom_id == "not_display":
                        await button_ctx.edit_origin(content=nonetxt)
                        await ctx.send("`chose the archetype (none for cancel this action): `")
                        try:
                                archetype_name_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                archetype_name = str(archetype_name_input.content)
                                await ctx.send("__name : __ `" + archetype_name + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                archetype_name = "none"


                if archetype_name != "none":                                
                        display_character = st.loadArchetype(archetype_name)
                        first_embed = tf.getFirstEmbedImageCharacter(ctx,display_character)
                        second_embed = tf.getSecondEmbedImageCharacter(ctx,display_character)
                        await ctx.send(embed=first_embed)
                        await ctx.send(embed=second_embed)
                        my_buttons = [create_button(style=ButtonStyle.green,
                                                    label="add this archetype whith a random name",
                                                    custom_id="random name"),
                                      create_button(style=ButtonStyle.green,
                                                    label="add this archetype whith a custom name",
                                                    custom_id="not random name")]
                        button_raw = create_actionrow(*my_buttons)
                        fait_choix = await ctx.send("`Push for add this archetype in your family : ` **" + ctx.author.display_name + "**" , components=[button_raw])
                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                        if button_ctx.custom_id == "random name":
                                await button_ctx.edit_origin(content=nonetxt)
                                display_name = ctx.author.display_name
                                user_name = ctx.author.name
                                await view_type.send("`enter the number of instances(moins de 20)`")
                                try:
                                        instance_number_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        instance_number = int(str(instance_number_input.content))
                                        await ctx.send("__number of new entity : __ **" + str(instance_number) + "**")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        instance_number = 1
                                for j in range(instance_number):
                                        instance_archetype_name = sktr.getRandomName(8) + " " + sktr.getRandomName()
                                        instance = copy.deepcopy(display_character)
                                        instance.name = instance_archetype_name
                                        st.saveCharacter(instance,user_name,display_name)
                                        await ctx.send("**new mobs register!**")
                        if button_ctx.custom_id == "not random name":
                                await button_ctx.edit_origin(content=nonetxt)
                                display_name = ctx.author.display_name
                                user_name = ctx.author.name
                                await view_type.send("`__enter the name of the instance of the archetype__`")
                                try:
                                        instance_archetype_name_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                        instance_archetype_name = str(instance_archetype_name_input.content)+"(mob)"
                                        await ctx.send("__name : __ `" + instance_archetype_name + "`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        instance_archetype_name = sktr.getRandomName(8) + " " + sktr.getRandomName()      
                                instance = copy.deepcopy(display_character)
                                instance.name = instance_archetype_name
                                st.saveCharacter(instance,user_name,display_name)
                                display_character = st.loadCharacter(user_name,display_name,instance_archetype_name)
                                first_embed = tf.getFirstEmbedImageCharacter(ctx,display_character)
                                second_embed = tf.getSecondEmbedImageCharacter(ctx,display_character)
                                await ctx.send(embed=first_embed)
                                await ctx.send(embed=second_embed)
                
        
        elif view_type.values[0] == "item":
                await view_type.send("`__enter the item name__`")
                display_name = ctx.author.display_name
                user_name = ctx.author.name
                
                my_buttons = [create_button(style=ButtonStyle.blue,
                                            label="display the item list",
                                            custom_id="display"),
                              create_button(style=ButtonStyle.blue,
                                            label="not display the item list",
                                            custom_id="not_display")]
                button_raw = create_actionrow(*my_buttons)
                fait_choix = await ctx.send("`Push for the item list : `", components=[button_raw])
                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                if button_ctx.custom_id == "display":
                        await button_ctx.edit_origin(content=nonetxt)
                        item_list = list((st.loadDict(r"database\ItemsDatabase.obj")).keys())
                        item_embed_list = tf.getListItemEmbedImageList(ctx,item_list)
                        for item_embed in item_embed_list:
                                await ctx.send(embed=item_embed)
                        try:
                                item_name_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                item_name = str(item_name_input.content)
                                await ctx.send("__name : __ `" + item_name + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                elif button_ctx.custom_id == "not_display":
                        await button_ctx.edit_origin(content=nonetxt)
                        try:
                                item_name_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                item_name = str(item_name_input.content)
                                await ctx.send("__name : __ `" + item_name + "`")
                        except:
                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                if item_name != "none":
                        display_item = st.loadItem(item_name)
                        my_embed = tf.getEmbedImageItem(ctx,display_item)
                        await ctx.send(embed=my_embed)
                        my_buttons = [create_button(style=ButtonStyle.green,
                                                    label="add the item in your inventory",
                                                    custom_id="add")]
                        button_raw = create_actionrow(*my_buttons)
                        fait_choix = await ctx.send("`Push for add the item in your inventory : `", components=[button_raw])
                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                        if button_ctx.custom_id == "add":
                                await button_ctx.edit_origin(content=nonetxt)
                                
                                display_name = ctx.author.display_name
                                user_name = ctx.author.name
                                if user_name in st.loadDict(r"database\users_database.obj").keys():
                                        char_name = st.loadUser(user_name).sub_pointage
                                        display_character = st.loadCharacter(user_name,display_name,char_name)
                                        await ctx.send("number of **" + item_name + " : **")
                                        try:
                                                item_number_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                                item_number = int(str(item_number_input.content))
                                                await ctx.send("__item number : __ `" + str(item_number) + "`")
                                        except:
                                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                item_number = 1
                                        if item_name in display_character.craft_knowledge:
                                                if display_character.capital >= int(display_item.price*item_number*(1/8)):
                                                        if item_name in display_character.inventory.keys():
                                                                display_character.inventory[item_name].quantity += item_number
                                                        else:
                                                                display_character.inventory[item_name] = display_item
                                                                display_character.inventory[item_name].quantity += item_number
                                                        display_character.capital = display_character.capital - int(display_item.price * item_number * (1/8))
                                                        st.saveCharacter(display_character,user_name,display_name)
                                                        await ctx.send("`item ajouter a l'inventaire`")
                                                else:
                                                        await ctx.send("`fonds insuffisants`")
                                        else:
                                                if display_character.capital >= (display_item.price*item_number):
                                                        if item_name in display_character.inventory.keys():
                                                                display_character.inventory[item_name].quantity += item_number
                                                        else:
                                                                display_character.inventory[item_name] = display_item
                                                                display_character.inventory[item_name].quantity += item_number
                                                        display_character.capital = display_character.capital - (display_item.price * item_number)
                                                        st.saveCharacter(display_character,user_name,display_name)
                                                        await ctx.send("`item ajouter a l'inventaire`")
                                                else:
                                                        await ctx.send("`fonds insuffisants`")
                                else:
                                        await ctx.send("personnage non enregistrer")
                pass
                
@notlolabot.bot.command()
async def board(ctx):
        """display the statistics of the character , update your equipement , diplay your inventory , your history and refresh your statistics"""
        def check(m):
                return m.author_id == ctx.author.id and m.origin_message.id == fait_choix.id
        def checkMessage(message):
                return message.author == ctx.message.author and ctx.message.channel == message.channel
        display_name = ctx.author.display_name
        user_name = ctx.author.name
        if user_name in st.loadDict(r"database\users_database.obj").keys():
                char_name = st.loadUser(user_name).sub_pointage
                display_character = st.loadCharacter(user_name,display_name,char_name)
                state_of_caster = sktr.getUpdateStateOfCharacter(display_character)
                display_character.state = (state_of_caster,display_character.state[1],display_character.state[2])
                st.saveCharacter(display_character,user_name,display_name)
                display_character = st.loadCharacter(user_name,display_name,char_name)
                first_embed = tf.getFirstEmbedImageCharacter(ctx,display_character)
                second_embed = tf.getSecondEmbedImageCharacter(ctx,display_character)
                await ctx.send(embed=first_embed)
                await ctx.send(embed=second_embed)


                my_buttons = [create_button(style=ButtonStyle.green,
                                            label="update gear",
                                            custom_id="update gear"),
                              create_button(style=ButtonStyle.green,
                                            label="display lore",
                                            custom_id="display the history"),
                              create_button(style=ButtonStyle.green,
                                            label="refresh",
                                            custom_id="refresh"),
                              create_button(style=ButtonStyle.green,
                                            label="display inventory",
                                            custom_id="display inventory")]
                button_raw = create_actionrow(*my_buttons)
                fait_choix = await ctx.send("`Push the button for display or change a option : `", components=[button_raw])
                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                if button_ctx.custom_id == "update gear":
                        await button_ctx.edit_origin(content=nonetxt)
                        selection = ["first weapon","second weapon","third weapon","first accessory","second accessory","armor","user_level","user_max_life","race","classe","capital","knoledges"]
                        update_type_select = tf.getListSelection(ctx,"chose the update of your gear",selection,selection) 
                        fait_choix = await ctx.send("`chose the update of your gear : `", components=[create_actionrow(update_type_select)])
                        update_type = await wait_for_component(notlolabot.bot, components=update_type_select, check=check)
                        if update_type.values[0] == "knoledges":
                                await update_type.send(nonetxt)
                                embed_list = tf.getListKnoledgeEmbedImageList(ctx,display_character.craft_knowledge)
                                for my_embed in embed_list:
                                        await ctx.send(embed=my_embed)
                                my_buttons = [create_button(style=ButtonStyle.green,
                                                            label="update the list",
                                                            custom_id="update"),
                                              create_button(style=ButtonStyle.green,
                                                            label="ad a item",
                                                            custom_id="ad"),
                                              create_button(style=ButtonStyle.green,
                                                            label="delete a item",
                                                            custom_id="delete")]
                                button_raw = create_actionrow(*my_buttons)
                                fait_choix = await ctx.send("`Push the button for display or change a option : `", components=[button_raw])
                                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                if button_ctx.custom_id == "update":
                                        await button_ctx.edit_origin(content=nonetxt)
                                        if button_ctx.custom_id == "display":
                                                await button_ctx.edit_origin(content=nonetxt)
                                                item_list = list((st.loadDict(r"database\ItemsDatabase.obj")).keys())
                                                item_embed_list = tf.getListItemEmbedImageList(ctx,item_list)
                                                for item_embed in item_embed_list:
                                                        await ctx.send(embed=item_embed)
                                                await ctx.send("`item01`|`item02`|.....|`itemN`")
                                                try:
                                                        item_name_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                                        item_names = str(item_name_input.content)
                                                except:
                                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                        item_names = "none"
                                        elif button_ctx.custom_id == "not_display":
                                                await button_ctx.edit_origin(content=nonetxt)
                                                await ctx.send("`item01`|`item02`|.....|`itemN`")
                                                try:
                                                        item_name_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                                        item_names = str(item_name_input.content)
                                                except:
                                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                        item_names = "none"
                                        if item_names != "none":
                                                knoledge_list = item_names.split("|")
                                                display_character.craft_knowledge = knoledge_list
                                                st.saveCharacter(display_character,user_name,display_name)    
                                if button_ctx.custom_id == "ad":
                                        await button_ctx.edit_origin(content=nonetxt)
                                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                                    label="display the item list",
                                                                    custom_id="display"),
                                                      create_button(style=ButtonStyle.blue,
                                                                    label="not display the item list",
                                                                    custom_id="not_display")]
                                        button_raw = create_actionrow(*my_buttons)
                                        fait_choix = await ctx.send("`Push for the item list : `", components=[button_raw])
                                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                        if button_ctx.custom_id == "display":
                                                await button_ctx.edit_origin(content=nonetxt)
                                                item_list = list((st.loadDict(r"database\ItemsDatabase.obj")).keys())
                                                item_embed_list = tf.getListItemEmbedImageList(ctx,item_list)
                                                for item_embed in item_embed_list:
                                                        await ctx.send(embed=item_embed)
                                                await ctx.send("`enter the item name :`")
                                                try:
                                                        item_name_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                                        item_name = str(item_name_input.content)
                                                        await ctx.send("__name : __ `" + item_name + "`")
                                                except:
                                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        elif button_ctx.custom_id == "not_display":
                                                await button_ctx.edit_origin(content=nonetxt)
                                                await ctx.send("`enter the item name :`")
                                                try:
                                                        item_name_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                                        item_name = str(item_name_input.content)
                                                        await ctx.send("__name : __ `" + item_name + "`")
                                                except:
                                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        if item_name != "none":
                                                display_character.craft_knowledge.append(item_name)
                                                st.saveCharacter(display_character,user_name,display_name)   
                                if button_ctx.custom_id == "delete":
                                        await button_ctx.edit_origin(content=nonetxt)
                                        try:
                                                item_name_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                                item_name = str(item_name_input.content)
                                                await ctx.send("__name : __ `" + item_name + "`")
                                        except:
                                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        if item_name != "none":
                                                display_character.craft_knowledge.pop(st.getIndice(display_character.craft_knowledge,item_name))
                                                st.saveCharacter(display_character,user_name,display_name)
                        if update_type.values[0] == "first weapon":
                                await update_type.send(nonetxt)
                                await ctx.send("`do you want to generate a new weapon`")
                                my_buttons = [create_button(style=ButtonStyle.blue,
                                                            label="generate a new weapon",
                                                            custom_id="generate"),
                                              create_button(style=ButtonStyle.blue,
                                                            label="dont generate a new weapon",
                                                            custom_id="not_generate")]
                                button_raw = create_actionrow(*my_buttons)
                                fait_choix = await ctx.send("`Push for generation : `", components=[button_raw])
                                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                if button_ctx.custom_id == "generate":
                                        await button_ctx.edit_origin(content=nonetxt)
                                        await ctx.send("`__enter the name of the 1st weapon(not the type of the weapon , the name)__`")
                                        try:
                                                first_weapon_name_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                                first_weapon_name = str(first_weapon_name_input.content)
                                                await ctx.send("__name of the 1st weapon : __ `" + first_weapon_name + "`")
                                        except:
                                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                first_weapon_name = nonetxt
                                        await ctx.send("`__enter the description of the 1st weapon__`")
                                        try:
                                                first_weapon_description_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                                first_weapon_description = str(first_weapon_description_input.content)
                                                await ctx.send("__descrition of the 1st weapon : __ `" + first_weapon_description + "`")
                                        except:
                                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                first_weapon_description = nonetxt
                                        await ctx.send("`__enter the level of the 1st weapon__`")
                                        try:
                                                first_weapon_level_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                                first_weapon_level = int(first_weapon_level_input.content)
                                                await ctx.send("__level of the 1st weapon : __ `" + str(first_weapon_level) + "`")
                                        except:
                                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                first_weapon_level = 0
                                        await ctx.send("`__enter the type of the 1st weapon__`")
                                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                                    label="display the equipement-type list",
                                                                    custom_id="display"),
                                                      create_button(style=ButtonStyle.blue,
                                                                    label="not display the equipement-type list",
                                                                    custom_id="not_display")]
                                        button_raw = create_actionrow(*my_buttons)
                                        fait_choix = await ctx.send("`Push for the equipement-type list : `", components=[button_raw])
                                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                        if button_ctx.custom_id == "display":
                                                await button_ctx.edit_origin(content=nonetxt)
                                                equipement_list = list(st.filterEquipementType("weapon_type"))
                                                equipement_embed_list = tf.getListEmbedEquipementList(ctx,equipement_list)
                                                for equipement_embed in equipement_embed_list:
                                                        await ctx.send(embed=equipement_embed)
                                                await ctx.send("`equipement chose`")
                                                try:
                                                        string_equipement_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                                        equipement_name = str(string_equipement_input.content)
                                                        await ctx.send("__equipement-type : __ `" + equipement_name + "`")
                                                except:
                                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                        equipement_name = "none"
                                        elif button_ctx.custom_id == "not_display":
                                                await button_ctx.edit_origin(content=nonetxt)
                                                await view_type.send("`equipement-type chose`")
                                                try:
                                                        string_equipement_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                                        equipement_name = str(string_equipement_input.content)
                                                        await ctx.send("__equipement-type : __ `" + equipement_name + "`")
                                                except:
                                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                        equipement_name = "none"
                                        first_weapon_type = st.loadEquipement(equipement_name)
                                        await ctx.send("`__enter the enchance of the 1st weapon__`")
                                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                                    label="display the enchance list",
                                                                    custom_id="display"),
                                                      create_button(style=ButtonStyle.blue,
                                                                    label="not display the enchance list",
                                                                    custom_id="not_display")]
                                        button_raw = create_actionrow(*my_buttons)
                                        fait_choix = await ctx.send("`Push for the enchance list : `", components=[button_raw])
                                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                        if button_ctx.custom_id == "display":
                                                await button_ctx.edit_origin(content=nonetxt)
                                                enchance_list = list((st.loadDict("database\EnchancesDatabase.obj")).keys())
                                                enchance_embed_list = tf.getListEmbedEnchancesList(ctx,enchance_list)
                                                for enchance_embed in enchance_embed_list:
                                                        await ctx.send(embed=enchance_embed)
                                                await ctx.send("`enchance chose`")
                                                try:
                                                        string_enchance_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                                        enchance = str(string_enchance_input.content)
                                                        await ctx.send("__enchance : __ `" + enchance + "`")
                                                except:
                                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                        enchance = "none"
                                        elif button_ctx.custom_id == "not_display":
                                                await button_ctx.edit_origin(content=nonetxt)
                                                await button_ctx.edit_origin(content=nonetxt)
                                                await ctx.send("`enchance chose`")
                                                try:
                                                        string_enchance_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                                        enchance = str(string_enchance_input.content)
                                                        await ctx.send("__enchance : __ `" + enchance + "`")
                                                except:
                                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                        enchance = "none"
                                        first_weapon_enchance = st.loadEnchance(enchance)
                                        weapon_constructor01 = {"name" : first_weapon_name,
                                                                "description": first_weapon_description,
                                                                "level": first_weapon_level,
                                                                "type" : first_weapon_type ,
                                                                "enchance" : first_weapon_enchance,
                                                                "enchance_name" : enchance}
                                if button_ctx.custom_id == "not_generate":
                                        await button_ctx.edit_origin(content=nonetxt)
                                        weapon_constructor01 = {"name" : nonetxt,
                                                                "description": nonetxt,
                                                                "level": 0,
                                                                "type" : rp.WeaponTypeClass("none","none") ,
                                                                "enchance" : [rp.StatisticsClass("") for x in range(9)],
                                                                "enchance_name" : nonetxt}
                                display_character.constructor_weapon01 = weapon_constructor01
                                display_character.weapon01 = rp.WeaponClass(weapon_constructor01["name"],weapon_constructor01["description"],weapon_constructor01["level"],weapon_constructor01["type"],weapon_constructor01["enchance"],weapon_constructor01["enchance_name"])
                                st.saveCharacter(display_character,user_name,display_name)
                                await ctx.send("`moddifications register`")
                                pass
                        if update_type.values[0] == "second weapon":
                                await update_type.send(nonetxt)
                                await ctx.send("`do you want to generate a new weapon`")
                                my_buttons = [create_button(style=ButtonStyle.blue,
                                                            label="generate a new weapon",
                                                            custom_id="generate"),
                                              create_button(style=ButtonStyle.blue,
                                                            label="dont generate a new weapon",
                                                            custom_id="not_generate")]
                                button_raw = create_actionrow(*my_buttons)
                                fait_choix = await ctx.send("`Push for generation : `", components=[button_raw])
                                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                if button_ctx.custom_id == "generate":
                                        await button_ctx.edit_origin(content=nonetxt)
                                        await ctx.send("`__enter the name of the 2nd weapon(not the type of the weapon , the name)__`")
                                        try:
                                                second_weapon_name_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                                second_weapon_name = str(second_weapon_name_input.content)
                                                await ctx.send("__name of the 2nd weapon : __ `" + second_weapon_name + "`")
                                        except:
                                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                second_weapon_name = nonetxt
                                        await ctx.send("`__enter the description of the 2nd weapon__`")
                                        try:
                                                second_weapon_description_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                                second_weapon_description = str(second_weapon_description_input.content)
                                                await ctx.send("__descrition of the 2nd weapon : __ `" + second_weapon_description + "`")
                                        except:
                                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                second_weapon_description = nonetxt
                                        await ctx.send("`__enter the level of the 2nd weapon__`")
                                        try:
                                                second_weapon_level_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                                second_weapon_level = int(second_weapon_level_input.content)
                                                await ctx.send("__level of the 2st weapon : __ `" + str(second_weapon_level) + "`")
                                        except:
                                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                second_weapon_level = 0
                                        await ctx.send("`__enter the type of the 2nd weapon__`")
                                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                                    label="display the equipement-type list",
                                                                    custom_id="display"),
                                                      create_button(style=ButtonStyle.blue,
                                                                    label="not display the equipement-type list",
                                                                    custom_id="not_display")]
                                        button_raw = create_actionrow(*my_buttons)
                                        fait_choix = await ctx.send("`Push for the equipement-type list : `", components=[button_raw])
                                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                        if button_ctx.custom_id == "display":
                                                await button_ctx.edit_origin(content=nonetxt)
                                                equipement_list = list(st.filterEquipementType("weapon_type"))
                                                equipement_embed_list = tf.getListEmbedEquipementList(ctx,equipement_list)
                                                for equipement_embed in equipement_embed_list:
                                                        await ctx.send(embed=equipement_embed)
                                                await ctx.send("`equipement chose`")
                                                try:
                                                        string_equipement_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                                        equipement_name = str(string_equipement_input.content)
                                                        await ctx.send("__equipement-type : __ `" + equipement_name + "`")
                                                except:
                                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                        equipement_name = "none"
                                        elif button_ctx.custom_id == "not_display":
                                                await button_ctx.edit_origin(content=nonetxt)
                                                await view_type.send("`equipement-type chose`")
                                                try:
                                                        string_equipement_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                                        equipement_name = str(string_equipement_input.content)
                                                        await ctx.send("__equipement-type : __ `" + equipement_name + "`")
                                                except:
                                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                        equipement_name = "none"
                                        second_weapon_type = st.loadEquipement(equipement_name)
                                        await ctx.send("`__enter the enchance of the 2nd weapon__`")
                                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                                    label="display the enchance list",
                                                                    custom_id="display"),
                                                      create_button(style=ButtonStyle.blue,
                                                                    label="not display the enchance list",
                                                                    custom_id="not_display")]
                                        button_raw = create_actionrow(*my_buttons)
                                        fait_choix = await ctx.send("`Push for the enchance list : `", components=[button_raw])
                                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                        if button_ctx.custom_id == "display":
                                                await button_ctx.edit_origin(content=nonetxt)
                                                enchance_list = list((st.loadDict("database\EnchancesDatabase.obj")).keys())
                                                enchance_embed_list = tf.getListEmbedEnchancesList(ctx,enchance_list)
                                                for enchance_embed in enchance_embed_list:
                                                        await ctx.send(embed=enchance_embed)
                                                await ctx.send("`enchance chose`")
                                                try:
                                                        string_enchance_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                                        enchance = str(string_enchance_input.content)
                                                        await ctx.send("__enchance : __ `" + enchance + "`")
                                                except:
                                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                        enchance = "none"
                                        elif button_ctx.custom_id == "not_display":
                                                await button_ctx.edit_origin(content=nonetxt)
                                                await button_ctx.edit_origin(content=nonetxt)
                                                await ctx.send("`enchance chose`")
                                                try:
                                                        string_enchance_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                                        enchance = str(string_enchance_input.content)
                                                        await ctx.send("__enchance : __ `" + enchance + "`")
                                                except:
                                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                        enchance = "none"
                                        second_weapon_enchance = st.loadEnchance(enchance)
                                        weapon_constructor02 = {"name" : second_weapon_name,
                                                                "description": second_weapon_description,
                                                                "level": second_weapon_level,
                                                                "type" : second_weapon_type ,
                                                                "enchance" : second_weapon_enchance,
                                                                "enchance_name" : enchance}
                                if button_ctx.custom_id == "not_generate":
                                        await button_ctx.edit_origin(content=nonetxt)
                                        weapon_constructor02 = {"name" : nonetxt,
                                                                "description": nonetxt,
                                                                "level": 0,
                                                                "type" : rp.WeaponTypeClass("none","none") ,
                                                                "enchance" : [rp.StatisticsClass("") for x in range(9)],
                                                                "enchance_name" : nonetxt}
                                display_character.constructor_weapon02 = weapon_constructor02
                                display_character.weapon02 = rp.WeaponClass(weapon_constructor02["name"],weapon_constructor02["description"],weapon_constructor02["level"],weapon_constructor02["type"],weapon_constructor02["enchance"],weapon_constructor02["enchance_name"])
                                st.saveCharacter(display_character,user_name,display_name)
                                await ctx.send("`moddifications register`")
                                pass
                        if update_type.values[0] == "third weapon":
                                await update_type.send(nonetxt)
                                await ctx.send("`do you want to generate a new weapon`")
                                my_buttons = [create_button(style=ButtonStyle.blue,
                                                            label="generate a new weapon",
                                                            custom_id="generate"),
                                              create_button(style=ButtonStyle.blue,
                                                            label="dont generate a new weapon",
                                                            custom_id="not_generate")]
                                button_raw = create_actionrow(*my_buttons)
                                fait_choix = await ctx.send("`Push for generation : `", components=[button_raw])
                                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                if button_ctx.custom_id == "generate":
                                        await button_ctx.edit_origin(content=nonetxt)
                                        await ctx.send("`__enter the name of the 3st weapon(not the type of the weapon , the name)__`")
                                        try:
                                                third_weapon_name_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                                third_weapon_name = str(third_weapon_name_input.content)
                                                await ctx.send("__name of the 3st weapon : __ `" + third_weapon_name + "`")
                                        except:
                                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                third_weapon_name = nonetxt
                                        await ctx.send("`__enter the description of the 3st weapon__`")
                                        try:
                                                third_weapon_description_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                                third_weapon_description = str(third_weapon_description_input.content)
                                                await ctx.send("__descrition of the 3st weapon : __ `" + third_weapon_description + "`")
                                        except:
                                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                third_weapon_description = nonetxt
                                        await ctx.send("`__enter the level of the 3st weapon__`")
                                        try:
                                                thirs_weapon_level_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                                thirs_weapon_level = int(thirs_weapon_level_input.content)
                                                await ctx.send("__level of the 3st weapon : __ `" + str(thirs_weapon_level) + "`")
                                        except:
                                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                thirs_weapon_level = 0
                                        await ctx.send("`__enter the type of the 3st weapon__`")
                                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                                    label="display the equipement-type list",
                                                                    custom_id="display"),
                                                      create_button(style=ButtonStyle.blue,
                                                                    label="not display the equipement-type list",
                                                                    custom_id="not_display")]
                                        button_raw = create_actionrow(*my_buttons)
                                        fait_choix = await ctx.send("`Push for the equipement-type list : `", components=[button_raw])
                                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                        if button_ctx.custom_id == "display":
                                                await button_ctx.edit_origin(content=nonetxt)
                                                equipement_list = list(st.filterEquipementType("weapon_type"))
                                                equipement_embed_list = tf.getListEmbedEquipementList(ctx,equipement_list)
                                                for equipement_embed in equipement_embed_list:
                                                        await ctx.send(embed=equipement_embed)
                                                await ctx.send("`equipement chose`")
                                                try:
                                                        string_equipement_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                                        equipement_name = str(string_equipement_input.content)
                                                        await ctx.send("__equipement-type : __ `" + equipement_name + "`")
                                                except:
                                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                        equipement_name = "none"
                                        elif button_ctx.custom_id == "not_display":
                                                await button_ctx.edit_origin(content=nonetxt)
                                                await view_type.send("`equipement-type chose`")
                                                try:
                                                        string_equipement_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                                        equipement_name = str(string_equipement_input.content)
                                                        await ctx.send("__equipement-type : __ `" + equipement_name + "`")
                                                except:
                                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                        equipement_name = "none"
                                        third_weapon_type = st.loadEquipement(equipement_name)
                                        await ctx.send("`__enter the enchance of the 3st weapon__`")
                                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                                    label="display the enchance list",
                                                                    custom_id="display"),
                                                      create_button(style=ButtonStyle.blue,
                                                                    label="not display the enchance list",
                                                                    custom_id="not_display")]
                                        button_raw = create_actionrow(*my_buttons)
                                        fait_choix = await ctx.send("`Push for the enchance list : `", components=[button_raw])
                                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                        if button_ctx.custom_id == "display":
                                                await button_ctx.edit_origin(content=nonetxt)
                                                enchance_list = list((st.loadDict("database\EnchancesDatabase.obj")).keys())
                                                enchance_embed_list = tf.getListEmbedEnchancesList(ctx,enchance_list)
                                                for enchance_embed in enchance_embed_list:
                                                        await ctx.send(embed=enchance_embed)
                                                await ctx.send("`enchance chose`")
                                                try:
                                                        string_enchance_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                                        enchance = str(string_enchance_input.content)
                                                        await ctx.send("__enchance : __ `" + enchance + "`")
                                                except:
                                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                        enchance = "none"
                                        elif button_ctx.custom_id == "not_display":
                                                await button_ctx.edit_origin(content=nonetxt)
                                                await button_ctx.edit_origin(content=nonetxt)
                                                await ctx.send("`enchance chose`")
                                                try:
                                                        string_enchance_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                                        enchance = str(string_enchance_input.content)
                                                        await ctx.send("__enchance : __ `" + enchance + "`")
                                                except:
                                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                        enchance = "none"
                                        third_weapon_enchance = st.loadEnchance(enchance)
                                        weapon_constructor03 = {"name" : third_weapon_name,
                                                                "description": third_weapon_description,
                                                                "level": third_weapon_level,
                                                                "type" : third_weapon_type ,
                                                                "enchance" : third_weapon_enchance,
                                                                "enchance_name" : enchance}
                                if button_ctx.custom_id == "not_generate":
                                        await button_ctx.edit_origin(content=nonetxt)
                                        weapon_constructor03 = {"name" : nonetxt,
                                                                "description": nonetxt,
                                                                "level": 0,
                                                                "type" : rp.WeaponTypeClass("none","none") ,
                                                                "enchance" : [rp.StatisticsClass("") for x in range(9)],
                                                                "enchance_name" : nonetxt}
                                display_character.constructor_weapon03 = weapon_constructor03
                                display_character.weapon03 = rp.WeaponClass(weapon_constructor03["name"],weapon_constructor03["description"],weapon_constructor03["level"],weapon_constructor03["type"],weapon_constructor03["enchance"],weapon_constructor03["enchance_name"])
                                st.saveCharacter(display_character,user_name,display_name)
                                await ctx.send("`moddifications register`")
                                pass
                        if update_type.values[0] == "first accessory":
                                await update_type.send(nonetxt)
                                await ctx.send("`do you want to generate a new accessory`")
                                my_buttons = [create_button(style=ButtonStyle.blue,
                                                            label="generate a new accessory",
                                                            custom_id="generate"),
                                              create_button(style=ButtonStyle.blue,
                                                            label="dont generate a new accessory",
                                                            custom_id="not_generate")]
                                button_raw = create_actionrow(*my_buttons)
                                fait_choix = await ctx.send("`Push for generation : `", components=[button_raw])
                                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                if button_ctx.custom_id == "generate":
                                        await button_ctx.edit_origin(content=nonetxt)
                                        await ctx.send("`__enter the name of the 1st accessory(not the type of the accessory , the name)__`")
                                        try:
                                                first_accessory_name_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                                first_accessory_name = str(first_accessory_name_input.content)
                                                await ctx.send("__name of the 1st accessory : __ `" + first_accessory_name + "`")
                                        except:
                                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                first_accessory_name = nonetxt
                                        await ctx.send("`__enter the description of the 1st accessory__`")
                                        try:
                                                first_accessory_description_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                                first_accessory_description = str(first_accessory_description_input.content)
                                                await ctx.send("__descrition of the 1st accessory : __ `" + first_accessory_description + "`")
                                        except:
                                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                first_accessory_description = nonetxt
                                        await ctx.send("`__enter the level of the 1st accessory__`")
                                        try:
                                                first_accessory_level_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                                first_accessory_level = int(first_accessory_level_input.content)
                                                await ctx.send("__level of the 1st accessory : __ `" + str(first_accessory_level) + "`")
                                        except:
                                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                first_accessory_level = 0
                                        await ctx.send("`__enter the type of the 1st accessory__`")
                                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                                    label="display the equipement-type list",
                                                                    custom_id="display"),
                                                      create_button(style=ButtonStyle.blue,
                                                                    label="not display the equipement-type list",
                                                                    custom_id="not_display")]
                                        button_raw = create_actionrow(*my_buttons)
                                        fait_choix = await ctx.send("`Push for the equipement-type list : `", components=[button_raw])
                                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                        if button_ctx.custom_id == "display":
                                                await button_ctx.edit_origin(content=nonetxt)
                                                equipement_list = st.filterEquipementType("accessory_type")
                                                equipement_embed_list = tf.getListEmbedEquipementList(ctx,equipement_list)
                                                for equipement_embed in equipement_embed_list:
                                                        await ctx.send(embed=equipement_embed)
                                                await ctx.send("`equipement chose`")
                                                try:
                                                        string_equipement_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                                        equipement_name = str(string_equipement_input.content)
                                                        await ctx.send("__equipement-type : __ `" + equipement_name + "`")
                                                except:
                                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                        equipement_name = "none"
                                        elif button_ctx.custom_id == "not_display":
                                                await button_ctx.edit_origin(content=nonetxt)
                                                await view_type.send("`equipement-type chose`")
                                                try:
                                                        string_equipement_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                                        equipement_name = str(string_equipement_input.content)
                                                        await ctx.send("__equipement-type : __ `" + equipement_name + "`")
                                                except:
                                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                        equipement_name = "none"
                                        first_accessory_type = st.loadEquipement(equipement_name)
                                        await ctx.send("`__enter the enchance of the 1st accessory__`")
                                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                                    label="display the enchance list",
                                                                    custom_id="display"),
                                                      create_button(style=ButtonStyle.blue,
                                                                    label="not display the enchance list",
                                                                    custom_id="not_display")]
                                        button_raw = create_actionrow(*my_buttons)
                                        fait_choix = await ctx.send("`Push for the enchance list : `", components=[button_raw])
                                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                        if button_ctx.custom_id == "display":
                                                await button_ctx.edit_origin(content=nonetxt)
                                                enchance_list = list((st.loadDict("database\EnchancesDatabase.obj")).keys())
                                                enchance_embed_list = tf.getListEmbedEnchancesList(ctx,enchance_list)
                                                for enchance_embed in enchance_embed_list:
                                                        await ctx.send(embed=enchance_embed)
                                                await ctx.send("`enchance chose`")
                                                try:
                                                        string_enchance_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                                        enchance = str(string_enchance_input.content)
                                                        await ctx.send("__enchance : __ `" + enchance + "`")
                                                except:
                                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                        enchance = "none"
                                        elif button_ctx.custom_id == "not_display":
                                                await button_ctx.edit_origin(content=nonetxt)
                                                await button_ctx.edit_origin(content=nonetxt)
                                                await ctx.send("`enchance chose`")
                                                try:
                                                        string_enchance_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                                        enchance = str(string_enchance_input.content)
                                                        await ctx.send("__enchance : __ `" + enchance + "`")
                                                except:
                                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                        enchance = "none"
                                        first_accessory_enchance = st.loadEnchance(enchance)
                                        accessory_constructor01 = {"name" : first_accessory_name,
                                                                   "description": first_accessory_description,
                                                                   "level": first_accessory_level,
                                                                   "type" : first_accessory_type ,
                                                                   "enchance" : first_accessory_enchance,
                                                                   "enchance_name" : enchance}
                                if button_ctx.custom_id == "not_generate":
                                        await button_ctx.edit_origin(content=nonetxt)
                                        accessory_constructor01 = {"name" : nonetxt,
                                                                   "description": nonetxt,
                                                                   "level": 0,
                                                                   "type" : rp.AccessoryClassTypeClass("none","none") ,
                                                                   "enchance" : [rp.StatisticsClass("") for x in range(9)],
                                                                   "enchance_name" : nonetxt}
                                display_character.constructor_acces01 = accessory_constructor01
                                display_character.accessorry01 = rp.AccessoryClass(accessory_constructor01["name"],accessory_constructor01["description"],accessory_constructor01["level"],accessory_constructor01["type"],accessory_constructor01["enchance"],accessory_constructor01["enchance_name"])
                                display_character.refreshEquipement()
                                display_character.refreshOrga()
                                st.saveCharacter(display_character,user_name,display_name)
                                await ctx.send("`moddifications register`")
                                pass
                        if update_type.values[0] == "second accessory":
                                await update_type.send(nonetxt)
                                await ctx.send("`do you want to generate a new accessory`")
                                my_buttons = [create_button(style=ButtonStyle.blue,
                                                            label="generate a new accessory",
                                                            custom_id="generate"),
                                              create_button(style=ButtonStyle.blue,
                                                            label="dont generate a new accessory",
                                                            custom_id="not_generate")]
                                button_raw = create_actionrow(*my_buttons)
                                fait_choix = await ctx.send("`Push for generation : `", components=[button_raw])
                                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                if button_ctx.custom_id == "generate":
                                        await button_ctx.edit_origin(content=nonetxt)
                                        await ctx.send("`__enter the name of the 2nd accessory(not the type of the accessory , the name)__`")
                                        try:
                                                second_accessory_name_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                                second_accessory_name = str(second_accessory_name_input.content)
                                                await ctx.send("__name of the 2nd accessory : __ `" + second_accessory_name + "`")
                                        except:
                                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                second_accessory_name = nonetxt
                                        await ctx.send("`__enter the description of the 2nd accessory__`")
                                        try:
                                                second_accessory_weapon_description_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                                second_accessory_description = str(second_accessory_weapon_description_input.content)
                                                await ctx.send("__descrition of the 2nd accessory : __ `" + second_accessory_weapon_description + "`")
                                        except:
                                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                second_accessory_description = nonetxt
                                        await ctx.send("`__enter the level of the 2nd accessory__`")
                                        try:
                                                second_accessory_level_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                                second_accessory_level = int(second_accessory_level_input.content)
                                                await ctx.send("__level of the 2nd accessory : __ `" + str(second_accessory_level) + "`")
                                        except:
                                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                second_accessory_level = 0
                                        await ctx.send("`__enter the type of the 2nd accessory__`")
                                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                                    label="display the equipement-type list",
                                                                    custom_id="display"),
                                                      create_button(style=ButtonStyle.blue,
                                                                    label="not display the equipement-type list",
                                                                    custom_id="not_display")]
                                        button_raw = create_actionrow(*my_buttons)
                                        fait_choix = await ctx.send("`Push for the equipement-type list : `", components=[button_raw])
                                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                        if button_ctx.custom_id == "display":
                                                await button_ctx.edit_origin(content=nonetxt)
                                                equipement_list = st.filterEquipementType("accessory_type")
                                                equipement_embed_list = tf.getListEmbedEquipementList(ctx,equipement_list)
                                                for equipement_embed in equipement_embed_list:
                                                        await ctx.send(embed=equipement_embed)
                                                await ctx.send("`equipement chose`")
                                                try:
                                                        string_equipement_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                                        equipement_name = str(string_equipement_input.content)
                                                        await ctx.send("__equipement-type : __ `" + equipement_name + "`")
                                                except:
                                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                        equipement_name = "none"
                                        elif button_ctx.custom_id == "not_display":
                                                await button_ctx.edit_origin(content=nonetxt)
                                                await view_type.send("`equipement-type chose`")
                                                try:
                                                        string_equipement_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                                        equipement_name = str(string_equipement_input.content)
                                                        await ctx.send("__equipement-type : __ `" + equipement_name + "`")
                                                except:
                                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                        equipement_name = "none"
                                        second_accessory_type = st.loadEquipement(equipement_name)
                                        await ctx.send("`__enter the enchance of the 2nd accessory__`")
                                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                                    label="display the enchance list",
                                                                    custom_id="display"),
                                                      create_button(style=ButtonStyle.blue,
                                                                    label="not display the enchance list",
                                                                    custom_id="not_display")]
                                        button_raw = create_actionrow(*my_buttons)
                                        fait_choix = await ctx.send("`Push for the enchance list : `", components=[button_raw])
                                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                        if button_ctx.custom_id == "display":
                                                await button_ctx.edit_origin(content=nonetxt)
                                                enchance_list = list((st.loadDict("database\EnchancesDatabase.obj")).keys())
                                                enchance_embed_list = tf.getListEmbedEnchancesList(ctx,enchance_list)
                                                for enchance_embed in enchance_embed_list:
                                                        await ctx.send(embed=enchance_embed)
                                                await ctx.send("`enchance chose`")
                                                try:
                                                        string_enchance_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                                        enchance = str(string_enchance_input.content)
                                                        await ctx.send("__enchance : __ `" + enchance + "`")
                                                except:
                                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                        enchance = "none"
                                        elif button_ctx.custom_id == "not_display":
                                                await button_ctx.edit_origin(content=nonetxt)
                                                await button_ctx.edit_origin(content=nonetxt)
                                                await ctx.send("`enchance chose`")
                                                try:
                                                        string_enchance_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                                        enchance = str(string_enchance_input.content)
                                                        await ctx.send("__enchance : __ `" + enchance + "`")
                                                except:
                                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                        enchance = "none"
                                        second_accessory_enchance = st.loadEnchance(enchance)
                                        accessory_constructor02 = {"name" : second_accessory_name,
                                                                   "description": second_accessory_description,
                                                                   "level": second_accessory_level,
                                                                   "type" : second_accessory_type ,
                                                                   "enchance" : second_accessory_enchance,
                                                                   "enchance_name" : enchance}
                                if button_ctx.custom_id == "not_generate":
                                        await button_ctx.edit_origin(content=nonetxt)
                                        accessory_constructor02 = {"name" : nonetxt,
                                                                   "description": nonetxt,
                                                                   "level": 0,
                                                                   "type" : rp.AccessoryClassTypeClass("none","none") ,
                                                                   "enchance" : [rp.StatisticsClass("") for x in range(9)],
                                                                   "enchance_name" : nonetxt}
                                display_character.constructor_acces02 = accessory_constructor02
                                display_character.accessorry02 = rp.AccessoryClass(accessory_constructor02["name"],accessory_constructor02["description"],accessory_constructor02["level"],accessory_constructor02["type"],accessory_constructor02["enchance"],accessory_constructor02["enchance_name"])
                                display_character.refreshEquipement()
                                display_character.refreshOrga()
                                st.saveCharacter(display_character,user_name,display_name)
                                await ctx.send("`moddifications register`")
                                pass
                        if update_type.values[0] == "armor":
                                await update_type.send(nonetxt)
                                await ctx.send("`do you want to generate a new armor`")
                                my_buttons = [create_button(style=ButtonStyle.blue,
                                                            label="generate a new armor",
                                                            custom_id="generate"),
                                              create_button(style=ButtonStyle.blue,
                                                            label="dont generate a new armor",
                                                            custom_id="not_generate")]
                                button_raw = create_actionrow(*my_buttons)
                                fait_choix = await ctx.send("`Push for generation : `", components=[button_raw])
                                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                if button_ctx.custom_id == "generate":
                                        await button_ctx.edit_origin(content=nonetxt)
                                        await ctx.send("`__enter the name of the armor(not the type of the armor , the name)__`")
                                        try:
                                                armor_name_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                                armor_name = str(armor_name_input.content)
                                                await ctx.send("__name of the armor : __ `" + armor_name + "`")
                                        except:
                                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                armor_name = nonetxt
                                        await ctx.send("`__enter the description of the armor__`")
                                        try:
                                                armor_description_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                                armor_description = str(armor_description_input.content)
                                                await ctx.send("__descrition of the armor : __ `" + armor_description + "`")
                                        except:
                                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                armor_description = nonetxt
                                        await ctx.send("`__enter the level of the armor__`")
                                        try:
                                                armor_level_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                                armor_level = int(armor_level_input.content)
                                                await ctx.send("__level of the armor : __ `" + str(armor_level) + "`")
                                        except:
                                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                armor_level = 0
                                        await ctx.send("`__enter the type of the armor__`")
                                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                                    label="display the equipement-type list",
                                                                    custom_id="display"),
                                                      create_button(style=ButtonStyle.blue,
                                                                    label="not display the equipement-type list",
                                                                    custom_id="not_display")]
                                        button_raw = create_actionrow(*my_buttons)
                                        fait_choix = await ctx.send("`Push for the equipement-type list : `", components=[button_raw])
                                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                        if button_ctx.custom_id == "display":
                                                await button_ctx.edit_origin(content=nonetxt)
                                                equipement_list = st.filterEquipementType("armor_type")
                                                equipement_embed_list = tf.getListEmbedEquipementList(ctx,equipement_list)
                                                for equipement_embed in equipement_embed_list:
                                                        await ctx.send(embed=equipement_embed)
                                                await ctx.send("`equipement chose`")
                                                try:
                                                        string_equipement_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                                        equipement_name = str(string_equipement_input.content)
                                                        await ctx.send("__equipement-type : __ `" + equipement_name + "`")
                                                except:
                                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                        equipement_name = "none"
                                        elif button_ctx.custom_id == "not_display":
                                                await button_ctx.edit_origin(content=nonetxt)
                                                await view_type.send("`equipement-type chose`")
                                                try:
                                                        string_equipement_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                                        equipement_name = str(string_equipement_input.content)
                                                        await ctx.send("__equipement-type : __ `" + equipement_name + "`")
                                                except:
                                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                        equipement_name = "none"
                                        armor_type = st.loadEquipement(equipement_name)
                                        await ctx.send("`__enter the enchance of the armor__`")
                                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                                    label="display the enchance list",
                                                                    custom_id="display"),
                                                      create_button(style=ButtonStyle.blue,
                                                                    label="not display the enchance list",
                                                                    custom_id="not_display")]
                                        button_raw = create_actionrow(*my_buttons)
                                        fait_choix = await ctx.send("`Push for the enchance list : `", components=[button_raw])
                                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                        if button_ctx.custom_id == "display":
                                                await button_ctx.edit_origin(content=nonetxt)
                                                enchance_list = list((st.loadDict("database\EnchancesDatabase.obj")).keys())
                                                enchance_embed_list = tf.getListEmbedEnchancesList(ctx,enchance_list)
                                                for enchance_embed in enchance_embed_list:
                                                        await ctx.send(embed=enchance_embed)
                                                await ctx.send("`enchance chose`")
                                                try:
                                                        string_enchance_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                                        enchance = str(string_enchance_input.content)
                                                        await ctx.send("__enchance : __ `" + enchance + "`")
                                                except:
                                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                        enchance = "none"
                                        elif button_ctx.custom_id == "not_display":
                                                await button_ctx.edit_origin(content=nonetxt)
                                                await button_ctx.edit_origin(content=nonetxt)
                                                await ctx.send("`enchance chose`")
                                                try:
                                                        string_enchance_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                                        enchance = str(string_enchance_input.content)
                                                        await ctx.send("__enchance : __ `" + enchance + "`")
                                                except:
                                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                        enchance = "none"
                                        armor_enchance = st.loadEnchance(enchance)
                                        armor_constructor = {"name" : armor_name,
                                                             "description": armor_description,
                                                             "level": armor_level,
                                                             "type" : armor_type ,
                                                             "enchance" : armor_enchance,
                                                             "enchance_name" : enchance}
                                if button_ctx.custom_id == "not_generate":
                                        await button_ctx.edit_origin(content=nonetxt)
                                        armor_constructor = {"name" : nonetxt,
                                                             "description": nonetxt,
                                                             "level": 0,
                                                             "type" : rp.ArmorClassTypeClass("none","none") ,
                                                             "enchance" : [rp.StatisticsClass("") for x in range(9)],
                                                             "enchance_name" : nonetxt}
                                display_character.constructor_armor = armor_constructor
                                display_character.armor = rp.ArmorClass(armor_constructor["name"],armor_constructor["description"],armor_constructor["level"],armor_constructor["type"],armor_constructor["enchance"],armor_constructor["enchance_name"])
                                display_character.refreshEquipement()
                                display_character.refreshOrga()
                                st.saveCharacter(display_character,user_name,display_name)
                                await ctx.send("`moddifications register`")
                                pass
                        if update_type.values[0] == "user_level":
                                await update_type.send(nonetxt)
                                update_level_select = tf.getListSelection(ctx,"chose the level of the character",[str(x) for x in range(21)],[str(x) for x in range(21)]) 
                                fait_choix = await ctx.send("`chose the level of the character : `", components=[create_actionrow( update_level_select)])
                                update_level = await wait_for_component(notlolabot.bot, components= update_level_select, check=check)
                                await update_level.send(nonetxt)
                                await ctx.send("`__enter the max hp of the character__`")
                                try:
                                        char_max_hp_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                        char_max_hp = int(str(char_max_hp_input.content))
                                        await ctx.send("__max hp of the character : __ `" + str(char_max_hp) + "`")
                                except:
                                        await ctx.send("`Erreur sur la commande valeure de base fixée a " + str(display_character.life[1])+ " , si cela ne vous convient pas , veuillez reiterer la commande.`")
                                        char_max_hp = display_character.life[1]
                                display_character.life = (display_character.life[0],char_max_hp)
                                display_character.level = int(update_level.values[0])
                                display_character.refreshEquipement()
                                display_character.refreshOrga()
                                st.saveCharacter(display_character,user_name,display_name)
                                await ctx.send("`moddifications register`")
                                pass
                        if update_type.values[0] == "user_max_life":
                                await update_type.send(nonetxt)
                                await ctx.send("`__enter the max hp of the character__`")
                                try:
                                        char_max_hp_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                        char_max_hp = int(str(char_max_hp_input.content))
                                        await ctx.send("__max hp of the character : __ `" + str(char_max_hp) + "`")
                                except:
                                        await ctx.send("`Erreur sur la commande valeure de base fixée a " + str(display_character.life[1])+ " , si cela ne vous convient pas , veuillez reiterer la commande.`")
                                        char_max_hp = display_character.life[1]
                                display_character.life = (display_character.life[0],char_max_hp)
                                display_character.refreshEquipement()
                                display_character.refreshOrga()
                                st.saveCharacter(display_character,user_name,display_name)
                                await ctx.send("`moddifications register`")
                                pass
                        if update_type.values[0] == "race":
                                await update_type.send(nonetxt)
                                await register_type.send("`__enter the race name of the character__`")
                                my_buttons = [create_button(style=ButtonStyle.blue,
                                                            label="display the race list",
                                                            custom_id="display"),
                                              create_button(style=ButtonStyle.blue,
                                                            label="not display the race list",
                                                            custom_id="not_display")]
                                button_raw = create_actionrow(*my_buttons)
                                fait_choix = await ctx.send("`Push for the race list : `", components=[button_raw])
                                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                if button_ctx.custom_id == "display":
                                        await button_ctx.edit_origin(content=nonetxt)
                                        race_list = (st.loadDict("database\RacesDatabase.obj")).keys()
                                        race_embed_list = tf.getListEmbedRaceList(ctx,race_list)
                                        for race_embed in race_embed_list:
                                                await ctx.send(embed=race_embed)
                                        await ctx.send("`race chose`")
                                        try:
                                                string_race_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                                race_name = str(string_race_input.content)
                                                await ctx.send("__race : __ `" + race_name + "`")
                                        except:
                                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                race_name = "none"
                                elif button_ctx.custom_id == "not_display":
                                        await button_ctx.edit_origin(content=nonetxt)
                                        await ctx.send("`race chose`")
                                        try:
                                                string_race_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                                race_name = str(string_race_input.content)
                                                await ctx.send("__race : __ `" + race_name + "`")
                                        except:
                                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                race_name = "none"
                                if race_name != "none":
                                        char_race = st.loadRace(race_name)
                                else:
                                        char_race = rp.RaceClass("","","",{})

                                display_character.race = char_race
                                display_character.refreshEquipement()
                                display_character.refreshOrga()
                                st.saveCharacter(display_character,user_name,display_name)
                                await ctx.send("`moddifications register`")
                                pass
                        if update_type.values[0] == "classe":
                                await update_type.send(nonetxt)
                                await ctx.send("`__enter the classe name of the character(enter none if your character dont have a class)__`")
                                my_buttons = [create_button(style=ButtonStyle.blue,
                                                            label="display the classe list",
                                                            custom_id="display"),
                                              create_button(style=ButtonStyle.blue,
                                                            label="not display the classe list",
                                                            custom_id="not_display")]
                                button_raw = create_actionrow(*my_buttons)
                                fait_choix = await ctx.send("`Push for the classe list : `", components=[button_raw])
                                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                if button_ctx.custom_id == "display":
                                        await button_ctx.edit_origin(content=nonetxt)
                                        classe_list = (st.loadDict("database\ClassDatabase.obj")).keys()
                                        classe_embed_list = tf.getListEmbedClasseList(ctx,classe_list)
                                        for classe_embed in classe_embed_list:
                                                await ctx.send(embed=classe_embed)
                                        await ctx.send("`classe chose`")
                                        try:
                                                string_classe_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                                classe_name = str(string_classe_input.content)
                                                await ctx.send("__classe : __ `" + classe_name + "`")
                                        except:
                                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                classe_name = "none"
                                elif button_ctx.custom_id == "not_display":
                                        await button_ctx.edit_origin(content=nonetxt)
                                        await ctx.send("`classe chose`")
                                        try:
                                                string_classe_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                                classe_name = str(string_classe_input.content)
                                                await ctx.send("__classe : __ `" + classe_name + "`")
                                        except:
                                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                classe_name = "none"
                                if classe_name != "none":
                                        char_classe = st.loadClasse(classe_name)
                                else:
                                        char_classe = rp.ClasseClass("","","",{},"")
                                display_character.classe = char_classe
                                display_character.refreshEquipement()
                                display_character.refreshOrga()
                                st.saveCharacter(display_character,user_name,display_name)
                                await ctx.send("`moddifications register`")
                                pass
                        if update_type.values[0] == "capital":
                                await update_type.send(nonetxt)
                                await ctx.send("`__enter the capital in gold piece of the character__`")
                                try:
                                        char_capital_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                        char_capital = int(str(char_capital_input.content))
                                        await ctx.send("__capital of the character : __ `" + str(char_capital) + " golds`")
                                except:
                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        char_capital = display_character.capital
                                display_character.capital = char_capital
                                display_character.refreshEquipement()
                                display_character.refreshOrga()
                                st.saveCharacter(display_character,user_name,display_name)
                                await ctx.send("`moddifications register`")
                                pass
                if button_ctx.custom_id == "display the history":
                        await button_ctx.edit_origin(content=nonetxt)
                        embed_list = tf.getListLoreCharacterEmbedImage(ctx,display_character.lore_history,display_character)
                        for embed in embed_list:
                                await ctx.send(embed=embed)
                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                    label="display the knoledge list",
                                                    custom_id="display")]
                        button_raw = create_actionrow(*my_buttons)
                        fait_choix = await ctx.send("`Push for the knoledge list : `", components=[button_raw])
                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                        if button_ctx.custom_id == "display":
                                await button_ctx.edit_origin(content=nonetxt)
                                embed_list = tf.getListKnoledgeEmbedImageList(ctx,display_character.craft_knowledge)
                                for my_embed in embed_list:
                                        await ctx.send(embed=my_embed)
                                my_buttons = [create_button(style=ButtonStyle.green,
                                                            label="update the list",
                                                            custom_id="update"),
                                              create_button(style=ButtonStyle.green,
                                                            label="ad a item",
                                                            custom_id="ad"),
                                              create_button(style=ButtonStyle.green,
                                                            label="delete a item",
                                                            custom_id="delete")]
                                button_raw = create_actionrow(*my_buttons)
                                fait_choix = await ctx.send("`Push the button for display or change a option : `", components=[button_raw])
                                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                if button_ctx.custom_id == "update":
                                        await button_ctx.edit_origin(content=nonetxt)
                                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                                    label="display the item list",
                                                                    custom_id="display"),
                                                      create_button(style=ButtonStyle.blue,
                                                                    label="not display the item list",
                                                                    custom_id="not_display")]
                                        button_raw = create_actionrow(*my_buttons)
                                        fait_choix = await ctx.send("`Push for the item list : `", components=[button_raw])
                                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                        if button_ctx.custom_id == "display":
                                                await button_ctx.edit_origin(content=nonetxt)
                                                item_list = list((st.loadDict(r"database\ItemsDatabase.obj")).keys())
                                                item_embed_list = tf.getListItemEmbedImageList(ctx,item_list)
                                                for item_embed in item_embed_list:
                                                        await ctx.send(embed=item_embed)
                                                await ctx.send("`item01`|`item02`|.....|`itemN`")
                                                try:
                                                        item_name_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                                        item_names = str(item_name_input.content)
                                                except:
                                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                        item_names = "none"
                                        elif button_ctx.custom_id == "not_display":
                                                await button_ctx.edit_origin(content=nonetxt)
                                                await ctx.send("`item01`|`item02`|.....|`itemN`")
                                                try:
                                                        item_name_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                                        item_names = str(item_name_input.content)
                                                except:
                                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                        item_names = "none"
                                        if item_names != "none":
                                                knoledge_list = item_names.split("|")
                                                display_character.craft_knowledge = knoledge_list
                                                st.saveCharacter(display_character,user_name,display_name)    
                                if button_ctx.custom_id == "ad":
                                        await button_ctx.edit_origin(content=nonetxt)
                                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                                    label="display the item list",
                                                                    custom_id="display"),
                                                      create_button(style=ButtonStyle.blue,
                                                                    label="not display the item list",
                                                                    custom_id="not_display")]
                                        button_raw = create_actionrow(*my_buttons)
                                        fait_choix = await ctx.send("`Push for the item list : `", components=[button_raw])
                                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                        if button_ctx.custom_id == "display":
                                                await button_ctx.edit_origin(content=nonetxt)
                                                item_list = list((st.loadDict(r"database\ItemsDatabase.obj")).keys())
                                                item_embed_list = tf.getListItemEmbedImageList(ctx,item_list)
                                                for item_embed in item_embed_list:
                                                        await ctx.send(embed=item_embed)
                                                await ctx.send("`enter the item name :`")
                                                try:
                                                        item_name_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                                        item_name = str(item_name_input.content)
                                                        await ctx.send("__name : __ `" + item_name + "`")
                                                except:
                                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        elif button_ctx.custom_id == "not_display":
                                                await button_ctx.edit_origin(content=nonetxt)
                                                await ctx.send("`enter the item name :`")
                                                try:
                                                        item_name_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                                        item_name = str(item_name_input.content)
                                                        await ctx.send("__name : __ `" + item_name + "`")
                                                except:
                                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        if item_name != "none":
                                                display_character.craft_knowledge.append(item_name)
                                                st.saveCharacter(display_character,user_name,display_name)   
                                if button_ctx.custom_id == "delete":
                                        await button_ctx.edit_origin(content=nonetxt)
                                        await ctx.send("`enter the item name :`")
                                        try:
                                                item_name_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                                item_name = str(item_name_input.content)
                                                await ctx.send("__name : __ `" + item_name + "`")
                                        except:
                                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        if item_name != "none":
                                                display_character.craft_knowledge.pop(st.getIndice(display_character.craft_knowledge,item_name))
                                                st.saveCharacter(display_character,user_name,display_name)
                if button_ctx.custom_id == "refresh":
                        await button_ctx.edit_origin(content=nonetxt)
                        char_name = display_character.name
                        char_description = display_character.presentation
                        char_history = display_character.lore_history
                        char_nickname = display_character.nickname
                        char_titles = display_character.title_list
                        char_background = display_character.background
                        char_allignement = display_character.alignement
                        char_max_hp = display_character.life[1]
                        char_level = display_character.level
                        if display_character.race.name != "":
                                char_race = st.loadRace(display_character.race.name)
                        else:
                                char_race = display_character.race
                        if display_character.classe.name != "":
                                char_classe = st.loadClasse(display_character.classe.name)
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
                        for name in display_character.inventory.keys():
                                char_inventory[name] = st.loadItem(name)
                                char_inventory[name].quantity = display_character.inventory[name].quantity
                                pass
                        fresh_character = rp.CharacterClass(char_name,char_description,char_history,char_nickname,char_titles,char_background,char_allignement,char_max_hp,char_level,char_race,char_classe,char_basic_stats,char_constructor_weapon01,char_constructor_weapon02,char_constructor_weapon03,char_constructor_acces01,char_constructor_acces02, char_constructor_armor,char_other_stats,char_image_path,char_inventory,char_capital,char_languages,char_autority,char_organisation)
                        st.saveCharacter(fresh_character,user_name,display_name)
                        await ctx.send("`refresh`")
                if button_ctx.custom_id == "display inventory":
                        await button_ctx.edit_origin(content=nonetxt)
                        selection = ["inventory","knoledges","first weapon","second weapon","third weapon","first accessory","second accessory","armor"]
                        inventory_type_select = tf.getListSelection(ctx,"chose the inventory to see",selection,selection) 
                        fait_choix = await ctx.send("`chose the inventory to see : `", components=[create_actionrow(inventory_type_select)])
                        inventory_type = await wait_for_component(notlolabot.bot, components=inventory_type_select, check=check)
                        if inventory_type.values[0] == "knoledges":
                                await inventory_type.send(nonetxt)
                                embed_list = tf.getListKnoledgeEmbedImageList(ctx,display_character.craft_knowledge)
                                for my_embed in embed_list:
                                        await ctx.send(embed=my_embed)
                                my_buttons = [create_button(style=ButtonStyle.green,
                                                            label="update the list",
                                                            custom_id="update"),
                                              create_button(style=ButtonStyle.green,
                                                            label="ad a item",
                                                            custom_id="ad"),
                                              create_button(style=ButtonStyle.green,
                                                            label="delete a item",
                                                            custom_id="delete")]
                                button_raw = create_actionrow(*my_buttons)
                                fait_choix = await ctx.send("`Push the button for display or change a option : `", components=[button_raw])
                                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                if button_ctx.custom_id == "update":
                                        await button_ctx.edit_origin(content=nonetxt)
                                        if button_ctx.custom_id == "display":
                                                await button_ctx.edit_origin(content=nonetxt)
                                                item_list = list((st.loadDict(r"database\ItemsDatabase.obj")).keys())
                                                item_embed_list = tf.getListItemEmbedImageList(ctx,item_list)
                                                for item_embed in item_embed_list:
                                                        await ctx.send(embed=item_embed)
                                                await ctx.send("`item01`|`item02`|.....|`itemN`")
                                                try:
                                                        item_name_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                                        item_names = str(item_name_input.content)
                                                except:
                                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                        item_names = "none"
                                        elif button_ctx.custom_id == "not_display":
                                                await button_ctx.edit_origin(content=nonetxt)
                                                await ctx.send("`item01`|`item02`|.....|`itemN`")
                                                try:
                                                        item_name_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                                        item_names = str(item_name_input.content)
                                                except:
                                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                        item_names = "none"
                                        if item_names != "none":
                                                knoledge_list = item_names.split("|")
                                                display_character.craft_knowledge = knoledge_list
                                                st.saveCharacter(display_character,user_name,display_name)    
                                if button_ctx.custom_id == "ad":
                                        await button_ctx.edit_origin(content=nonetxt)
                                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                                    label="display the item list",
                                                                    custom_id="display"),
                                                      create_button(style=ButtonStyle.blue,
                                                                    label="not display the item list",
                                                                    custom_id="not_display")]
                                        button_raw = create_actionrow(*my_buttons)
                                        fait_choix = await ctx.send("`Push for the item list : `", components=[button_raw])
                                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                        if button_ctx.custom_id == "display":
                                                await button_ctx.edit_origin(content=nonetxt)
                                                item_list = list((st.loadDict(r"database\ItemsDatabase.obj")).keys())
                                                item_embed_list = tf.getListItemEmbedImageList(ctx,item_list)
                                                for item_embed in item_embed_list:
                                                        await ctx.send(embed=item_embed)
                                                await ctx.send("`enter the item name :`")
                                                try:
                                                        item_name_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                                        item_name = str(item_name_input.content)
                                                        await ctx.send("__name : __ `" + item_name + "`")
                                                except:
                                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        elif button_ctx.custom_id == "not_display":
                                                await button_ctx.edit_origin(content=nonetxt)
                                                await ctx.send("`enter the item name :`")
                                                try:
                                                        item_name_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                                        item_name = str(item_name_input.content)
                                                        await ctx.send("__name : __ `" + item_name + "`")
                                                except:
                                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        if item_name != "none":
                                                display_character.craft_knowledge.append(item_name)
                                                st.saveCharacter(display_character,user_name,display_name)   
                                if button_ctx.custom_id == "delete":
                                        await button_ctx.edit_origin(content=nonetxt)
                                        try:
                                                item_name_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                                item_name = str(item_name_input.content)
                                                await ctx.send("__name : __ `" + item_name + "`")
                                        except:
                                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        if item_name != "none":
                                                display_character.craft_knowledge.pop(st.getIndice(display_character.craft_knowledge,item_name))
                                                st.saveCharacter(display_character,user_name,display_name)
                        if inventory_type.values[0] == "inventory":
                                await inventory_type.send(nonetxt)
                                embed_list = tf.getListInventoryCharacterEmbedImage(ctx,display_character)
                                for embed in embed_list:
                                        await ctx.send(embed=embed)
                                my_buttons = [create_button(style=ButtonStyle.blue,
                                                            label="use a item",
                                                            custom_id="use a item"),
                                              create_button(style=ButtonStyle.blue,
                                                            label="left the display",
                                                            custom_id="left the display")]
                                button_raw = create_actionrow(*my_buttons)
                                fait_choix = await ctx.send("`Push the button for display or change a option : `", components=[button_raw])
                                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                if button_ctx.custom_id == "use a item":
                                        await button_ctx.edit_origin(content=nonetxt)
                                        await ctx.send("`__enter the name of the consummable to use__`")
                                        try:
                                                item_name_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                                item_name = str(item_name_input.content)
                                        except:
                                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                item_name = "none"
                                        if item_name != "none":
                                                if display_character.inventory[item_name].quantity > 0:
                                                        display_character.inventory[item_name].quantity = display_character.inventory[item_name].quantity - 1
                                                        if display_character.life[0] + display_character.inventory[item_name].life > display_character.life[1]:
                                                                display_character.life = (display_character.life[1],display_character.life[1])
                                                        else:
                                                                display_character.life = (display_character.life[0] + display_character.inventory[item_name].life,display_character.life[1])
                                                        st.saveCharacter(display_character,user_name,display_name)
                                                        st.tickUpdate()
                                                        await ctx.send("`" + item_name + "` : **used**.")
                                                else:
                                                        await ctx.send("`" + item_name + "` : **can't be used**.")
                                if button_ctx.custom_id == "left the display":
                                        await button_ctx.edit_origin(content=nonetxt)
                        if inventory_type.values[0] == "first weapon":
                                await inventory_type.send(nonetxt)
                                embed = tf.getEmbedImageCharacterEquipement(ctx,display_character.weapon01)
                                await ctx.send(embed=embed)
                                my_buttons = [create_button(style=ButtonStyle.green,
                                                            label="change the level of the weapon",
                                                            custom_id="change the level")]
                                button_raw = create_actionrow(*my_buttons)
                                fait_choix = await ctx.send("`Push the button for display or change the level : `", components=[button_raw])
                                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                if button_ctx.custom_id == "change the level":
                                        await button_ctx.edit_origin(content=nonetxt)
                                        await ctx.send("`__enter the level of the weapon__`")
                                        try:
                                                item_level_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                                item_level = int(item_level_input.content)
                                        except:
                                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                item_level = 1000000
                                        if item_level != 1000000:
                                                display_character.weapon01.updateLevel(item_level)
                                                display_character.constructor_weapon01["level"] = item_level
                                                display_character.refreshEquipement()
                                                display_character.refreshOrga()
                                                st.saveCharacter(display_character,user_name,display_name)
                                                await ctx.send("`moddifications register`")
                        if inventory_type.values[0] == "second weapon":
                                await inventory_type.send(nonetxt)
                                embed = tf.getEmbedImageCharacterEquipement(ctx,display_character.weapon02)
                                await ctx.send(embed=embed)
                                my_buttons = [create_button(style=ButtonStyle.green,
                                                            label="change the level of the weapon",
                                                            custom_id="change the level")]
                                button_raw = create_actionrow(*my_buttons)
                                fait_choix = await ctx.send("`Push the button for display or change the level : `", components=[button_raw])
                                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                if button_ctx.custom_id == "change the level":
                                        await button_ctx.edit_origin(content=nonetxt)
                                        await ctx.send("`__enter the level of the weapon__`")
                                        try:
                                                item_level_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                                item_level = int(item_level_input.content)
                                        except:
                                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                item_level = 1000000
                                        if item_level != 1000000:
                                                display_character.weapon02.updateLevel(item_level)
                                                display_character.constructor_weapon02["level"] = item_level
                                                display_character.refreshEquipement()
                                                display_character.refreshOrga()
                                                st.saveCharacter(display_character,user_name,display_name)
                                                await ctx.send("`moddifications register`")
                        if inventory_type.values[0] == "third weapon":
                                await inventory_type.send(nonetxt)
                                embed = tf.getEmbedImageCharacterEquipement(ctx,display_character.weapon02)
                                await ctx.send(embed=embed)
                                my_buttons = [create_button(style=ButtonStyle.green,
                                                            label="change the level of the weapon",
                                                            custom_id="change the level")]
                                button_raw = create_actionrow(*my_buttons)
                                fait_choix = await ctx.send("`Push the button for display or change the level : `", components=[button_raw])
                                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                if button_ctx.custom_id == "change the level":
                                        await button_ctx.edit_origin(content=nonetxt)
                                        await ctx.send("`__enter the level of the weapon__`")
                                        try:
                                                item_level_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                                item_level = int(item_level_input.content)
                                        except:
                                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                item_level = 1000000
                                        if item_level != 1000000:
                                                display_character.weapon03.updateLevel(item_level)
                                                display_character.constructor_weapon03["level"] = item_level
                                                display_character.refreshEquipement()
                                                display_character.refreshOrga()
                                                st.saveCharacter(display_character,user_name,display_name)
                                                await ctx.send("`moddifications register`")
                        if inventory_type.values[0] == "first accessory":
                                await inventory_type.send(nonetxt)
                                embed = tf.getEmbedImageCharacterEquipement(ctx,display_character.accessorry01)
                                await ctx.send(embed=embed)
                                my_buttons = [create_button(style=ButtonStyle.green,
                                                            label="change the level of the accessory",
                                                            custom_id="change the level")]
                                button_raw = create_actionrow(*my_buttons)
                                fait_choix = await ctx.send("`Push the button for display or change the level : `", components=[button_raw])
                                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                if button_ctx.custom_id == "change the level":
                                        await button_ctx.edit_origin(content=nonetxt)
                                        await ctx.send("`__enter the level of the accessory__`")
                                        try:
                                                item_level_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                                item_level = int(item_level_input.content)
                                        except:
                                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                item_level = 1000000
                                        if item_level != 1000000:
                                                display_character.accessorry01.updateLevel(item_level)
                                                display_character.constructor_acces01["level"] = item_level
                                                display_character.refreshEquipement()
                                                display_character.refreshOrga()
                                                st.saveCharacter(display_character,user_name,display_name)
                                                await ctx.send("`moddifications register`")
                        if inventory_type.values[0] == "second accessory":
                                await inventory_type.send(nonetxt)
                                embed = tf.getEmbedImageCharacterEquipement(ctx,display_character.accessorry02)
                                await ctx.send(embed=embed)
                                my_buttons = [create_button(style=ButtonStyle.green,
                                                            label="change the level of the accessory",
                                                            custom_id="change the level")]
                                button_raw = create_actionrow(*my_buttons)
                                fait_choix = await ctx.send("`Push the button for display or change the level : `", components=[button_raw])
                                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                if button_ctx.custom_id == "change the level":
                                        await button_ctx.edit_origin(content=nonetxt)
                                        await ctx.send("`__enter the level of the accessory__`")
                                        try:
                                                item_level_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                                item_level = int(item_level_input.content)
                                        except:
                                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                item_level = 1000000
                                        if item_level != 1000000:
                                                display_character.accessorry02.updateLevel(item_level)
                                                display_character.constructor_acces02["level"] = item_level
                                                display_character.refreshEquipement()
                                                display_character.refreshOrga()
                                                st.saveCharacter(display_character,user_name,display_name)
                                                await ctx.send("`moddifications register`")
                        if inventory_type.values[0] == "armor":
                                await inventory_type.send(nonetxt)
                                embed = tf.getEmbedImageCharacterEquipement(ctx,display_character.armor)
                                await ctx.send(embed=embed)
                                my_buttons = [create_button(style=ButtonStyle.green,
                                                            label="change the level of the accessory",
                                                            custom_id="change the level")]
                                button_raw = create_actionrow(*my_buttons)
                                fait_choix = await ctx.send("`Push the button for display or change the level : `", components=[button_raw])
                                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                if button_ctx.custom_id == "change the level":
                                        await button_ctx.edit_origin(content=nonetxt)
                                        await ctx.send("`__enter the level of the armor__`")
                                        try:
                                                item_level_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                                item_level = int(item_level_input.content)
                                        except:
                                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                item_level = 1000000
                                        if item_level != 1000000:
                                                display_character.armor.updateLevel(item_level)
                                                display_character.constructor_armor["level"] = item_level
                                                display_character.refreshEquipement()
                                                display_character.refreshOrga()
                                                st.saveCharacter(display_character,user_name,display_name)
                                                await ctx.send("`moddifications register`")
                pass
        else:
                await ctx.send("`Personnage non enregistrer!`")
@notlolabot.bot.command()
async def mycharacters(ctx):
        """mycharacters command for display and select your character in your family board"""
        def check(m):
                return m.author_id == ctx.author.id and m.origin_message.id == fait_choix.id
        def checkMessage(message):
                return message.author == ctx.message.author and ctx.message.channel == message.channel
        mess = await ctx.channel.history(limit = 1).flatten()
        await mess[0].delete()
        display_name = ctx.author.display_name
        user_name = ctx.author.name
        if user_name in st.loadDict(r"database\users_database.obj").keys():
                user = st.loadUser(user_name)
                character_select = tf.getListSelection(ctx,"chose the character", list(user.content[display_name].keys()) ,list(user.content[display_name].keys())) 
                fait_choix = await ctx.send("`Chose the character : `", components=[create_actionrow(character_select)])
                character_type = await wait_for_component(notlolabot.bot, components=character_select, check=check)
                user.sub_pointage = character_type.values[0]
                user.pointage = display_name
                st.saveUser(user)
                await character_type.send("`__character chose :__`  **" + character_type.values[0] + "**")
        else:
                await ctx.send("`Personnage non enregistrer!`")
@notlolabot.bot.command()
async def liteboard(ctx):
        """lite board command for display the lite-board of your character"""
        def check(m):
                return m.author_id == ctx.author.id and m.origin_message.id == fait_choix.id
        def checkMessage(message):
                return message.author == ctx.message.author and ctx.message.channel == message.channel
        display_name = ctx.author.display_name
        user_name = ctx.author.name
        if user_name in st.loadDict(r"database\users_database.obj").keys():
                char_name = st.loadUser(user_name).sub_pointage
                display_character = st.loadCharacter(user_name,display_name,char_name)
                state_of_caster = sktr.getUpdateStateOfCharacter(display_character)
                display_character.state = (state_of_caster,display_character.state[1],display_character.state[2])
                st.saveCharacter(display_character,user_name,display_name)
                display_character = st.loadCharacter(user_name,display_name,char_name)
                my_embed = tf.getLiteEmbedCharacter(ctx,display_character)
                await ctx.send(embed=my_embed)
                my_buttons = [create_button(style=ButtonStyle.green,
                                            label="display skills",
                                            custom_id="display competences"),
                              create_button(style=ButtonStyle.green,
                                            label="display lore",
                                            custom_id="display the history"),
                              create_button(style=ButtonStyle.green,
                                            label="refresh",
                                            custom_id="refresh"),
                              create_button(style=ButtonStyle.green,
                                            label="display inventory",
                                            custom_id="display inventory"),
                              create_button(style=ButtonStyle.green,
                                            label="switch",
                                            custom_id="switch weapon")]
                button_raw = create_actionrow(*my_buttons)
                fait_choix = await ctx.send("`Push the button for display or change a option : `", components=[button_raw])
                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                if button_ctx.custom_id == "display competences":
                        await button_ctx.edit_origin(content=nonetxt)
                        my_embed_list = tf.getFirstEmbedImageCharacterCompetencesList(ctx,display_character)
                        for my_embed in my_embed_list:
                                await ctx.send(embed=my_embed)
                        my_buttons = [create_button(style=ButtonStyle.green,
                                                    label="display the others weapon skills",
                                                    custom_id="others weapon"),
                                      create_button(style=ButtonStyle.green,
                                                    label="display the class and race skills",
                                                    custom_id="class race skills")]
                        button_raw = create_actionrow(*my_buttons)
                        fait_choix = await ctx.send("`Push for display the competences list : `", components=[button_raw])
                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                        if button_ctx.custom_id == "others weapon":
                                await button_ctx.edit_origin(content="`|Weapons Skills|`")
                                my_embed = tf.getFirstEmbedImageCharacterCompetencesListWeapons(ctx,display_character)
                                await ctx.send(embed=my_embed)
                                pass
                        if button_ctx.custom_id == "class race skills":
                                await button_ctx.edit_origin(content="`|Races And Class Skills|`")
                                my_embed = tf.getFirstEmbedImageCharacterCompetencesListRacesClasses(ctx,display_character)
                                await ctx.send(embed=my_embed)
                        pass
                if button_ctx.custom_id == "display the history":
                        await button_ctx.edit_origin(content=nonetxt)
                        embed_list = tf.getListLoreCharacterEmbedImage(ctx,display_character.lore_history,display_character)
                        for embed in embed_list:
                                await ctx.send(embed=embed)
                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                    label="display the knoledge list",
                                                    custom_id="display")]
                        button_raw = create_actionrow(*my_buttons)
                        fait_choix = await ctx.send("`Push for the knoledge list : `", components=[button_raw])
                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                        if button_ctx.custom_id == "display":
                                await button_ctx.edit_origin(content=nonetxt)
                                embed_list = tf.getListKnoledgeEmbedImageList(ctx,display_character.craft_knowledge)
                                for my_embed in embed_list:
                                        await ctx.send(embed=my_embed)
                                my_buttons = [create_button(style=ButtonStyle.green,
                                                            label="update the list",
                                                            custom_id="update"),
                                              create_button(style=ButtonStyle.green,
                                                            label="ad a item",
                                                            custom_id="ad"),
                                              create_button(style=ButtonStyle.green,
                                                            label="delete a item",
                                                            custom_id="delete")]
                                button_raw = create_actionrow(*my_buttons)
                                fait_choix = await ctx.send("`Push the button for display or change a option : `", components=[button_raw])
                                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                if button_ctx.custom_id == "update":
                                        await button_ctx.edit_origin(content=nonetxt)
                                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                                    label="display the item list",
                                                                    custom_id="display"),
                                                      create_button(style=ButtonStyle.blue,
                                                                    label="not display the item list",
                                                                    custom_id="not_display")]
                                        button_raw = create_actionrow(*my_buttons)
                                        fait_choix = await ctx.send("`Push for the item list : `", components=[button_raw])
                                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                        if button_ctx.custom_id == "display":
                                                await button_ctx.edit_origin(content=nonetxt)
                                                item_list = list((st.loadDict(r"database\ItemsDatabase.obj")).keys())
                                                item_embed_list = tf.getListItemEmbedImageList(ctx,item_list)
                                                for item_embed in item_embed_list:
                                                        await ctx.send(embed=item_embed)
                                                await ctx.send("`item01`|`item02`|.....|`itemN`")
                                                try:
                                                        item_name_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                                        item_names = str(item_name_input.content)
                                                except:
                                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                        item_names = "none"
                                        elif button_ctx.custom_id == "not_display":
                                                await button_ctx.edit_origin(content=nonetxt)
                                                await ctx.send("`item01`|`item02`|.....|`itemN`")
                                                try:
                                                        item_name_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                                        item_names = str(item_name_input.content)
                                                except:
                                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                        item_names = "none"
                                        if item_names != "none":
                                                knoledge_list = item_names.split("|")
                                                display_character.craft_knowledge = knoledge_list
                                                st.saveCharacter(display_character,user_name,display_name)    
                                if button_ctx.custom_id == "ad":
                                        await button_ctx.edit_origin(content=nonetxt)
                                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                                    label="display the item list",
                                                                    custom_id="display"),
                                                      create_button(style=ButtonStyle.blue,
                                                                    label="not display the item list",
                                                                    custom_id="not_display")]
                                        button_raw = create_actionrow(*my_buttons)
                                        fait_choix = await ctx.send("`Push for the item list : `", components=[button_raw])
                                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                        if button_ctx.custom_id == "display":
                                                await button_ctx.edit_origin(content=nonetxt)
                                                item_list = list((st.loadDict(r"database\ItemsDatabase.obj")).keys())
                                                item_embed_list = tf.getListItemEmbedImageList(ctx,item_list)
                                                for item_embed in item_embed_list:
                                                        await ctx.send(embed=item_embed)
                                                await ctx.send("`enter the item name :`")
                                                try:
                                                        item_name_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                                        item_name = str(item_name_input.content)
                                                        await ctx.send("__name : __ `" + item_name + "`")
                                                except:
                                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        elif button_ctx.custom_id == "not_display":
                                                await button_ctx.edit_origin(content=nonetxt)
                                                await ctx.send("`enter the item name :`")
                                                try:
                                                        item_name_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                                        item_name = str(item_name_input.content)
                                                        await ctx.send("__name : __ `" + item_name + "`")
                                                except:
                                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        if item_name != "none":
                                                display_character.craft_knowledge.append(item_name)
                                                st.saveCharacter(display_character,user_name,display_name)   
                                if button_ctx.custom_id == "delete":
                                        await button_ctx.edit_origin(content=nonetxt)
                                        await ctx.send("`enter the item name :`")
                                        try:
                                                item_name_input = await notlolabot.bot.wait_for("message", timeout = 180, check=checkMessage)
                                                item_name = str(item_name_input.content)
                                                await ctx.send("__name : __ `" + item_name + "`")
                                        except:
                                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                        if item_name != "none":
                                                display_character.craft_knowledge.pop(st.getIndice(display_character.craft_knowledge,item_name))
                                                st.saveCharacter(display_character,user_name,display_name)
                if button_ctx.custom_id == "refresh":
                        await button_ctx.edit_origin(content=nonetxt)
                        char_name = display_character.name
                        char_description = display_character.presentation
                        char_history = display_character.lore_history
                        char_nickname = display_character.nickname
                        char_titles = display_character.title_list
                        char_background = display_character.background
                        char_allignement = display_character.alignement
                        char_max_hp = display_character.life[1]
                        char_level = display_character.level
                        if display_character.race.name != "":
                                char_race = st.loadRace(display_character.race.name)
                        else:
                                char_race = display_character.race
                        if display_character.classe.name != "":
                                char_classe = st.loadClasse(display_character.classe.name)
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
                                pass
                        fresh_character = rp.CharacterClass(char_name,char_description,char_history,char_nickname,char_titles,char_background,char_allignement,char_max_hp,char_level,char_race,char_classe,char_basic_stats,char_constructor_weapon01,char_constructor_weapon02,char_constructor_weapon03,char_constructor_acces01,char_constructor_acces02, char_constructor_armor,char_other_stats,char_image_path,char_inventory,char_capital,char_languages,char_autority,char_organisation,char_knowledge)
                        st.saveCharacter(fresh_character,user_name,display_name)
                        await ctx.send("`refresh`")
                if button_ctx.custom_id == "display inventory":
                        await button_ctx.edit_origin(content=nonetxt)
                        selection = ["inventory","first weapon","second weapon","third weapon","first accessory","second accessory","armor"]
                        inventory_type_select = tf.getListSelection(ctx,"chose the inventory to see",selection,selection) 
                        fait_choix = await ctx.send("`chose the inventory to see : `", components=[create_actionrow(inventory_type_select)])
                        inventory_type = await wait_for_component(notlolabot.bot, components=inventory_type_select, check=check)
                        if inventory_type.values[0] == "inventory":
                                await inventory_type.send(nonetxt)
                                embed_list = tf.getListInventoryCharacterEmbedImage(ctx,display_character)
                                for embed in embed_list:
                                        await ctx.send(embed=embed)
                                my_buttons = [create_button(style=ButtonStyle.blue,
                                                            label="use a item",
                                                            custom_id="use a item"),
                                              create_button(style=ButtonStyle.blue,
                                                            label="left the display",
                                                            custom_id="left the display")]
                                button_raw = create_actionrow(*my_buttons)
                                fait_choix = await ctx.send("`Push the button for display or change a option : `", components=[button_raw])
                                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                if button_ctx.custom_id == "use a item":
                                        await button_ctx.edit_origin(content=nonetxt)
                                        await ctx.send("`__enter the name of the consummable to use__`")
                                        try:
                                                item_name_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                                item_name = str(item_name_input.content)
                                        except:
                                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                item_name = "none"
                                        if item_name != "none":
                                                if item_name in display_character.inventory.keys():
                                                        if isinstance(display_character.inventory[item_name],rp.ConsumableClass):
                                                                if display_character.inventory[item_name].quantity > 0:
                                                                        display_character.inventory[item_name].quantity = display_character.inventory[item_name].quantity - 1
                                                                        if display_character.life[0] + display_character.inventory[item_name].life > display_character.life[1]:
                                                                                display_character.life = (display_character.life[1],display_character.life[1])
                                                                        else:
                                                                                display_character.life = (display_character.life[0] + display_character.inventory[item_name].life,display_character.life[1])
                                                                        st.saveCharacter(display_character,user_name,display_name)
                                                                        st.tickUpdate()
                                                                        await ctx.send("`" + item_name + "` : **used**.")
                                                                if display_character.inventory[item_name].quantity == 1:
                                                                        del display_character.inventory[item_name]
                                                                        if display_character.life[0] + display_character.inventory[item_name].life > display_character.life[1]:
                                                                                display_character.life = (display_character.life[1],display_character.life[1])
                                                                        else:
                                                                                display_character.life = (display_character.life[0] + display_character.inventory[item_name].life,display_character.life[1])
                                                                        st.saveCharacter(display_character,user_name,display_name)
                                                                        st.tickUpdate()
                                                                        await ctx.send("`" + item_name + "` : **used**.")
                                                                else:
                                                                        await ctx.send("`" + item_name + "` : **can't be used**.")
                                                        elif isinstance(display_character.inventory[item_name],rp.MagicalConsumableClass) or isinstance(display_character.inventory[item_name],rp.MagicalItemClass):
                                                                if True:
                                                                        if display_character.inventory[item_name].competence.type[0] in ["transversal_attack"]:
                                                                                my_buttons = [create_button(style=ButtonStyle.blue,
                                                                                                            label="use as a attack",
                                                                                                            custom_id="attack"),
                                                                                              create_button(style=ButtonStyle.blue,
                                                                                                            label="use as a competence",
                                                                                                            custom_id="competence")]
                                                                                button_raw = create_actionrow(*my_buttons)
                                                                                fait_choix = await ctx.send("`Push for chose the mode of utilisation : `", components=[button_raw])
                                                                                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                                                                if button_ctx.custom_id == "attack":
                                                                                        await button_ctx.edit_origin(content="`||use as a Attack||`")
                                                                                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                                                                                    label="display the character list",
                                                                                                                    custom_id="display"),
                                                                                                      create_button(style=ButtonStyle.blue,
                                                                                                                    label="dont display the character list",
                                                                                                                    custom_id="not display")]
                                                                                        button_raw = create_actionrow(*my_buttons)
                                                                                        fait_choix = await ctx.send("`Push for display the character list : `", components=[button_raw])
                                                                                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                                                                        if button_ctx.custom_id == "display":
                                                                                                await button_ctx.edit_origin(content=nonetxt)
                                                                                                character_dict = st.getCharactersDict()
                                                                                                txt = tf.getPlayerArchitectureChar(character_dict)
                                                                                                my_embed_list = tf.getEmbedCharacterDict(ctx ,character_dict)
                                                                                                for my_embed in my_embed_list:
                                                                                                        await ctx.send(embed=my_embed)
                                                                                                await ctx.send("`__enter the name of your target : __`")
                                                                                                try:
                                                                                                        target_name_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                                                                                        target_name = str(target_name_input.content)
                                                                                                except:
                                                                                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                                                                        target_name = "none"
                                                                                                if target_name != "none":
                                                                                                        target_path_list = st.getCharactersPaths(target_name)
                                                                                                        selection = []
                                                                                                        for target_path in target_path_list:
                                                                                                                selection_aux = target_path.split("|")
                                                                                                                selection.append(selection_aux[1] + "(" + target_name + ")")
                                                                                                        target_type_select = tf.getListSelection(ctx,"chose your target",selection,target_path_list) 
                                                                                                        fait_choix = await ctx.send("`Chose your target : `", components=[create_actionrow(target_type_select)])
                                                                                                        target_type = await wait_for_component(notlolabot.bot, components=target_type_select, check=check)
                                                                                                        await target_type.send(nonetxt)
                                                                                                        my_target_path = target_type.values[0].split("|")
                                                                                                        target = st.loadCharacter(my_target_path[0],my_target_path[1],my_target_path[2])


                                                                                                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                                                                                                    label="roll the attack dice",
                                                                                                                                    custom_id="dice")]
                                                                                                        button_raw = create_actionrow(*my_buttons)
                                                                                                        fait_choix = await ctx.send("`Push the result : `", components=[button_raw])
                                                                                                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)


                                                                                                        state_of_caster = sktr.getUpdateStateOfCharacter(display_character)
                                                                                                        display_character.state = (state_of_caster,display_character.state[1],display_character.state[2])
                                                                                                        state_of_target = sktr.getUpdateStateOfCharacter(target)
                                                                                                        target.state = (state_of_target,target.state[1],target.state[2])

                                                                                                                                   
                                                                                                        my_embed = tf.getEmbedStateCharacter(ctx,state_of_caster,state_of_target,char_name,target_name)
                                                                                                        await ctx.send(embed=my_embed)
                                                                                                        if button_ctx.custom_id == "dice":
                                                                                                                await button_ctx.edit_origin(content=nonetxt)  
                                                                                                                display_character.buffs = sktr.updateBuffList(display_character.buffs)
                                                                                                                target.buffs = sktr.updateBuffList(target.buffs)
                                                                                                                if isinstance(display_character.inventory[item_name],rp.MagicalItemClass):
                                                                                                                        display_character.inventory[item_name].competence.last_utilisation = st.getTick()
                                                                                                                results = sktr.getAttackResult(display_character.inventory[item_name].competence,display_character,target,50)
                                                                                                                last_life = copy.copy(target.life)
                                                                                                                if results[0] == True:
                                                                                                                        target.life = (sktr.getTheAbsoluteZero(target.life[0] - results[1]),target.life[1])
                                                                                                                        if display_character.competences[competence_name].type[1] == "buff":
                                                                                                                                target.buffs.append(rp.BuffClass(display_character.inventory[item_name].competence.state[1],display_character.inventory[item_name].competence.buff))
                                                                                                                        if display_character.competences[competence_name].type[1] == "self_buff":
                                                                                                                                display_character.buffs.append(rp.BuffClass(display_character.inventory[item_name].competence.state[1],display_character.inventory[item_name].competence.self_buff))
                                                                                                                if state_of_caster != "iframe" or display_character.inventory[item_name].competence.state[0] == "iframe":
                                                                                                                        display_character.state = (display_character.inventory[item_name].competence.state[0],display_character.inventory[item_name].competence.state[1],st.getTick())
                                                                                                                if display_character.inventory[item_name].competence.state[0] == "block":
                                                                                                                        new_template = {"strength" : (0,0),"dexterity" : (0,0),"bleeding" : (0,0) ,"posture" : display_character.inventory[item_name].competence.posture ,"constitution" : (0,0),"evasion" : (0,0),"intellect" : (0,0),"charisma" : (0,0) ,"wisdom" : (0,0)}
                                                                                                                        display_character.buffs.append(rp.BuffClass(display_character.inventory[item_name].competence.state[1],rp.StatisticsClass("",new_template)))
                                                                                                                st.saveCharacter(display_character,user_name,display_name)
                                                                                                                await ctx.send("`moddifications register`")
                                                                                                                st.saveCharacter(target,my_target_path[0],my_target_path[1])
                                                                                                                await ctx.send("`moddifications register`")
                                                                                                                st.tickUpdate()
                                                                                                                attack_embed = tf.getEmbedAttackRole(ctx ,results,char_name,target_name,display_character,target,last_life)
                                                                                                                await ctx.send(embed=attack_embed)
                                                                                                                if results[0] == True:
                                                                                                                        my_buttons = [create_button(style=ButtonStyle.green,
                                                                                                                                                    label="description of the skill",
                                                                                                                                                    custom_id="description"),
                                                                                                                                      create_button(style=ButtonStyle.green,
                                                                                                                                                    label="show buff",
                                                                                                                                                    custom_id="show buff"),
                                                                                                                                      create_button(style=ButtonStyle.blue,
                                                                                                                                                    label="cancel the attack",
                                                                                                                                                    custom_id="undo")]
                                                                                                                        button_raw = create_actionrow(*my_buttons)
                                                                                                                        fait_choix = await ctx.send("`Push for show : `", components=[button_raw])
                                                                                                                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                                                                                                        if button_ctx.custom_id == "description":
                                                                                                                                await button_ctx.edit_origin(content=nonetxt)
                                                                                                                                descr_embed = tf.getEmbedAttacDescription(ctx,display_character.inventory[item_name].competence)
                                                                                                                                await ctx.send(embed=descr_embed)
                                                                                                                        if button_ctx.custom_id == "show buff":
                                                                                                                                await button_ctx.edit_origin(content=nonetxt)
                                                                                                                                buffs_embed = tf.getEmbedAttackBuff(ctx,display_character.inventory[item_name].competence,results)
                                                                                                                                await ctx.send(embed=buffs_embed)
                                                                                                                        if button_ctx.custom_id == "undo":
                                                                                                                                await button_ctx.edit_origin(content=nonetxt)
                                                                                                                                target.life = (sktr.getTheAbsoluteZero(target.life[0] + results[1]),target.life[1])
                                                                                                                                
                                                                                                                                st.saveCharacter(display_character,user_name,display_name)
                                                                                                                                await ctx.send("`moddifications register`")
                                                                                                                                st.saveCharacter(target,my_target_path[0],my_target_path[1])
                                                                                                                                await ctx.send("`moddifications register`")
                                                                                                                else:
                                                                                                                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                                                                                                                    label="description of the skill",
                                                                                                                                                    custom_id="description"),
                                                                                                                                      create_button(style=ButtonStyle.blue,
                                                                                                                                                    label="show buff",
                                                                                                                                                    custom_id="show buff")]
                                                                                                                        button_raw = create_actionrow(*my_buttons)
                                                                                                                        fait_choix = await ctx.send("`Push for show : `", components=[button_raw])
                                                                                                                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                                                                                                        if button_ctx.custom_id == "description":
                                                                                                                                await button_ctx.edit_origin(content=nonetxt)
                                                                                                                                descr_embed = tf.getEmbedAttacDescription(ctx,display_character.inventory[item_name].competence)
                                                                                                                                await ctx.send(embed=descr_embed)
                                                                                                                        if button_ctx.custom_id == "show buff":
                                                                                                                                await button_ctx.edit_origin(content=nonetxt)
                                                                                                                                buffs_embed = tf.getEmbedAttackBuff(ctx,display_character.inventory[item_name].competence,results)
                                                                                                                                await ctx.send(embed=buffs_embed)
                                                                                                                


                                                                                                        
                                                                                        if button_ctx.custom_id == "not display":
                                                                                                await button_ctx.edit_origin(content=nonetxt)
                                                                                                await ctx.send("`__enter the name of your target : __`")
                                                                                                try:
                                                                                                        target_name_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                                                                                        target_name = str(target_name_input.content)
                                                                                                except:
                                                                                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                                                                        target_name = "none"
                                                                                                if target_name != "none":
                                                                                                        target_path_list = st.getCharactersPaths(target_name)
                                                                                                        selection = []
                                                                                                        for target_path in target_path_list:
                                                                                                                selection_aux = target_path.split("|")
                                                                                                                selection.append(selection_aux[1] + "(" + target_name + ")")
                                                                                                        target_type_select = tf.getListSelection(ctx,"chose your target",selection,target_path_list) 
                                                                                                        fait_choix = await ctx.send("`Chose your target : `", components=[create_actionrow(target_type_select)])
                                                                                                        target_type = await wait_for_component(notlolabot.bot, components=target_type_select, check=check)
                                                                                                        await target_type.send(nonetxt)
                                                                                                        my_target_path = target_type.values[0].split("|")
                                                                                                        target = st.loadCharacter(my_target_path[0],my_target_path[1],my_target_path[2])


                                                                                                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                                                                                                    label="roll the attack dice",
                                                                                                                                    custom_id="dice")]
                                                                                                        button_raw = create_actionrow(*my_buttons)
                                                                                                        fait_choix = await ctx.send("`Push the result : `", components=[button_raw])
                                                                                                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)


                                                                                                        state_of_caster = sktr.getUpdateStateOfCharacter(display_character)
                                                                                                        display_character.state = (state_of_caster,display_character.state[1],display_character.state[2])
                                                                                                        state_of_target = sktr.getUpdateStateOfCharacter(target)
                                                                                                        target.state = (state_of_target,target.state[1],target.state[2])

                                                                                                                                   
                                                                                                        my_embed = tf.getEmbedStateCharacter(ctx,state_of_caster,state_of_target,char_name,target_name)
                                                                                                        await ctx.send(embed=my_embed)
                                                                                                        if button_ctx.custom_id == "dice":
                                                                                                                await button_ctx.edit_origin(content=nonetxt)  
                                                                                                                display_character.buffs = sktr.updateBuffList(display_character.buffs)
                                                                                                                target.buffs = sktr.updateBuffList(target.buffs)
                                                                                                                if isinstance(display_character.inventory[item_name],rp.MagicalItemClass):
                                                                                                                        display_character.inventory[item_name].competence.last_utilisation = st.getTick()
                                                                                                                results = sktr.getAttackResult(display_character.inventory[item_name].competence,display_character,target,50)
                                                                                                                last_life = copy.copy(target.life)
                                                                                                                if results[0] == True:
                                                                                                                        target.life = (sktr.getTheAbsoluteZero(target.life[0] - results[1]),target.life[1])
                                                                                                                        if display_character.competences[competence_name].type[1] == "buff":
                                                                                                                                target.buffs.append(rp.BuffClass(display_character.inventory[item_name].competence.state[1],display_character.inventory[item_name].competence.buff))
                                                                                                                        if display_character.competences[competence_name].type[1] == "self_buff":
                                                                                                                                display_character.buffs.append(rp.BuffClass(display_character.inventory[item_name].competence.state[1],display_character.inventory[item_name].competence.self_buff))
                                                                                                                if state_of_caster != "iframe" or display_character.inventory[item_name].competence.state[0] == "iframe":
                                                                                                                        display_character.state = (display_character.inventory[item_name].competence.state[0],display_character.inventory[item_name].competence.state[1],st.getTick())
                                                                                                                if display_character.inventory[item_name].competence.state[0] == "block":
                                                                                                                        new_template = {"strength" : (0,0),"dexterity" : (0,0),"bleeding" : (0,0) ,"posture" : display_character.inventory[item_name].competence.posture ,"constitution" : (0,0),"evasion" : (0,0),"intellect" : (0,0),"charisma" : (0,0) ,"wisdom" : (0,0)}
                                                                                                                        display_character.buffs.append(rp.BuffClass(display_character.inventory[item_name].competence.state[1],rp.StatisticsClass("",new_template)))
                                                                                                                st.saveCharacter(display_character,user_name,display_name)
                                                                                                                await ctx.send("`moddifications register`")
                                                                                                                st.saveCharacter(target,my_target_path[0],my_target_path[1])
                                                                                                                await ctx.send("`moddifications register`")
                                                                                                                st.tickUpdate()
                                                                                                                attack_embed = tf.getEmbedAttackRole(ctx ,results,char_name,target_name,display_character,target,last_life)
                                                                                                                await ctx.send(embed=attack_embed)
                                                                                                                if results[0] == True:
                                                                                                                        my_buttons = [create_button(style=ButtonStyle.green,
                                                                                                                                                    label="description of the skill",
                                                                                                                                                    custom_id="description"),
                                                                                                                                      create_button(style=ButtonStyle.green,
                                                                                                                                                    label="show buff",
                                                                                                                                                    custom_id="show buff"),
                                                                                                                                      create_button(style=ButtonStyle.blue,
                                                                                                                                                    label="cancel the attack",
                                                                                                                                                    custom_id="undo")]
                                                                                                                        button_raw = create_actionrow(*my_buttons)
                                                                                                                        fait_choix = await ctx.send("`Push for show : `", components=[button_raw])
                                                                                                                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                                                                                                        if button_ctx.custom_id == "description":
                                                                                                                                await button_ctx.edit_origin(content=nonetxt)
                                                                                                                                descr_embed = tf.getEmbedAttacDescription(ctx,display_character.inventory[item_name].competence)
                                                                                                                                await ctx.send(embed=descr_embed)
                                                                                                                        if button_ctx.custom_id == "show buff":
                                                                                                                                await button_ctx.edit_origin(content=nonetxt)
                                                                                                                                buffs_embed = tf.getEmbedAttackBuff(ctx,display_character.inventory[item_name].competence,results)
                                                                                                                                await ctx.send(embed=buffs_embed)
                                                                                                                        if button_ctx.custom_id == "undo":
                                                                                                                                await button_ctx.edit_origin(content=nonetxt)
                                                                                                                                target.life = (sktr.getTheAbsoluteZero(target.life[0] + results[1]),target.life[1])
                                                                                                                                
                                                                                                                                st.saveCharacter(display_character,user_name,display_name)
                                                                                                                                await ctx.send("`moddifications register`")
                                                                                                                                st.saveCharacter(target,my_target_path[0],my_target_path[1])
                                                                                                                                await ctx.send("`moddifications register`")
                                                                                                                else:
                                                                                                                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                                                                                                                    label="description of the skill",
                                                                                                                                                    custom_id="description"),
                                                                                                                                      create_button(style=ButtonStyle.blue,
                                                                                                                                                    label="show buff",
                                                                                                                                                    custom_id="show buff")]
                                                                                                                        button_raw = create_actionrow(*my_buttons)
                                                                                                                        fait_choix = await ctx.send("`Push for show : `", components=[button_raw])
                                                                                                                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                                                                                                        if button_ctx.custom_id == "description":
                                                                                                                                await button_ctx.edit_origin(content=nonetxt)
                                                                                                                                descr_embed = tf.getEmbedAttacDescription(ctx,display_character.inventory[item_name].competence)
                                                                                                                                await ctx.send(embed=descr_embed)
                                                                                                                        if button_ctx.custom_id == "show buff":
                                                                                                                                await button_ctx.edit_origin(content=nonetxt)
                                                                                                                                buffs_embed = tf.getEmbedAttackBuff(ctx,display_character.inventory[item_name].competence,results)
                                                                                                                                await ctx.send(embed=buffs_embed)
                                                                                if button_ctx.custom_id == "competence":
                                                                                        await button_ctx.edit_origin(content="`||use as a Competence||`")
                                                                                        display_character.state = (display_character.inventory[item_name].competence.state[0],display_character.inventory[item_name].competence.state[1],st.getTick())
                                                                                        if isinstance(display_character.inventory[item_name],rp.MagicalItemClass):
                                                                                                display_character.inventory[item_name].competence.last_utilisation = st.getTick()
                                                                                        if display_character.inventory[item_name].competence.type[1] == "self_buff":
                                                                                                display_character.buffs.append(rp.BuffClass(display_character.inventory[item_name].competence.state[1],display_character.inventory[item_name].competence.self_buff))
                                                                                        st.saveCharacter(display_character,user_name,display_name)
                                                                                        st.tickUpdate()
                                                                                        await ctx.send("`competence utilisée`")

                                                                                        
                                                                                
                                                                                pass
                                                                        elif display_character.inventory[item_name].competence.type[0] in ["massiv_skill"]:
                                                                                await competence_aux.send(nonetxt)
                                                                                my_buttons = [create_button(style=ButtonStyle.blue,
                                                                                                            label="display the character list",
                                                                                                            custom_id="display"),
                                                                                              create_button(style=ButtonStyle.blue,
                                                                                                            label="dont display the character list",
                                                                                                            custom_id="not display")]
                                                                                button_raw = create_actionrow(*my_buttons)
                                                                                fait_choix = await ctx.send("`Push for display the character list : `", components=[button_raw])
                                                                                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                                                                if button_ctx.custom_id == "display":
                                                                                        await button_ctx.edit_origin(content=nonetxt)
                                                                                        character_dict = st.getCharactersDict()
                                                                                        txt = tf.getPlayerArchitectureChar(character_dict)
                                                                                        my_embed_list = tf.getEmbedCharacterDict(ctx ,character_dict)
                                                                                        for my_embed in my_embed_list:
                                                                                                await ctx.send(embed=my_embed)
                                                                                        await ctx.send("`__enter the names of your targets : __`")
                                                                                        await ctx.send("`target1|target2|target3|target4........`")
                                                                                        try:
                                                                                                target_names_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                                                                                target_names = str(target_names_input.content)
                                                                                        except:
                                                                                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                                                                target_names = "none"
                                                                                        if target_names != "none":
                                                                                                targets_list = target_names.split("|")
                                                                                                selection_target = []
                                                                                                new_target_path_list = []
                                                                                                for target_name in targets_list:
                                                                                                        target_path_list = st.getCharactersPaths(target_name)
                                                                                                        new_target_path_list = new_target_path_list + target_path_list
                                                                                                        selection = []
                                                                                                        for target_path in target_path_list:
                                                                                                                selection_aux = target_path.split("|")
                                                                                                                selection.append(selection_aux[1] + "(" + target_name + ")")
                                                                                                        selection_target = selection_target + selection
                                                                                                if (display_character.inventory[item_name].competence.level <= 14) and (display_character.level <= 14):
                                                                                                        if len(selection_target) < 3:
                                                                                                                targets_selection = tf.getListSelection(ctx,"chose the targets",selection_target,new_target_path_list,1,len(selection_target))
                                                                                                                fait_choix = await ctx.send("`Chose the targets : `", components=[create_actionrow(targets_selection)])
                                                                                                                targets_list_path = await wait_for_component(notlolabot.bot, components=targets_selection, check=check)
                                                                                                                await targets_list_path.send(nonetxt)
                                                                                                                pass
                                                                                                        else:
                                                                                                                targets_selection = tf.getListSelection(ctx,"chose the targets",selection_target,new_target_path_list,1,3)
                                                                                                                fait_choix = await ctx.send("`Chose the targets : `", components=[create_actionrow(targets_selection)])
                                                                                                                targets_list_path = await wait_for_component(notlolabot.bot, components=targets_selection, check=check)
                                                                                                                await targets_list_path.send(nonetxt)
                                                                                                else:
                                                                                                        if len(selection_target) < 8:
                                                                                                                targets_selection = tf.getListSelection(ctx,"chose the targets",selection_target,new_target_path_list,1,len(selection_target))
                                                                                                                fait_choix = await ctx.send("`Chose the targets : `", components=[create_actionrow(targets_selection)])
                                                                                                                targets_list_path = await wait_for_component(notlolabot.bot, components=targets_selection, check=check)
                                                                                                                await targets_list_path.send(nonetxt)
                                                                                                                pass
                                                                                                        else:
                                                                                                                targets_selection = tf.getListSelection(ctx,"chose the targets",selection_target,new_target_path_list,1,8)
                                                                                                                fait_choix = await ctx.send("`Chose the targets : `", components=[create_actionrow(targets_selection)])
                                                                                                                targets_list_path = await wait_for_component(notlolabot.bot, components=targets_selection, check=check)
                                                                                                                await targets_list_path.send(nonetxt)
                                                                                                        pass
                                                                                                if targets_list_path.values != []:
                                                                                                        if isinstance(display_character.inventory[item_name],rp.MagicalItemClass):
                                                                                                                display_character.inventory[item_name].competence.last_utilisation = st.getTick()
                                                                                                        st.saveCharacter(display_character,user_name,display_name)
                                                                                                        for k in range(len(targets_list_path.values)):
                                                                                                                my_target_path = targets_list_path.values[k].split("|")
                                                                                                                target = st.loadCharacter(my_target_path[0],my_target_path[1],my_target_path[2])
                                                                                                                target.buffs.append(rp.BuffClass(display_character.inventory[item_name].competence.state[1],display_character.inventory[item_name].competence.buff))
                                                                                                                st.saveCharacter(target,my_target_path[0],my_target_path[1])
                                                                                                                await ctx.send("buffs add")
                                                                                                        pass
                                                                                if button_ctx.custom_id == "not display":
                                                                                        await button_ctx.edit_origin(content=nonetxt)
                                                                                        await ctx.send("`__enter the names of your targets : __`")
                                                                                        await ctx.send("`target1|target2|target3|target4........`")
                                                                                        try:
                                                                                                target_names_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                                                                                target_names = str(target_names_input.content)
                                                                                        except:
                                                                                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                                                                target_names = "none"
                                                                                        if target_names != "none":
                                                                                                targets_list = target_names.split("|")
                                                                                                selection_target = []
                                                                                                new_target_path_list = []
                                                                                                for target_name in targets_list:
                                                                                                        target_path_list = st.getCharactersPaths(target_name)
                                                                                                        new_target_path_list = new_target_path_list + target_path_list
                                                                                                        selection = []
                                                                                                        for target_path in target_path_list:
                                                                                                                selection_aux = target_path.split("|")
                                                                                                                selection.append(selection_aux[1] + "(" + target_name + ")")
                                                                                                        selection_target = selection_target + selection
                                                                                                if (display_character.inventory[item_name].competence.level <= 14) and (display_character.level <= 14):
                                                                                                        if len(selection_target) < 3:
                                                                                                                targets_selection = tf.getListSelection(ctx,"chose the targets",selection_target,new_target_path_list,1,len(selection_target))
                                                                                                                fait_choix = await ctx.send("`Chose the targets : `", components=[create_actionrow(targets_selection)])
                                                                                                                targets_list_path = await wait_for_component(notlolabot.bot, components=targets_selection, check=check)
                                                                                                                await targets_list_path.send(nonetxt)
                                                                                                                pass
                                                                                                        else:
                                                                                                                targets_selection = tf.getListSelection(ctx,"chose the targets",selection_target,new_target_path_list,1,3)
                                                                                                                fait_choix = await ctx.send("`Chose the targets : `", components=[create_actionrow(targets_selection)])
                                                                                                                targets_list_path = await wait_for_component(notlolabot.bot, components=targets_selection, check=check)
                                                                                                                await targets_list_path.send(nonetxt)
                                                                                                else:
                                                                                                        if len(selection_target) < 8:
                                                                                                                targets_selection = tf.getListSelection(ctx,"chose the targets",selection_target,new_target_path_list,1,len(selection_target))
                                                                                                                fait_choix = await ctx.send("`Chose the targets : `", components=[create_actionrow(targets_selection)])
                                                                                                                targets_list_path = await wait_for_component(notlolabot.bot, components=targets_selection, check=check)
                                                                                                                await targets_list_path.send(nonetxt)
                                                                                                                pass
                                                                                                        else:
                                                                                                                targets_selection = tf.getListSelection(ctx,"chose the targets",selection_target,new_target_path_list,1,8)
                                                                                                                fait_choix = await ctx.send("`Chose the targets : `", components=[create_actionrow(targets_selection)])
                                                                                                                targets_list_path = await wait_for_component(notlolabot.bot, components=targets_selection, check=check)
                                                                                                                await targets_list_path.send(nonetxt)
                                                                                                        pass
                                                                                                if targets_list_path.values != []:
                                                                                                        if isinstance(display_character.inventory[item_name],rp.MagicalItemClass):
                                                                                                                display_character.inventory[item_name].competence.last_utilisation = st.getTick()
                                                                                                        st.saveCharacter(display_character,user_name,display_name)
                                                                                                        for k in range(len(targets_list_path.values)):
                                                                                                                my_target_path = targets_list_path.values[k].split("|")
                                                                                                                target = st.loadCharacter(my_target_path[0],my_target_path[1],my_target_path[2])
                                                                                                                target.buffs.append(rp.BuffClass(display_character.inventory[item_name].competence.state[1],display_character.inventory[item_name].competence.buff))
                                                                                                                st.saveCharacter(target,my_target_path[0],my_target_path[1])
                                                                                                                await ctx.send("buffs add")
                                                                                                        pass
                                                                        else:
                                                                                await competence_aux.send(nonetxt)
                                                                                display_character.state = (display_character.inventory[item_name].competence.state[0],display_character.inventory[item_name].competence.state[1],st.getTick())
                                                                                if isinstance(display_character.inventory[item_name],rp.MagicalItemClass):
                                                                                        display_character.inventory[item_name].competence.last_utilisation = st.getTick()
                                                                                if display_character.competences[competence_name].type[1] == "self_buff":
                                                                                        display_character.buffs.append(rp.BuffClass(display_character.inventory[item_name].competence.state[1],display_character.inventory[item_name].competence.self_buff))
                                                                                st.saveCharacter(display_character,user_name,display_name)
                                                                                st.tickUpdate()
                                                                                await ctx.send("`competence utilisée`")
                                                                if isinstance(display_character.inventory[item_name],rp.MagicalConsumableClass):
                                                                        if display_character.inventory[item_name].quantity > 0:
                                                                                display_character.inventory[item_name].quantity = display_character.inventory[item_name].quantity - 1
                                                                                if display_character.life[0] + display_character.inventory[item_name].life > display_character.life[1]:
                                                                                        display_character.life = (display_character.life[1],display_character.life[1])
                                                                                else:
                                                                                        display_character.life = (display_character.life[0] + display_character.inventory[item_name].life,display_character.life[1])
                                                                                st.saveCharacter(display_character,user_name,display_name)
                                                                                await ctx.send("`" + item_name + "` : **used**.")
                                                                        if display_character.inventory[item_name].quantity == 1:
                                                                                del display_character.inventory[item_name]
                                                                                if display_character.life[0] + display_character.inventory[item_name].life > display_character.life[1]:
                                                                                        display_character.life = (display_character.life[1],display_character.life[1])
                                                                                else:
                                                                                        display_character.life = (display_character.life[0] + display_character.inventory[item_name].life,display_character.life[1])
                                                                                st.saveCharacter(display_character,user_name,display_name)
                                                                                await ctx.send("`" + item_name + "` : **used**.")
                                                                        else:
                                                                                await ctx.send("`" + item_name + "` : **can't be used**.")
                                                        else:
                                                                await ctx.send("`item sans effets`")



                                                else:
                                                        await ctx.send("`item introuvable!`")
                                if button_ctx.custom_id == "left the display":
                                        await button_ctx.edit_origin(content=nonetxt)
                        if inventory_type.values[0] == "first weapon":
                                await inventory_type.send(nonetxt)
                                embed = tf.getEmbedImageCharacterEquipement(ctx,display_character.weapon01)
                                await ctx.send(embed=embed)
                        if inventory_type.values[0] == "second weapon":
                                await inventory_type.send(nonetxt)
                                embed = tf.getEmbedImageCharacterEquipement(ctx,display_character.weapon02)
                                await ctx.send(embed=embed)
                        if inventory_type.values[0] == "third weapon":
                                await inventory_type.send(nonetxt)
                                embed = tf.getEmbedImageCharacterEquipement(ctx,display_character.weapon02)
                                await ctx.send(embed=embed)
                        if inventory_type.values[0] == "first accessory":
                                await inventory_type.send(nonetxt)
                                embed = tf.getEmbedImageCharacterEquipement(ctx,display_character.accessorry01)
                                await ctx.send(embed=embed)
                        if inventory_type.values[0] == "second accessory":
                                await inventory_type.send(nonetxt)
                                embed = tf.getEmbedImageCharacterEquipement(ctx,display_character.accessorry02)
                                await ctx.send(embed=embed)
                        if inventory_type.values[0] == "armor":
                                await inventory_type.send(nonetxt)
                                embed = tf.getEmbedImageCharacterEquipement(ctx,display_character.armor)
                                await ctx.send(embed=embed)
                if button_ctx.custom_id == "switch weapon":
                        await button_ctx.edit_origin(content=nonetxt)
                        selection = ["rotation",
                                     "weapon01 " + display_character.weapon01.name,
                                     "weapon02 " + display_character.weapon02.name,
                                     "weapon03 " + display_character.weapon03.name]
                        switch_type_select = tf.getListSelection(ctx,"chose the main weapon",selection,["rotation","weapon1","weapon2","weapon3"]) 
                        fait_choix = await ctx.send("`chose the main weapon : `", components=[create_actionrow(switch_type_select)])
                        switch_type = await wait_for_component(notlolabot.bot, components=switch_type_select, check=check)
                        if switch_type.values[0] == "weapon1":
                                 await switch_type.send(nonetxt)
                                 display_character.main_weapon = display_character.weapon01
                                 st.saveCharacter(display_character,user_name,display_name)
                                 await ctx.send("`moddifications register`")
                        if switch_type.values[0] == "weapon2":
                                 await switch_type.send(nonetxt)
                                 display_character.main_weapon = display_character.weapon02
                                 st.saveCharacter(display_character,user_name,display_name)
                                 await ctx.send("`moddifications register`")
                        if switch_type.values[0] == "weapon3":
                                 await switch_type.send(nonetxt)
                                 display_character.main_weapon = display_character.weapon03
                                 st.saveCharacter(display_character,user_name,display_name)
                                 await ctx.send("`moddifications register`")
                        if switch_type.values[0] == "rotation":
                                 await switch_type.send(nonetxt)
                                 display_character.switchWeapon()
                                 st.saveCharacter(display_character,user_name,display_name)
                                 await ctx.send("`moddifications register`")
                        pass
                pass
        else:
                await ctx.send("`Personnage non enregistrer!`")
@notlolabot.bot.command()
async def competences(ctx):
        """competences command for display the competences board"""
        def check(m):
                return m.author_id == ctx.author.id and m.origin_message.id == fait_choix.id
        def checkMessage(message):
                return message.author == ctx.message.author and ctx.message.channel == message.channel
        display_name = ctx.author.display_name
        user_name = ctx.author.name
        if user_name in st.loadDict(r"database\users_database.obj").keys():
                char_name = st.loadUser(user_name).sub_pointage
                
                display_character = st.loadCharacter(user_name,display_name,char_name)
                my_embed_list = tf.getFirstEmbedImageCharacterCompetencesList(ctx,display_character)
                for my_embed in my_embed_list:
                        await ctx.send(embed=my_embed)
                my_buttons = [create_button(style=ButtonStyle.green,
                                            label="display the others weapon skills",
                                            custom_id="others weapon"),
                              create_button(style=ButtonStyle.green,
                                            label="display the class and race skills",
                                            custom_id="class race skills")]
                button_raw = create_actionrow(*my_buttons)
                fait_choix = await ctx.send("`Push for display the competences list : `", components=[button_raw])
                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                if button_ctx.custom_id == "others weapon":
                        await button_ctx.edit_origin(content="`|Weapons Skills|`")
                        my_embed = tf.getFirstEmbedImageCharacterCompetencesListWeapons(ctx,display_character)
                        await ctx.send(embed=my_embed)
                        pass
                if button_ctx.custom_id == "class race skills":
                        await button_ctx.edit_origin(content="`|Races And Class Skills|`")
                        my_embed = tf.getFirstEmbedImageCharacterCompetencesListRacesClasses(ctx,display_character)
                        await ctx.send(embed=my_embed)
        else:
                await ctx.send("`Personnage non enregistrer!`")
@notlolabot.bot.command()
async def action(ctx):
        """action command for use a competence/skill or roll a characteristic dice"""
        def check(m):
                return m.author_id == ctx.author.id and m.origin_message.id == fait_choix.id
        def checkMessage(message):
                return message.author == ctx.message.author and ctx.message.channel == message.channel
        display_name = ctx.author.display_name
        user_name = ctx.author.name
        
        if user_name in st.loadDict(r"database\users_database.obj").keys():
                char_name = st.loadUser(user_name).sub_pointage
                display_character = st.loadCharacter(user_name,display_name,char_name)
                



                
                action_type_select = tf.getListSelection(ctx,"chose the action",["use a skill | competence","characteristic dice","use a mass entity skill","use a item | consumable","use a ritual | competence"],["use a skill","characteristic dice","mass entity","use a item","use a ritual"]) 
                fait_choix = await ctx.send("`Chose the action : `", components=[create_actionrow(action_type_select)])
                action_type = await wait_for_component(notlolabot.bot, components=action_type_select, check=check)
                if action_type.values[0] == "use a skill":
                        await action_type.send("`||use a skill | competence||`")
                        usable_skill_list = sktr.getUsableSkillList(display_character)
                        competence_select = tf.getListSelection(ctx,"chose the skill to use",usable_skill_list,usable_skill_list) 
                        fait_choix = await ctx.send("`chose the skill to use : `", components=[create_actionrow(competence_select)])
                        competence_aux = await wait_for_component(notlolabot.bot, components=competence_select, check=check)
                        competence_name = competence_aux.values[0]
                        if display_character.competences[competence_name].type[0] in ["weapon_attack","normal_attack","one hand weapon_attack"]:
                                await competence_aux.send(nonetxt)

                                
                                my_buttons = [create_button(style=ButtonStyle.blue,
                                                            label="display the character list",
                                                            custom_id="display"),
                                              create_button(style=ButtonStyle.blue,
                                                            label="dont display the character list",
                                                            custom_id="not display")]
                                button_raw = create_actionrow(*my_buttons)
                                fait_choix = await ctx.send("`Push for display the character list : `", components=[button_raw])
                                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                if button_ctx.custom_id == "display":
                                        await button_ctx.edit_origin(content=nonetxt)
                                        character_dict = st.getCharactersDict()
                                        txt = tf.getPlayerArchitectureChar(character_dict)
                                        my_embed_list = tf.getEmbedCharacterDict(ctx ,character_dict)
                                        for my_embed in my_embed_list:
                                                await ctx.send(embed=my_embed)
                                        await ctx.send("`__enter the name of your target : __`")
                                        try:
                                                target_name_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                                target_name = str(target_name_input.content)
                                        except:
                                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                target_name = "none"
                                        if target_name != "none":
                                                target_path_list = st.getCharactersPaths(target_name)
                                                selection = []
                                                for target_path in target_path_list:
                                                        selection_aux = target_path.split("|")
                                                        selection.append(selection_aux[1] + "(" + target_name + ")")
                                                target_type_select = tf.getListSelection(ctx,"chose your target",selection,target_path_list) 
                                                fait_choix = await ctx.send("`Chose your target : `", components=[create_actionrow(target_type_select)])
                                                target_type = await wait_for_component(notlolabot.bot, components=target_type_select, check=check)
                                                await target_type.send(nonetxt)
                                                my_target_path = target_type.values[0].split("|")
                                                target = st.loadCharacter(my_target_path[0],my_target_path[1],my_target_path[2])


                                                my_buttons = [create_button(style=ButtonStyle.blue,
                                                                            label="roll the attack dice",
                                                                            custom_id="dice")]
                                                button_raw = create_actionrow(*my_buttons)
                                                fait_choix = await ctx.send("`Push the result : `", components=[button_raw])
                                                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)


                                                state_of_caster = sktr.getUpdateStateOfCharacter(display_character)
                                                display_character.state = (state_of_caster,display_character.state[1],display_character.state[2])
                                                state_of_target = sktr.getUpdateStateOfCharacter(target)
                                                target.state = (state_of_target,target.state[1],target.state[2])

                                                                           
                                                my_embed = tf.getEmbedStateCharacter(ctx,state_of_caster,state_of_target,char_name,target_name)
                                                await ctx.send(embed=my_embed)
                                                if button_ctx.custom_id == "dice":
                                                        await button_ctx.edit_origin(content=nonetxt)  
                                                        display_character.buffs = sktr.updateBuffList(display_character.buffs)
                                                        target.buffs = sktr.updateBuffList(target.buffs)
                                                        display_character.competences[competence_name].last_utilisation = st.getTick()
                                                        results = sktr.getAttackResult(display_character.competences[competence_name],display_character,target,50)
                                                        last_life = copy.copy(target.life)
                                                        if results[0] == True:
                                                                target.life = (sktr.getTheAbsoluteZero(target.life[0] - results[1]),target.life[1])
                                                                if display_character.competences[competence_name].type[1] == "buff":
                                                                        target.buffs.append(rp.BuffClass(display_character.competences[competence_name].state[1],display_character.competences[competence_name].buff))
                                                                if display_character.competences[competence_name].type[1] == "self_buff":
                                                                        display_character.buffs.append(rp.BuffClass(display_character.competences[competence_name].state[1],display_character.competences[competence_name].self_buff))
                                                        if state_of_caster != "iframe" or display_character.competences[competence_name].state[0] == "iframe":
                                                                display_character.state = (display_character.competences[competence_name].state[0],display_character.competences[competence_name].state[1],st.getTick())
                                                        if display_character.competences[competence_name].state[0] == "block":
                                                                new_template = {"strength" : (0,0),"dexterity" : (0,0),"bleeding" : (0,0) ,"posture" : display_character.competences[competence_name].posture ,"constitution" : (0,0),"evasion" : (0,0),"intellect" : (0,0),"charisma" : (0,0) ,"wisdom" : (0,0)}
                                                                display_character.buffs.append(rp.BuffClass(display_character.competences[competence_name].state[1],rp.StatisticsClass("",new_template)))
                                                        st.saveCharacter(display_character,user_name,display_name)
                                                        await ctx.send("`moddifications register`")
                                                        st.saveCharacter(target,my_target_path[0],my_target_path[1])
                                                        await ctx.send("`moddifications register`")
                                                        st.tickUpdate()
                                                        attack_embed = tf.getEmbedAttackRole(ctx ,results,char_name,target_name,display_character,target,last_life)
                                                        await ctx.send(embed=attack_embed)
                                                        if results[0] == True:
                                                                my_buttons = [create_button(style=ButtonStyle.green,
                                                                                            label="description of the skill",
                                                                                            custom_id="description"),
                                                                              create_button(style=ButtonStyle.green,
                                                                                            label="show buff",
                                                                                            custom_id="show buff"),
                                                                              create_button(style=ButtonStyle.blue,
                                                                                            label="cancel the attack",
                                                                                            custom_id="undo")]
                                                                button_raw = create_actionrow(*my_buttons)
                                                                fait_choix = await ctx.send("`Push for show : `", components=[button_raw])
                                                                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                                                if button_ctx.custom_id == "description":
                                                                        await button_ctx.edit_origin(content=nonetxt)
                                                                        descr_embed = tf.getEmbedAttacDescription(ctx,display_character.competences[competence_name])
                                                                        await ctx.send(embed=descr_embed)
                                                                if button_ctx.custom_id == "show buff":
                                                                        await button_ctx.edit_origin(content=nonetxt)
                                                                        buffs_embed = tf.getEmbedAttackBuff(ctx,display_character.competences[competence_name],results)
                                                                        await ctx.send(embed=buffs_embed)
                                                                if button_ctx.custom_id == "undo":
                                                                        await button_ctx.edit_origin(content=nonetxt)
                                                                        target.life = (sktr.getTheAbsoluteZero(target.life[0] + results[1]),target.life[1])
                                                                        display_character.competences[competence_name].last_utilisation = - display_character.competences[competence_name].competence_cooldown
                                                                        st.saveCharacter(display_character,user_name,display_name)
                                                                        await ctx.send("`moddifications register`")
                                                                        st.saveCharacter(target,my_target_path[0],my_target_path[1])
                                                                        await ctx.send("`moddifications register`")
                                                        else:
                                                                my_buttons = [create_button(style=ButtonStyle.blue,
                                                                                            label="description of the skill",
                                                                                            custom_id="description"),
                                                                              create_button(style=ButtonStyle.blue,
                                                                                            label="show buff",
                                                                                            custom_id="show buff")]
                                                                button_raw = create_actionrow(*my_buttons)
                                                                fait_choix = await ctx.send("`Push for show : `", components=[button_raw])
                                                                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                                                if button_ctx.custom_id == "description":
                                                                        await button_ctx.edit_origin(content=nonetxt)
                                                                        descr_embed = tf.getEmbedAttacDescription(ctx,display_character.competences[competence_name])
                                                                        await ctx.send(embed=descr_embed)
                                                                if button_ctx.custom_id == "show buff":
                                                                        await button_ctx.edit_origin(content=nonetxt)
                                                                        buffs_embed = tf.getEmbedAttackBuff(ctx,display_character.competences[competence_name],results)
                                                                        await ctx.send(embed=buffs_embed)
                                                        


                                                
                                if button_ctx.custom_id == "not display":
                                        await button_ctx.edit_origin(content=nonetxt)
                                        await ctx.send("`__enter the name of your target : __`")
                                        try:
                                                target_name_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                                target_name = str(target_name_input.content)
                                        except:
                                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                target_name = "none"
                                        if target_name != "none":
                                                target_path_list = st.getCharactersPaths(target_name)
                                                selection = []
                                                for target_path in target_path_list:
                                                        selection_aux = target_path.split("|")
                                                        selection.append(selection_aux[1] + "(" + target_name + ")")
                                                target_type_select = tf.getListSelection(ctx,"chose your target",selection,target_path_list) 
                                                fait_choix = await ctx.send("`Chose your target : `", components=[create_actionrow(target_type_select)])
                                                target_type = await wait_for_component(notlolabot.bot, components=target_type_select, check=check)
                                                await target_type.send(nonetxt)
                                                my_target_path = target_type.values[0].split("|")
                                                target = st.loadCharacter(my_target_path[0],my_target_path[1],my_target_path[2])


                                                my_buttons = [create_button(style=ButtonStyle.blue,
                                                                            label="roll the attack dice",
                                                                            custom_id="dice")]
                                                button_raw = create_actionrow(*my_buttons)
                                                fait_choix = await ctx.send("`Push the result : `", components=[button_raw])
                                                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)


                                                state_of_caster = sktr.getUpdateStateOfCharacter(display_character)
                                                display_character.state = (state_of_caster,display_character.state[1],display_character.state[2])
                                                state_of_target = sktr.getUpdateStateOfCharacter(target)
                                                target.state = (state_of_target,target.state[1],target.state[2])

                                                                           
                                                my_embed = tf.getEmbedStateCharacter(ctx,state_of_caster,state_of_target,char_name,target_name)
                                                await ctx.send(embed=my_embed)
                                                if button_ctx.custom_id == "dice":
                                                        await button_ctx.edit_origin(content=nonetxt)  
                                                        display_character.buffs = sktr.updateBuffList(display_character.buffs)
                                                        target.buffs = sktr.updateBuffList(target.buffs)
                                                        display_character.competences[competence_name].last_utilisation = st.getTick()
                                                        results = sktr.getAttackResult(display_character.competences[competence_name],display_character,target,50)
                                                        last_life = copy.copy(target.life)
                                                        if results[0] == True:
                                                                target.life = (sktr.getTheAbsoluteZero(target.life[0] - results[1]),target.life[1])
                                                                if display_character.competences[competence_name].type[1] == "buff":
                                                                        target.buffs.append(rp.BuffClass(display_character.competences[competence_name].state[1],display_character.competences[competence_name].buff))
                                                                if display_character.competences[competence_name].type[1] == "self_buff":
                                                                        display_character.buffs.append(rp.BuffClass(display_character.competences[competence_name].state[1],display_character.competences[competence_name].self_buff))
                                                        if state_of_caster != "iframe" or display_character.competences[competence_name].state[0] == "iframe":
                                                                display_character.state = (display_character.competences[competence_name].state[0],display_character.competences[competence_name].state[1],st.getTick())
                                                        if display_character.competences[competence_name].state[0] == "block":
                                                                new_template = {"strength" : (0,0),"dexterity" : (0,0),"bleeding" : (0,0) ,"posture" : display_character.competences[competence_name].posture ,"constitution" : (0,0),"evasion" : (0,0),"intellect" : (0,0),"charisma" : (0,0) ,"wisdom" : (0,0)}
                                                                display_character.buffs.append(rp.BuffClass(display_character.competences[competence_name].state[1],rp.StatisticsClass("",new_template)))
                                                        st.saveCharacter(display_character,user_name,display_name)
                                                        await ctx.send("`moddifications register`")
                                                        st.saveCharacter(target,my_target_path[0],my_target_path[1])
                                                        await ctx.send("`moddifications register`")
                                                        st.tickUpdate()
                                                        attack_embed = tf.getEmbedAttackRole(ctx ,results,char_name,target_name,display_character,target,last_life)
                                                        await ctx.send(embed=attack_embed)
                                                        if results[0] == True:
                                                                my_buttons = [create_button(style=ButtonStyle.green,
                                                                                            label="description of the skill",
                                                                                            custom_id="description"),
                                                                              create_button(style=ButtonStyle.green,
                                                                                            label="show buff",
                                                                                            custom_id="show buff"),
                                                                              create_button(style=ButtonStyle.blue,
                                                                                            label="cancel the attack",
                                                                                            custom_id="undo")]
                                                                button_raw = create_actionrow(*my_buttons)
                                                                fait_choix = await ctx.send("`Push for show : `", components=[button_raw])
                                                                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                                                if button_ctx.custom_id == "description":
                                                                        await button_ctx.edit_origin(content=nonetxt)
                                                                        descr_embed = tf.getEmbedAttacDescription(ctx,display_character.competences[competence_name])
                                                                        await ctx.send(embed=descr_embed)
                                                                if button_ctx.custom_id == "show buff":
                                                                        await button_ctx.edit_origin(content=nonetxt)
                                                                        buffs_embed = tf.getEmbedAttackBuff(ctx,display_character.competences[competence_name],results)
                                                                        await ctx.send(embed=buffs_embed)
                                                                if button_ctx.custom_id == "undo":
                                                                        await button_ctx.edit_origin(content=nonetxt)
                                                                        target.life = (sktr.getTheAbsoluteZero(target.life[0] + results[1]),target.life[1])
                                                                        display_character.competences[competence_name].last_utilisation = - display_character.competences[competence_name].competence_cooldown
                                                                        st.saveCharacter(display_character,user_name,display_name)
                                                                        await ctx.send("`moddifications register`")
                                                                        st.saveCharacter(target,my_target_path[0],my_target_path[1])
                                                                        await ctx.send("`moddifications register`")
                                                        else:
                                                                my_buttons = [create_button(style=ButtonStyle.blue,
                                                                                            label="description of the skill",
                                                                                            custom_id="description"),
                                                                              create_button(style=ButtonStyle.blue,
                                                                                            label="show buff",
                                                                                            custom_id="show buff")]
                                                                button_raw = create_actionrow(*my_buttons)
                                                                fait_choix = await ctx.send("`Push for show : `", components=[button_raw])
                                                                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                                                if button_ctx.custom_id == "description":
                                                                        await button_ctx.edit_origin(content=nonetxt)
                                                                        descr_embed = tf.getEmbedAttacDescription(ctx,display_character.competences[competence_name])
                                                                        await ctx.send(embed=descr_embed)
                                                                if button_ctx.custom_id == "show buff":
                                                                        await button_ctx.edit_origin(content=nonetxt)
                                                                        buffs_embed = tf.getEmbedAttackBuff(ctx,display_character.competences[competence_name],results)
                                                                        await ctx.send(embed=buffs_embed)




                        elif display_character.competences[competence_name].type[0] in ["transversal_attack"]:
                                await competence_aux.send(nonetxt)


                                my_buttons = [create_button(style=ButtonStyle.blue,
                                                            label="use as a attack",
                                                            custom_id="attack"),
                                              create_button(style=ButtonStyle.blue,
                                                            label="use as a competence",
                                                            custom_id="competence")]
                                button_raw = create_actionrow(*my_buttons)
                                fait_choix = await ctx.send("`Push for chose the mode of utilisation : `", components=[button_raw])
                                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                if button_ctx.custom_id == "attack":
                                        await button_ctx.edit_origin(content="`||use as a Attack||`")
                                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                                    label="display the character list",
                                                                    custom_id="display"),
                                                      create_button(style=ButtonStyle.blue,
                                                                    label="dont display the character list",
                                                                    custom_id="not display")]
                                        button_raw = create_actionrow(*my_buttons)
                                        fait_choix = await ctx.send("`Push for display the character list : `", components=[button_raw])
                                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                        if button_ctx.custom_id == "display":
                                                await button_ctx.edit_origin(content=nonetxt)
                                                character_dict = st.getCharactersDict()
                                                txt = tf.getPlayerArchitectureChar(character_dict)
                                                my_embed_list = tf.getEmbedCharacterDict(ctx ,character_dict)
                                                for my_embed in my_embed_list:
                                                        await ctx.send(embed=my_embed)
                                                await ctx.send("`__enter the name of your target : __`")
                                                try:
                                                        target_name_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                                        target_name = str(target_name_input.content)
                                                except:
                                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                        target_name = "none"
                                                if target_name != "none":
                                                        target_path_list = st.getCharactersPaths(target_name)
                                                        selection = []
                                                        for target_path in target_path_list:
                                                                selection_aux = target_path.split("|")
                                                                selection.append(selection_aux[1] + "(" + target_name + ")")
                                                        target_type_select = tf.getListSelection(ctx,"chose your target",selection,target_path_list) 
                                                        fait_choix = await ctx.send("`Chose your target : `", components=[create_actionrow(target_type_select)])
                                                        target_type = await wait_for_component(notlolabot.bot, components=target_type_select, check=check)
                                                        await target_type.send(nonetxt)
                                                        my_target_path = target_type.values[0].split("|")
                                                        target = st.loadCharacter(my_target_path[0],my_target_path[1],my_target_path[2])


                                                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                                                    label="roll the attack dice",
                                                                                    custom_id="dice")]
                                                        button_raw = create_actionrow(*my_buttons)
                                                        fait_choix = await ctx.send("`Push the result : `", components=[button_raw])
                                                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)


                                                        state_of_caster = sktr.getUpdateStateOfCharacter(display_character)
                                                        display_character.state = (state_of_caster,display_character.state[1],display_character.state[2])
                                                        state_of_target = sktr.getUpdateStateOfCharacter(target)
                                                        target.state = (state_of_target,target.state[1],target.state[2])

                                                                                   
                                                        my_embed = tf.getEmbedStateCharacter(ctx,state_of_caster,state_of_target,char_name,target_name)
                                                        await ctx.send(embed=my_embed)
                                                        if button_ctx.custom_id == "dice":
                                                                await button_ctx.edit_origin(content=nonetxt)  
                                                                display_character.buffs = sktr.updateBuffList(display_character.buffs)
                                                                target.buffs = sktr.updateBuffList(target.buffs)
                                                                display_character.competences[competence_name].last_utilisation = st.getTick()
                                                                results = sktr.getAttackResult(display_character.competences[competence_name],display_character,target,50)
                                                                last_life = copy.copy(target.life)
                                                                if results[0] == True:
                                                                        target.life = (sktr.getTheAbsoluteZero(target.life[0] - results[1]),target.life[1])
                                                                        if display_character.competences[competence_name].type[1] == "buff":
                                                                                target.buffs.append(rp.BuffClass(display_character.competences[competence_name].state[1],display_character.competences[competence_name].buff))
                                                                        if display_character.competences[competence_name].type[1] == "self_buff":
                                                                                display_character.buffs.append(rp.BuffClass(display_character.competences[competence_name].state[1],display_character.competences[competence_name].self_buff))
                                                                if state_of_caster != "iframe" or display_character.competences[competence_name].state[0] == "iframe":
                                                                        display_character.state = (display_character.competences[competence_name].state[0],display_character.competences[competence_name].state[1],st.getTick())
                                                                if display_character.competences[competence_name].state[0] == "block":
                                                                        new_template = {"strength" : (0,0),"dexterity" : (0,0),"bleeding" : (0,0) ,"posture" : display_character.competences[competence_name].posture ,"constitution" : (0,0),"evasion" : (0,0),"intellect" : (0,0),"charisma" : (0,0) ,"wisdom" : (0,0)}
                                                                        display_character.buffs.append(rp.BuffClass(display_character.competences[competence_name].state[1],rp.StatisticsClass("",new_template)))
                                                                st.saveCharacter(display_character,user_name,display_name)
                                                                await ctx.send("`moddifications register`")
                                                                st.saveCharacter(target,my_target_path[0],my_target_path[1])
                                                                await ctx.send("`moddifications register`")
                                                                st.tickUpdate()
                                                                attack_embed = tf.getEmbedAttackRole(ctx ,results,char_name,target_name,display_character,target,last_life)
                                                                await ctx.send(embed=attack_embed)
                                                                if results[0] == True:
                                                                        my_buttons = [create_button(style=ButtonStyle.green,
                                                                                                    label="description of the skill",
                                                                                                    custom_id="description"),
                                                                                      create_button(style=ButtonStyle.green,
                                                                                                    label="show buff",
                                                                                                    custom_id="show buff"),
                                                                                      create_button(style=ButtonStyle.blue,
                                                                                                    label="cancel the attack",
                                                                                                    custom_id="undo")]
                                                                        button_raw = create_actionrow(*my_buttons)
                                                                        fait_choix = await ctx.send("`Push for show : `", components=[button_raw])
                                                                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                                                        if button_ctx.custom_id == "description":
                                                                                await button_ctx.edit_origin(content=nonetxt)
                                                                                descr_embed = tf.getEmbedAttacDescription(ctx,display_character.competences[competence_name])
                                                                                await ctx.send(embed=descr_embed)
                                                                        if button_ctx.custom_id == "show buff":
                                                                                await button_ctx.edit_origin(content=nonetxt)
                                                                                buffs_embed = tf.getEmbedAttackBuff(ctx,display_character.competences[competence_name],results)
                                                                                await ctx.send(embed=buffs_embed)
                                                                        if button_ctx.custom_id == "undo":
                                                                                await button_ctx.edit_origin(content=nonetxt)
                                                                                target.life = (sktr.getTheAbsoluteZero(target.life[0] + results[1]),target.life[1])
                                                                                display_character.competences[competence_name].last_utilisation = - display_character.competences[competence_name].competence_cooldown
                                                                                st.saveCharacter(display_character,user_name,display_name)
                                                                                await ctx.send("`moddifications register`")
                                                                                st.saveCharacter(target,my_target_path[0],my_target_path[1])
                                                                                await ctx.send("`moddifications register`")
                                                                else:
                                                                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                                                                    label="description of the skill",
                                                                                                    custom_id="description"),
                                                                                      create_button(style=ButtonStyle.blue,
                                                                                                    label="show buff",
                                                                                                    custom_id="show buff")]
                                                                        button_raw = create_actionrow(*my_buttons)
                                                                        fait_choix = await ctx.send("`Push for show : `", components=[button_raw])
                                                                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                                                        if button_ctx.custom_id == "description":
                                                                                await button_ctx.edit_origin(content=nonetxt)
                                                                                descr_embed = tf.getEmbedAttacDescription(ctx,display_character.competences[competence_name])
                                                                                await ctx.send(embed=descr_embed)
                                                                        if button_ctx.custom_id == "show buff":
                                                                                await button_ctx.edit_origin(content=nonetxt)
                                                                                buffs_embed = tf.getEmbedAttackBuff(ctx,display_character.competences[competence_name],results)
                                                                                await ctx.send(embed=buffs_embed)
                                                                


                                                        
                                        if button_ctx.custom_id == "not display":
                                                await button_ctx.edit_origin(content=nonetxt)
                                                await ctx.send("`__enter the name of your target : __`")
                                                try:
                                                        target_name_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                                        target_name = str(target_name_input.content)
                                                except:
                                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                        target_name = "none"
                                                if target_name != "none":
                                                        target_path_list = st.getCharactersPaths(target_name)
                                                        selection = []
                                                        for target_path in target_path_list:
                                                                selection_aux = target_path.split("|")
                                                                selection.append(selection_aux[1] + "(" + target_name + ")")
                                                        target_type_select = tf.getListSelection(ctx,"chose your target",selection,target_path_list) 
                                                        fait_choix = await ctx.send("`Chose your target : `", components=[create_actionrow(target_type_select)])
                                                        target_type = await wait_for_component(notlolabot.bot, components=target_type_select, check=check)
                                                        await target_type.send(nonetxt)
                                                        my_target_path = target_type.values[0].split("|")
                                                        target = st.loadCharacter(my_target_path[0],my_target_path[1],my_target_path[2])


                                                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                                                    label="roll the attack dice",
                                                                                    custom_id="dice")]
                                                        button_raw = create_actionrow(*my_buttons)
                                                        fait_choix = await ctx.send("`Push the result : `", components=[button_raw])
                                                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)


                                                        state_of_caster = sktr.getUpdateStateOfCharacter(display_character)
                                                        state_of_target = sktr.getUpdateStateOfCharacter(target)
                                                        my_embed = tf.getEmbedStateCharacter(ctx,state_of_caster,state_of_target,char_name,target_name)
                                                        await ctx.send(embed=my_embed)
                                                        if button_ctx.custom_id == "dice":
                                                                await button_ctx.edit_origin(content=nonetxt)  
                                                                display_character.buffs = sktr.updateBuffList(display_character.buffs)
                                                                target.buffs = sktr.updateBuffList(target.buffs)
                                                                display_character.competences[competence_name].last_utilisation = st.getTick()
                                                                results = sktr.getAttackResult(display_character.competences[competence_name],display_character,target,50)
                                                                last_life = copy.copy(target.life)
                                                                if results[0] == True:
                                                                        target.life = (sktr.getTheAbsoluteZero(target.life[0] - results[1]),target.life[1])
                                                                        if display_character.competences[competence_name].type[1] == "buff":
                                                                                target.buffs.append(rp.BuffClass(display_character.competences[competence_name].state[1],display_character.competences[competence_name].buff))
                                                                        if display_character.competences[competence_name].type[1] == "self_buff":
                                                                                display_character.buffs.append(rp.BuffClass(display_character.competences[competence_name].state[1],display_character.competences[competence_name].self_buff))
                                                                if state_of_caster != "iframe" or display_character.competences[competence_name].state[0] == "iframe":
                                                                        display_character.state = (display_character.competences[competence_name].state[0],display_character.competences[competence_name].state[1],st.getTick())
                                                                if display_character.competences[competence_name].state[0] == "block":
                                                                        new_template = {"strength" : (0,0),"dexterity" : (0,0),"bleeding" : (0,0) ,"posture" : display_character.competences[competence_name].posture ,"constitution" : (0,0),"evasion" : (0,0),"intellect" : (0,0),"charisma" : (0,0) ,"wisdom" : (0,0)}
                                                                        display_character.buffs.append(rp.BuffClass(display_character.competences[competence_name].state[1],rp.StatisticsClass("",new_template)))
                                                                st.saveCharacter(display_character,user_name,display_name)
                                                                await ctx.send("`moddifications register`")
                                                                st.saveCharacter(target,my_target_path[0],my_target_path[1])
                                                                await ctx.send("`moddifications register`")
                                                                st.tickUpdate()
                                                                attack_embed = tf.getEmbedAttackRole(ctx ,results,char_name,target_name,display_character,target,last_life)
                                                                await ctx.send(embed=attack_embed)
                                                                if results[0] == True:
                                                                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                                                                    label="description of the skill",
                                                                                                    custom_id="description"),
                                                                                      create_button(style=ButtonStyle.blue,
                                                                                                    label="show buff",
                                                                                                    custom_id="show buff"),
                                                                                      create_button(style=ButtonStyle.blue,
                                                                                                    label="cancel the attack",
                                                                                                    custom_id="undo")]
                                                                        button_raw = create_actionrow(*my_buttons)
                                                                        fait_choix = await ctx.send("`Push for show : `", components=[button_raw])
                                                                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                                                        if button_ctx.custom_id == "description":
                                                                                await button_ctx.edit_origin(content=nonetxt)
                                                                                descr_embed = tf.getEmbedAttacDescription(ctx,display_character.competences[competence_name])
                                                                                await ctx.send(embed=descr_embed)
                                                                        if button_ctx.custom_id == "show buff":
                                                                                await button_ctx.edit_origin(content=nonetxt)
                                                                                buffs_embed = tf.getEmbedAttackBuff(ctx,display_character.competences[competence_name],results)
                                                                                await ctx.send(embed=buffs_embed)
                                                                        if button_ctx.custom_id == "undo":
                                                                                await button_ctx.edit_origin(content=nonetxt)
                                                                                target.life = (sktr.getTheAbsoluteZero(target.life[0] + results[1]),target.life[1])
                                                                                display_character.competences[competence_name].last_utilisation = - display_character.competences[competence_name].competence_cooldown
                                                                                st.saveCharacter(display_character,user_name,display_name)
                                                                                await ctx.send("`moddifications register`")
                                                                                st.saveCharacter(target,my_target_path[0],my_target_path[1])
                                                                                await ctx.send("`moddifications register`")
                                                                else:
                                                                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                                                                    label="description of the skill",
                                                                                                    custom_id="description"),
                                                                                      create_button(style=ButtonStyle.blue,
                                                                                                    label="show buff",
                                                                                                    custom_id="show buff")]
                                                                        button_raw = create_actionrow(*my_buttons)
                                                                        fait_choix = await ctx.send("`Push for show : `", components=[button_raw])
                                                                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                                                        if button_ctx.custom_id == "description":
                                                                                await button_ctx.edit_origin(content=nonetxt)
                                                                                descr_embed = tf.getEmbedAttacDescription(ctx,display_character.competences[competence_name])
                                                                                await ctx.send(embed=descr_embed)
                                                                        if button_ctx.custom_id == "show buff":
                                                                                await button_ctx.edit_origin(content=nonetxt)
                                                                                buffs_embed = tf.getEmbedAttackBuff(ctx,display_character.competences[competence_name],results)
                                                                                await ctx.send(embed=buffs_embed)
                                if button_ctx.custom_id == "competence":
                                        await button_ctx.edit_origin(content="`||use as a Competence||`")
                                        display_character.state = (display_character.competences[competence_name].state[0],display_character.competences[competence_name].state[1],st.getTick())
                                        display_character.competences[competence_name].last_utilisation = st.getTick()
                                        if display_character.competences[competence_name].type[1] == "self_buff":
                                                display_character.buffs.append(rp.BuffClass(display_character.competences[competence_name].state[1],display_character.competences[competence_name].self_buff))
                                        st.saveCharacter(display_character,user_name,display_name)
                                        st.tickUpdate()
                                        await ctx.send("`competence utilisée`")

                                        
                                
                                pass
                        elif display_character.competences[competence_name].type[0] in ["massiv_skill"]:
                                await competence_aux.send(nonetxt)
                                my_buttons = [create_button(style=ButtonStyle.blue,
                                                            label="display the character list",
                                                            custom_id="display"),
                                              create_button(style=ButtonStyle.blue,
                                                            label="dont display the character list",
                                                            custom_id="not display")]
                                button_raw = create_actionrow(*my_buttons)
                                fait_choix = await ctx.send("`Push for display the character list : `", components=[button_raw])
                                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                if button_ctx.custom_id == "display":
                                        await button_ctx.edit_origin(content=nonetxt)
                                        character_dict = st.getCharactersDict()
                                        txt = tf.getPlayerArchitectureChar(character_dict)
                                        my_embed_list = tf.getEmbedCharacterDict(ctx ,character_dict)
                                        for my_embed in my_embed_list:
                                                await ctx.send(embed=my_embed)
                                        await ctx.send("`__enter the names of your targets : __`")
                                        await ctx.send("`target1|target2|target3|target4........`")
                                        try:
                                                target_names_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                                target_names = str(target_names_input.content)
                                        except:
                                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                target_names = "none"
                                        if target_names != "none":
                                                targets_list = target_names.split("|")
                                                selection_target = []
                                                new_target_path_list = []
                                                for target_name in targets_list:
                                                        target_path_list = st.getCharactersPaths(target_name)
                                                        new_target_path_list = new_target_path_list + target_path_list
                                                        selection = []
                                                        for target_path in target_path_list:
                                                                selection_aux = target_path.split("|")
                                                                selection.append(selection_aux[1] + "(" + target_name + ")")
                                                        selection_target = selection_target + selection
                                                if display_character.competences[competence_name].level <= 14:
                                                        if len(selection_target) < 3:
                                                                targets_selection = tf.getListSelection(ctx,"chose the targets",selection_target,new_target_path_list,1,len(selection_target))
                                                                fait_choix = await ctx.send("`Chose the targets : `", components=[create_actionrow(targets_selection)])
                                                                targets_list_path = await wait_for_component(notlolabot.bot, components=targets_selection, check=check)
                                                                await targets_list_path.send(nonetxt)
                                                                pass
                                                        else:
                                                                targets_selection = tf.getListSelection(ctx,"chose the targets",selection_target,new_target_path_list,1,3)
                                                                fait_choix = await ctx.send("`Chose the targets : `", components=[create_actionrow(targets_selection)])
                                                                targets_list_path = await wait_for_component(notlolabot.bot, components=targets_selection, check=check)
                                                                await targets_list_path.send(nonetxt)
                                                else:
                                                        if len(selection_target) < 8:
                                                                targets_selection = tf.getListSelection(ctx,"chose the targets",selection_target,new_target_path_list,1,len(selection_target))
                                                                fait_choix = await ctx.send("`Chose the targets : `", components=[create_actionrow(targets_selection)])
                                                                targets_list_path = await wait_for_component(notlolabot.bot, components=targets_selection, check=check)
                                                                await targets_list_path.send(nonetxt)
                                                                pass
                                                        else:
                                                                targets_selection = tf.getListSelection(ctx,"chose the targets",selection_target,new_target_path_list,1,8)
                                                                fait_choix = await ctx.send("`Chose the targets : `", components=[create_actionrow(targets_selection)])
                                                                targets_list_path = await wait_for_component(notlolabot.bot, components=targets_selection, check=check)
                                                                await targets_list_path.send(nonetxt)
                                                        pass
                                                if targets_list_path.values != []:
                                                        display_character.competences[competence_name].last_utilisation = st.getTick()
                                                        st.saveCharacter(display_character,user_name,display_name)
                                                        for k in range(len(targets_list_path.values)):
                                                                my_target_path = targets_list_path.values[k].split("|")
                                                                target = st.loadCharacter(my_target_path[0],my_target_path[1],my_target_path[2])
                                                                target.buffs.append(rp.BuffClass(display_character.competences[competence_name].state[1],display_character.competences[competence_name].buff))
                                                                st.saveCharacter(target,my_target_path[0],my_target_path[1])
                                                                await ctx.send("buffs add")
                                                        pass
                                if button_ctx.custom_id == "not display":
                                        await button_ctx.edit_origin(content=nonetxt)
                                        await ctx.send("`__enter the names of your targets : __`")
                                        await ctx.send("`target1|target2|target3|target4........`")
                                        try:
                                                target_names_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                                target_names = str(target_names_input.content)
                                        except:
                                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                target_names = "none"
                                        if target_names != "none":
                                                targets_list = target_names.split("|")
                                                selection_target = []
                                                new_target_path_list = []
                                                for target_name in targets_list:
                                                        target_path_list = st.getCharactersPaths(target_name)
                                                        new_target_path_list = new_target_path_list + target_path_list
                                                        selection = []
                                                        for target_path in target_path_list:
                                                                selection_aux = target_path.split("|")
                                                                selection.append(selection_aux[1] + "(" + target_name + ")")
                                                        selection_target = selection_target + selection
                                                if display_character.competences[competence_name].level <= 14:
                                                        if len(selection_target) < 3:
                                                                targets_selection = tf.getListSelection(ctx,"chose the targets",selection_target,new_target_path_list,1,len(selection_target))
                                                                fait_choix = await ctx.send("`Chose the targets : `", components=[create_actionrow(targets_selection)])
                                                                targets_list_path = await wait_for_component(notlolabot.bot, components=targets_selection, check=check)
                                                                await targets_list_path.send(nonetxt)
                                                                pass
                                                        else:
                                                                targets_selection = tf.getListSelection(ctx,"chose the targets",selection_target,new_target_path_list,1,3)
                                                                fait_choix = await ctx.send("`Chose the targets : `", components=[create_actionrow(targets_selection)])
                                                                targets_list_path = await wait_for_component(notlolabot.bot, components=targets_selection, check=check)
                                                                await targets_list_path.send(nonetxt)
                                                else:
                                                        if len(selection_target) < 8:
                                                                targets_selection = tf.getListSelection(ctx,"chose the targets",selection_target,new_target_path_list,1,len(selection_target))
                                                                fait_choix = await ctx.send("`Chose the targets : `", components=[create_actionrow(targets_selection)])
                                                                targets_list_path = await wait_for_component(notlolabot.bot, components=targets_selection, check=check)
                                                                await targets_list_path.send(nonetxt)
                                                                pass
                                                        else:
                                                                targets_selection = tf.getListSelection(ctx,"chose the targets",selection_target,new_target_path_list,1,8)
                                                                fait_choix = await ctx.send("`Chose the targets : `", components=[create_actionrow(targets_selection)])
                                                                targets_list_path = await wait_for_component(notlolabot.bot, components=targets_selection, check=check)
                                                                await targets_list_path.send(nonetxt)
                                                        pass
                                                if targets_list_path.values != []:
                                                        display_character.competences[competence_name].last_utilisation = st.getTick()
                                                        st.saveCharacter(display_character,user_name,display_name)
                                                        for k in range(len(targets_list_path.values)):
                                                                my_target_path = targets_list_path.values[k].split("|")
                                                                target = st.loadCharacter(my_target_path[0],my_target_path[1],my_target_path[2])
                                                                target.buffs.append(rp.BuffClass(display_character.competences[competence_name].state[1],display_character.competences[competence_name].buff))
                                                                st.saveCharacter(target,my_target_path[0],my_target_path[1])
                                                                await ctx.send("buffs add")
                                                        pass
                        else:
                                await competence_aux.send(nonetxt)
                                display_character.state = (display_character.competences[competence_name].state[0],display_character.competences[competence_name].state[1],st.getTick())
                                display_character.competences[competence_name].last_utilisation = st.getTick()
                                if display_character.competences[competence_name].type[1] == "self_buff":
                                        display_character.buffs.append(rp.BuffClass(display_character.competences[competence_name].state[1],display_character.competences[competence_name].self_buff))
                                st.saveCharacter(display_character,user_name,display_name)
                                st.tickUpdate()
                                await ctx.send("`competence utilisée`")

                if action_type.values[0] == "characteristic dice":
                        await action_type.send("`||characteristic dice||`")
                        selection = ["arcanes","athletics","discretion","history","intimidation","investigation",
                                     "medicine","religion","survive","occultism","calm"]
                        characteristic_type_select = tf.getListSelection(ctx,"chose the dice roll",selection,selection) 
                        fait_choix = await ctx.send("`chose the dice roll : `", components=[create_actionrow(characteristic_type_select)])
                        characteristic_type = await wait_for_component(notlolabot.bot, components=characteristic_type_select, check=check)
                        characteristic = characteristic_type.values[0]
                        await characteristic_type.send(nonetxt)


                        level_type_select = tf.getListSelection(ctx,"choix du palier",["20","40","50","60","80","90"],["20","40","50","60","80","90"]) 
                        fait_choix = await ctx.send("`chose the level of the dice : `", components=[create_actionrow(level_type_select)])
                        level_type = await wait_for_component(notlolabot.bot, components=level_type_select, check=check)
                        palier = int(level_type.values[0])
                        await level_type.send("`the roll level chose is : `  `_-|" + level_type.values[0] + "|-_`")

                        
                        my_buttons = [create_button(style=ButtonStyle.green,
                                                    label="roll the " + characteristic + " dice",
                                                    custom_id="dice")]
                        button_raw = create_actionrow(*my_buttons)
                        fait_choix = await ctx.send("`Push the result : `", components=[button_raw])
                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                        if button_ctx.custom_id == "dice":
                                await button_ctx.edit_origin(content=nonetxt)  
                                results = sktr.getCharacteristicDiceResult(display_character,palier,characteristic)
                                my_embed = tf.getLiteEmbedCharacteristicRole(ctx,results, characteristic, palier)
                                await ctx.send(embed=my_embed)
                if action_type.values[0] == "mass entity":
                        await action_type.send("`||use a mass entity skill||`")
                        await ctx.send("en cours de construction , maj a venir")
                if action_type.values[0] == "use a ritual":
                        await action_type.send("`||use a ritual | Competence||`")
                        usable_skill_list = sktr.getUsableRitualList(display_character)
                        competence_select = tf.getListSelection(ctx,"chose the skill to use",usable_skill_list,usable_skill_list) 
                        fait_choix = await ctx.send("`chose the skill to use : `", components=[create_actionrow(competence_select)])
                        competence_aux = await wait_for_component(notlolabot.bot, components=competence_select, check=check)
                        competence_name = competence_aux.values[0]
                        if display_character.competences[competence_name].type[0] in ["ritual_skill"]:
                                await competence_aux.send(nonetxt)
                                if display_character.competences[competence_name].type[1] == "buff":
                                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                                    label="display the character list",
                                                                    custom_id="display"),
                                                      create_button(style=ButtonStyle.blue,
                                                                    label="dont display the character list",
                                                                    custom_id="not display")]
                                        button_raw = create_actionrow(*my_buttons)
                                        fait_choix = await ctx.send("`Push for display the character list : `", components=[button_raw])
                                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                        if button_ctx.custom_id == "display":
                                                await button_ctx.edit_origin(content=nonetxt)
                                                character_dict = st.getCharactersDict()
                                                txt = tf.getPlayerArchitectureChar(character_dict)
                                                my_embed_list = tf.getEmbedCharacterDict(ctx ,character_dict)
                                                for my_embed in my_embed_list:
                                                        await ctx.send(embed=my_embed)
                                                await ctx.send("`__enter the names of your targets : __`")
                                                await ctx.send("`target1|target2|target3|target4........`")
                                                try:
                                                        target_names_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                                        target_names = str(target_names_input.content)
                                                except:
                                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                        target_names = "none"
                                                if target_names != "none":
                                                        targets_list = target_names.split("|")
                                                        selection_target = []
                                                        new_target_path_list = []
                                                        for target_name in targets_list:
                                                                target_path_list = st.getCharactersPaths(target_name)
                                                                new_target_path_list = new_target_path_list + target_path_list
                                                                selection = []
                                                                for target_path in target_path_list:
                                                                        selection_aux = target_path.split("|")
                                                                        selection.append(selection_aux[1] + "(" + target_name + ")")
                                                                selection_target = selection_target + selection
                                                        if len(selection_target) < 9:
                                                                targets_selection = tf.getListSelection(ctx,"chose the targets",selection_target,new_target_path_list,1,len(selection_target))
                                                                fait_choix = await ctx.send("`Chose the targets : `", components=[create_actionrow(targets_selection)])
                                                                targets_list_path = await wait_for_component(notlolabot.bot, components=targets_selection, check=check)
                                                                await targets_list_path.send(nonetxt)
                                                                pass
                                                        else:
                                                                targets_selection = tf.getListSelection(ctx,"chose the targets",selection_target,new_target_path_list,1,9)
                                                                fait_choix = await ctx.send("`Chose the targets : `", components=[create_actionrow(targets_selection)])
                                                                targets_list_path = await wait_for_component(notlolabot.bot, components=targets_selection, check=check)
                                                                await targets_list_path.send(nonetxt)
                                                        if targets_list_path.values != []:
                                                                display_character.competences[competence_name].last_utilisation = st.getTick()
                                                                st.saveCharacter(display_character,user_name,display_name)
                                                                for k in range(len(targets_list_path.values)):
                                                                        my_target_path = targets_list_path.values[k].split("|")
                                                                        target = st.loadCharacter(my_target_path[0],my_target_path[1],my_target_path[2])
                                                                        target.buffs.append(rp.BuffClass(display_character.competences[competence_name].state[1],display_character.competences[competence_name].buff))
                                                                        target.state = (display_character.competences[competence_name].state[0],display_character.competences[competence_name].state[1],st.getTick())
                                                                        st.saveCharacter(target,my_target_path[0],my_target_path[1])
                                                                        await ctx.send("buffs add")
                                                                pass
                                        if button_ctx.custom_id == "not display":
                                                await button_ctx.edit_origin(content=nonetxt)
                                                await ctx.send("`__enter the names of your targets : __`")
                                                await ctx.send("`target1|target2|target3|target4........`")
                                                try:
                                                        target_names_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                                        target_names = str(target_names_input.content)
                                                except:
                                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                        target_names = "none"
                                                if target_names != "none":
                                                        targets_list = target_names.split("|")
                                                        selection_target = []
                                                        new_target_path_list = []
                                                        for target_name in targets_list:
                                                                target_path_list = st.getCharactersPaths(target_name)
                                                                new_target_path_list = new_target_path_list + target_path_list
                                                                selection = []
                                                                for target_path in target_path_list:
                                                                        selection_aux = target_path.split("|")
                                                                        selection.append(selection_aux[1] + "(" + target_name + ")")
                                                                selection_target = selection_target + selection
                                                        if len(selection_target) < 9:
                                                                targets_selection = tf.getListSelection(ctx,"chose the targets",selection_target,new_target_path_list,1,len(selection_target))
                                                                fait_choix = await ctx.send("`Chose the targets : `", components=[create_actionrow(targets_selection)])
                                                                targets_list_path = await wait_for_component(notlolabot.bot, components=targets_selection, check=check)
                                                                await targets_list_path.send(nonetxt)
                                                                pass
                                                        else:
                                                                targets_selection = tf.getListSelection(ctx,"chose the targets",selection_target,new_target_path_list,1,9)
                                                                fait_choix = await ctx.send("`Chose the targets : `", components=[create_actionrow(targets_selection)])
                                                                targets_list_path = await wait_for_component(notlolabot.bot, components=targets_selection, check=check)
                                                                await targets_list_path.send(nonetxt)
                                                        if targets_list_path.values != []:
                                                                display_character.competences[competence_name].last_utilisation = st.getTick()
                                                                st.saveCharacter(display_character,user_name,display_name)
                                                                for k in range(len(targets_list_path.values)):
                                                                        my_target_path = targets_list_path.values[k].split("|")
                                                                        target = st.loadCharacter(my_target_path[0],my_target_path[1],my_target_path[2])
                                                                        target.buffs.append(rp.BuffClass(display_character.competences[competence_name].state[1],display_character.competences[competence_name].buff))
                                                                        target.state = (display_character.competences[competence_name].state[0],display_character.competences[competence_name].state[1],st.getTick())
                                                                        st.saveCharacter(target,my_target_path[0],my_target_path[1])
                                                                        await ctx.send("buffs add")
                                                                pass

                if action_type.values[0] == "use a item":
                        await action_type.send("`||use a item | consumable||`")
                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                    label="display the inventory",
                                                    custom_id="display"),
                                      create_button(style=ButtonStyle.blue,
                                                    label="dont display the inventory",
                                                    custom_id="not display")]
                        button_raw = create_actionrow(*my_buttons)
                        fait_choix = await ctx.send("`Push for display your inventory : `", components=[button_raw])
                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                        if button_ctx.custom_id == "display":
                                embed_list = tf.getListInventoryCharacterEmbedImage(ctx,display_character)
                                for embed in embed_list:
                                        await ctx.send(embed=embed)
                                my_buttons = [create_button(style=ButtonStyle.blue,
                                                            label="use a item",
                                                            custom_id="use a item"),
                                              create_button(style=ButtonStyle.blue,
                                                            label="left the display",
                                                            custom_id="left the display")]
                                button_raw = create_actionrow(*my_buttons)
                                fait_choix = await ctx.send("`Push the button for display or change a option : `", components=[button_raw])
                                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                if button_ctx.custom_id == "use a item":
                                        await button_ctx.edit_origin(content=nonetxt)
                                        await ctx.send("`__enter the name of the consummable to use__`")
                                        try:
                                                item_name_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                                item_name = str(item_name_input.content)
                                        except:
                                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                item_name = "none"
                                        if item_name != "none":
                                                if item_name in display_character.inventory.keys():
                                                        if isinstance(display_character.inventory[item_name],rp.ConsumableClass):
                                                                if display_character.inventory[item_name].quantity > 0:
                                                                        display_character.inventory[item_name].quantity = display_character.inventory[item_name].quantity - 1
                                                                        if display_character.life[0] + display_character.inventory[item_name].life > display_character.life[1]:
                                                                                display_character.life = (display_character.life[1],display_character.life[1])
                                                                        else:
                                                                                display_character.life = (display_character.life[0] + display_character.inventory[item_name].life,display_character.life[1])
                                                                        st.saveCharacter(display_character,user_name,display_name)
                                                                        st.tickUpdate()
                                                                        await ctx.send("`" + item_name + "` : **used**.")
                                                                if display_character.inventory[item_name].quantity == 1:
                                                                        del display_character.inventory[item_name]
                                                                        if display_character.life[0] + display_character.inventory[item_name].life > display_character.life[1]:
                                                                                display_character.life = (display_character.life[1],display_character.life[1])
                                                                        else:
                                                                                display_character.life = (display_character.life[0] + display_character.inventory[item_name].life,display_character.life[1])
                                                                        st.saveCharacter(display_character,user_name,display_name)
                                                                        st.tickUpdate()
                                                                        await ctx.send("`" + item_name + "` : **used**.")
                                                                else:
                                                                        await ctx.send("`" + item_name + "` : **can't be used**.")
                                                        elif isinstance(display_character.inventory[item_name],rp.MagicalConsumableClass) or isinstance(display_character.inventory[item_name],rp.MagicalItemClass):
                                                                if True:
                                                                        if display_character.inventory[item_name].competence.type[0] in ["transversal_attack"]:
                                                                                my_buttons = [create_button(style=ButtonStyle.blue,
                                                                                                            label="use as a attack",
                                                                                                            custom_id="attack"),
                                                                                              create_button(style=ButtonStyle.blue,
                                                                                                            label="use as a competence",
                                                                                                            custom_id="competence")]
                                                                                button_raw = create_actionrow(*my_buttons)
                                                                                fait_choix = await ctx.send("`Push for chose the mode of utilisation : `", components=[button_raw])
                                                                                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                                                                if button_ctx.custom_id == "attack":
                                                                                        await button_ctx.edit_origin(content="`||use as a Attack||`")
                                                                                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                                                                                    label="display the character list",
                                                                                                                    custom_id="display"),
                                                                                                      create_button(style=ButtonStyle.blue,
                                                                                                                    label="dont display the character list",
                                                                                                                    custom_id="not display")]
                                                                                        button_raw = create_actionrow(*my_buttons)
                                                                                        fait_choix = await ctx.send("`Push for display the character list : `", components=[button_raw])
                                                                                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                                                                        if button_ctx.custom_id == "display":
                                                                                                await button_ctx.edit_origin(content=nonetxt)
                                                                                                character_dict = st.getCharactersDict()
                                                                                                txt = tf.getPlayerArchitectureChar(character_dict)
                                                                                                my_embed_list = tf.getEmbedCharacterDict(ctx ,character_dict)
                                                                                                for my_embed in my_embed_list:
                                                                                                        await ctx.send(embed=my_embed)
                                                                                                await ctx.send("`__enter the name of your target : __`")
                                                                                                try:
                                                                                                        target_name_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                                                                                        target_name = str(target_name_input.content)
                                                                                                except:
                                                                                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                                                                        target_name = "none"
                                                                                                if target_name != "none":
                                                                                                        target_path_list = st.getCharactersPaths(target_name)
                                                                                                        selection = []
                                                                                                        for target_path in target_path_list:
                                                                                                                selection_aux = target_path.split("|")
                                                                                                                selection.append(selection_aux[1] + "(" + target_name + ")")
                                                                                                        target_type_select = tf.getListSelection(ctx,"chose your target",selection,target_path_list) 
                                                                                                        fait_choix = await ctx.send("`Chose your target : `", components=[create_actionrow(target_type_select)])
                                                                                                        target_type = await wait_for_component(notlolabot.bot, components=target_type_select, check=check)
                                                                                                        await target_type.send(nonetxt)
                                                                                                        my_target_path = target_type.values[0].split("|")
                                                                                                        target = st.loadCharacter(my_target_path[0],my_target_path[1],my_target_path[2])


                                                                                                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                                                                                                    label="roll the attack dice",
                                                                                                                                    custom_id="dice")]
                                                                                                        button_raw = create_actionrow(*my_buttons)
                                                                                                        fait_choix = await ctx.send("`Push the result : `", components=[button_raw])
                                                                                                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)


                                                                                                        state_of_caster = sktr.getUpdateStateOfCharacter(display_character)
                                                                                                        display_character.state = (state_of_caster,display_character.state[1],display_character.state[2])
                                                                                                        state_of_target = sktr.getUpdateStateOfCharacter(target)
                                                                                                        target.state = (state_of_target,target.state[1],target.state[2])

                                                                                                                                   
                                                                                                        my_embed = tf.getEmbedStateCharacter(ctx,state_of_caster,state_of_target,char_name,target_name)
                                                                                                        await ctx.send(embed=my_embed)
                                                                                                        if button_ctx.custom_id == "dice":
                                                                                                                await button_ctx.edit_origin(content=nonetxt)  
                                                                                                                display_character.buffs = sktr.updateBuffList(display_character.buffs)
                                                                                                                target.buffs = sktr.updateBuffList(target.buffs)
                                                                                                                if isinstance(display_character.inventory[item_name],rp.MagicalItemClass):
                                                                                                                        display_character.inventory[item_name].competence.last_utilisation = st.getTick()
                                                                                                                results = sktr.getAttackResult(display_character.inventory[item_name].competence,display_character,target,50)
                                                                                                                last_life = copy.copy(target.life)
                                                                                                                if results[0] == True:
                                                                                                                        target.life = (sktr.getTheAbsoluteZero(target.life[0] - results[1]),target.life[1])
                                                                                                                        if display_character.competences[competence_name].type[1] == "buff":
                                                                                                                                target.buffs.append(rp.BuffClass(display_character.inventory[item_name].competence.state[1],display_character.inventory[item_name].competence.buff))
                                                                                                                        if display_character.competences[competence_name].type[1] == "self_buff":
                                                                                                                                display_character.buffs.append(rp.BuffClass(display_character.inventory[item_name].competence.state[1],display_character.inventory[item_name].competence.self_buff))
                                                                                                                if state_of_caster != "iframe" or display_character.inventory[item_name].competence.state[0] == "iframe":
                                                                                                                        display_character.state = (display_character.inventory[item_name].competence.state[0],display_character.inventory[item_name].competence.state[1],st.getTick())
                                                                                                                if display_character.inventory[item_name].competence.state[0] == "block":
                                                                                                                        new_template = {"strength" : (0,0),"dexterity" : (0,0),"bleeding" : (0,0) ,"posture" : display_character.inventory[item_name].competence.posture ,"constitution" : (0,0),"evasion" : (0,0),"intellect" : (0,0),"charisma" : (0,0) ,"wisdom" : (0,0)}
                                                                                                                        display_character.buffs.append(rp.BuffClass(display_character.inventory[item_name].competence.state[1],rp.StatisticsClass("",new_template)))
                                                                                                                st.saveCharacter(display_character,user_name,display_name)
                                                                                                                await ctx.send("`moddifications register`")
                                                                                                                st.saveCharacter(target,my_target_path[0],my_target_path[1])
                                                                                                                await ctx.send("`moddifications register`")
                                                                                                                st.tickUpdate()
                                                                                                                attack_embed = tf.getEmbedAttackRole(ctx ,results,char_name,target_name,display_character,target,last_life)
                                                                                                                await ctx.send(embed=attack_embed)
                                                                                                                if results[0] == True:
                                                                                                                        my_buttons = [create_button(style=ButtonStyle.green,
                                                                                                                                                    label="description of the skill",
                                                                                                                                                    custom_id="description"),
                                                                                                                                      create_button(style=ButtonStyle.green,
                                                                                                                                                    label="show buff",
                                                                                                                                                    custom_id="show buff"),
                                                                                                                                      create_button(style=ButtonStyle.blue,
                                                                                                                                                    label="cancel the attack",
                                                                                                                                                    custom_id="undo")]
                                                                                                                        button_raw = create_actionrow(*my_buttons)
                                                                                                                        fait_choix = await ctx.send("`Push for show : `", components=[button_raw])
                                                                                                                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                                                                                                        if button_ctx.custom_id == "description":
                                                                                                                                await button_ctx.edit_origin(content=nonetxt)
                                                                                                                                descr_embed = tf.getEmbedAttacDescription(ctx,display_character.inventory[item_name].competence)
                                                                                                                                await ctx.send(embed=descr_embed)
                                                                                                                        if button_ctx.custom_id == "show buff":
                                                                                                                                await button_ctx.edit_origin(content=nonetxt)
                                                                                                                                buffs_embed = tf.getEmbedAttackBuff(ctx,display_character.inventory[item_name].competence,results)
                                                                                                                                await ctx.send(embed=buffs_embed)
                                                                                                                        if button_ctx.custom_id == "undo":
                                                                                                                                await button_ctx.edit_origin(content=nonetxt)
                                                                                                                                target.life = (sktr.getTheAbsoluteZero(target.life[0] + results[1]),target.life[1])
                                                                                                                                
                                                                                                                                st.saveCharacter(display_character,user_name,display_name)
                                                                                                                                await ctx.send("`moddifications register`")
                                                                                                                                st.saveCharacter(target,my_target_path[0],my_target_path[1])
                                                                                                                                await ctx.send("`moddifications register`")
                                                                                                                else:
                                                                                                                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                                                                                                                    label="description of the skill",
                                                                                                                                                    custom_id="description"),
                                                                                                                                      create_button(style=ButtonStyle.blue,
                                                                                                                                                    label="show buff",
                                                                                                                                                    custom_id="show buff")]
                                                                                                                        button_raw = create_actionrow(*my_buttons)
                                                                                                                        fait_choix = await ctx.send("`Push for show : `", components=[button_raw])
                                                                                                                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                                                                                                        if button_ctx.custom_id == "description":
                                                                                                                                await button_ctx.edit_origin(content=nonetxt)
                                                                                                                                descr_embed = tf.getEmbedAttacDescription(ctx,display_character.inventory[item_name].competence)
                                                                                                                                await ctx.send(embed=descr_embed)
                                                                                                                        if button_ctx.custom_id == "show buff":
                                                                                                                                await button_ctx.edit_origin(content=nonetxt)
                                                                                                                                buffs_embed = tf.getEmbedAttackBuff(ctx,display_character.inventory[item_name].competence,results)
                                                                                                                                await ctx.send(embed=buffs_embed)
                                                                                                                


                                                                                                        
                                                                                        if button_ctx.custom_id == "not display":
                                                                                                await button_ctx.edit_origin(content=nonetxt)
                                                                                                await ctx.send("`__enter the name of your target : __`")
                                                                                                try:
                                                                                                        target_name_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                                                                                        target_name = str(target_name_input.content)
                                                                                                except:
                                                                                                        await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                                                                        target_name = "none"
                                                                                                if target_name != "none":
                                                                                                        target_path_list = st.getCharactersPaths(target_name)
                                                                                                        selection = []
                                                                                                        for target_path in target_path_list:
                                                                                                                selection_aux = target_path.split("|")
                                                                                                                selection.append(selection_aux[1] + "(" + target_name + ")")
                                                                                                        target_type_select = tf.getListSelection(ctx,"chose your target",selection,target_path_list) 
                                                                                                        fait_choix = await ctx.send("`Chose your target : `", components=[create_actionrow(target_type_select)])
                                                                                                        target_type = await wait_for_component(notlolabot.bot, components=target_type_select, check=check)
                                                                                                        await target_type.send(nonetxt)
                                                                                                        my_target_path = target_type.values[0].split("|")
                                                                                                        target = st.loadCharacter(my_target_path[0],my_target_path[1],my_target_path[2])


                                                                                                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                                                                                                    label="roll the attack dice",
                                                                                                                                    custom_id="dice")]
                                                                                                        button_raw = create_actionrow(*my_buttons)
                                                                                                        fait_choix = await ctx.send("`Push the result : `", components=[button_raw])
                                                                                                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)


                                                                                                        state_of_caster = sktr.getUpdateStateOfCharacter(display_character)
                                                                                                        display_character.state = (state_of_caster,display_character.state[1],display_character.state[2])
                                                                                                        state_of_target = sktr.getUpdateStateOfCharacter(target)
                                                                                                        target.state = (state_of_target,target.state[1],target.state[2])

                                                                                                                                   
                                                                                                        my_embed = tf.getEmbedStateCharacter(ctx,state_of_caster,state_of_target,char_name,target_name)
                                                                                                        await ctx.send(embed=my_embed)
                                                                                                        if button_ctx.custom_id == "dice":
                                                                                                                await button_ctx.edit_origin(content=nonetxt)  
                                                                                                                display_character.buffs = sktr.updateBuffList(display_character.buffs)
                                                                                                                target.buffs = sktr.updateBuffList(target.buffs)
                                                                                                                if isinstance(display_character.inventory[item_name],rp.MagicalItemClass):
                                                                                                                        display_character.inventory[item_name].competence.last_utilisation = st.getTick()
                                                                                                                results = sktr.getAttackResult(display_character.inventory[item_name].competence,display_character,target,50)
                                                                                                                last_life = copy.copy(target.life)
                                                                                                                if results[0] == True:
                                                                                                                        target.life = (sktr.getTheAbsoluteZero(target.life[0] - results[1]),target.life[1])
                                                                                                                        if display_character.competences[competence_name].type[1] == "buff":
                                                                                                                                target.buffs.append(rp.BuffClass(display_character.inventory[item_name].competence.state[1],display_character.inventory[item_name].competence.buff))
                                                                                                                        if display_character.competences[competence_name].type[1] == "self_buff":
                                                                                                                                display_character.buffs.append(rp.BuffClass(display_character.inventory[item_name].competence.state[1],display_character.inventory[item_name].competence.self_buff))
                                                                                                                if state_of_caster != "iframe" or display_character.inventory[item_name].competence.state[0] == "iframe":
                                                                                                                        display_character.state = (display_character.inventory[item_name].competence.state[0],display_character.inventory[item_name].competence.state[1],st.getTick())
                                                                                                                if display_character.inventory[item_name].competence.state[0] == "block":
                                                                                                                        new_template = {"strength" : (0,0),"dexterity" : (0,0),"bleeding" : (0,0) ,"posture" : display_character.inventory[item_name].competence.posture ,"constitution" : (0,0),"evasion" : (0,0),"intellect" : (0,0),"charisma" : (0,0) ,"wisdom" : (0,0)}
                                                                                                                        display_character.buffs.append(rp.BuffClass(display_character.inventory[item_name].competence.state[1],rp.StatisticsClass("",new_template)))
                                                                                                                st.saveCharacter(display_character,user_name,display_name)
                                                                                                                await ctx.send("`moddifications register`")
                                                                                                                st.saveCharacter(target,my_target_path[0],my_target_path[1])
                                                                                                                await ctx.send("`moddifications register`")
                                                                                                                st.tickUpdate()
                                                                                                                attack_embed = tf.getEmbedAttackRole(ctx ,results,char_name,target_name,display_character,target,last_life)
                                                                                                                await ctx.send(embed=attack_embed)
                                                                                                                if results[0] == True:
                                                                                                                        my_buttons = [create_button(style=ButtonStyle.green,
                                                                                                                                                    label="description of the skill",
                                                                                                                                                    custom_id="description"),
                                                                                                                                      create_button(style=ButtonStyle.green,
                                                                                                                                                    label="show buff",
                                                                                                                                                    custom_id="show buff"),
                                                                                                                                      create_button(style=ButtonStyle.blue,
                                                                                                                                                    label="cancel the attack",
                                                                                                                                                    custom_id="undo")]
                                                                                                                        button_raw = create_actionrow(*my_buttons)
                                                                                                                        fait_choix = await ctx.send("`Push for show : `", components=[button_raw])
                                                                                                                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                                                                                                        if button_ctx.custom_id == "description":
                                                                                                                                await button_ctx.edit_origin(content=nonetxt)
                                                                                                                                descr_embed = tf.getEmbedAttacDescription(ctx,display_character.inventory[item_name].competence)
                                                                                                                                await ctx.send(embed=descr_embed)
                                                                                                                        if button_ctx.custom_id == "show buff":
                                                                                                                                await button_ctx.edit_origin(content=nonetxt)
                                                                                                                                buffs_embed = tf.getEmbedAttackBuff(ctx,display_character.inventory[item_name].competence,results)
                                                                                                                                await ctx.send(embed=buffs_embed)
                                                                                                                        if button_ctx.custom_id == "undo":
                                                                                                                                await button_ctx.edit_origin(content=nonetxt)
                                                                                                                                target.life = (sktr.getTheAbsoluteZero(target.life[0] + results[1]),target.life[1])
                                                                                                                                
                                                                                                                                st.saveCharacter(display_character,user_name,display_name)
                                                                                                                                await ctx.send("`moddifications register`")
                                                                                                                                st.saveCharacter(target,my_target_path[0],my_target_path[1])
                                                                                                                                await ctx.send("`moddifications register`")
                                                                                                                else:
                                                                                                                        my_buttons = [create_button(style=ButtonStyle.blue,
                                                                                                                                                    label="description of the skill",
                                                                                                                                                    custom_id="description"),
                                                                                                                                      create_button(style=ButtonStyle.blue,
                                                                                                                                                    label="show buff",
                                                                                                                                                    custom_id="show buff")]
                                                                                                                        button_raw = create_actionrow(*my_buttons)
                                                                                                                        fait_choix = await ctx.send("`Push for show : `", components=[button_raw])
                                                                                                                        button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                                                                                                        if button_ctx.custom_id == "description":
                                                                                                                                await button_ctx.edit_origin(content=nonetxt)
                                                                                                                                descr_embed = tf.getEmbedAttacDescription(ctx,display_character.inventory[item_name].competence)
                                                                                                                                await ctx.send(embed=descr_embed)
                                                                                                                        if button_ctx.custom_id == "show buff":
                                                                                                                                await button_ctx.edit_origin(content=nonetxt)
                                                                                                                                buffs_embed = tf.getEmbedAttackBuff(ctx,display_character.inventory[item_name].competence,results)
                                                                                                                                await ctx.send(embed=buffs_embed)
                                                                                if button_ctx.custom_id == "competence":
                                                                                        await button_ctx.edit_origin(content="`||use as a Competence||`")
                                                                                        display_character.state = (display_character.inventory[item_name].competence.state[0],display_character.inventory[item_name].competence.state[1],st.getTick())
                                                                                        if isinstance(display_character.inventory[item_name],rp.MagicalItemClass):
                                                                                                display_character.inventory[item_name].competence.last_utilisation = st.getTick()
                                                                                        if display_character.inventory[item_name].competence.type[1] == "self_buff":
                                                                                                display_character.buffs.append(rp.BuffClass(display_character.inventory[item_name].competence.state[1],display_character.inventory[item_name].competence.self_buff))
                                                                                        st.saveCharacter(display_character,user_name,display_name)
                                                                                        st.tickUpdate()
                                                                                        await ctx.send("`competence utilisée`")

                                                                                        
                                                                                
                                                                                pass
                                                                        elif display_character.inventory[item_name].competence.type[0] in ["massiv_skill"]:
                                                                                await competence_aux.send(nonetxt)
                                                                                my_buttons = [create_button(style=ButtonStyle.blue,
                                                                                                            label="display the character list",
                                                                                                            custom_id="display"),
                                                                                              create_button(style=ButtonStyle.blue,
                                                                                                            label="dont display the character list",
                                                                                                            custom_id="not display")]
                                                                                button_raw = create_actionrow(*my_buttons)
                                                                                fait_choix = await ctx.send("`Push for display the character list : `", components=[button_raw])
                                                                                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                                                                if button_ctx.custom_id == "display":
                                                                                        await button_ctx.edit_origin(content=nonetxt)
                                                                                        character_dict = st.getCharactersDict()
                                                                                        txt = tf.getPlayerArchitectureChar(character_dict)
                                                                                        my_embed_list = tf.getEmbedCharacterDict(ctx ,character_dict)
                                                                                        for my_embed in my_embed_list:
                                                                                                await ctx.send(embed=my_embed)
                                                                                        await ctx.send("`__enter the names of your targets : __`")
                                                                                        await ctx.send("`target1|target2|target3|target4........`")
                                                                                        try:
                                                                                                target_names_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                                                                                target_names = str(target_names_input.content)
                                                                                        except:
                                                                                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                                                                target_names = "none"
                                                                                        if target_names != "none":
                                                                                                targets_list = target_names.split("|")
                                                                                                selection_target = []
                                                                                                new_target_path_list = []
                                                                                                for target_name in targets_list:
                                                                                                        target_path_list = st.getCharactersPaths(target_name)
                                                                                                        new_target_path_list = new_target_path_list + target_path_list
                                                                                                        selection = []
                                                                                                        for target_path in target_path_list:
                                                                                                                selection_aux = target_path.split("|")
                                                                                                                selection.append(selection_aux[1] + "(" + target_name + ")")
                                                                                                        selection_target = selection_target + selection
                                                                                                if (display_character.inventory[item_name].competence.level <= 14) and (display_character.level <= 14):
                                                                                                        if len(selection_target) < 3:
                                                                                                                targets_selection = tf.getListSelection(ctx,"chose the targets",selection_target,new_target_path_list,1,len(selection_target))
                                                                                                                fait_choix = await ctx.send("`Chose the targets : `", components=[create_actionrow(targets_selection)])
                                                                                                                targets_list_path = await wait_for_component(notlolabot.bot, components=targets_selection, check=check)
                                                                                                                await targets_list_path.send(nonetxt)
                                                                                                                pass
                                                                                                        else:
                                                                                                                targets_selection = tf.getListSelection(ctx,"chose the targets",selection_target,new_target_path_list,1,3)
                                                                                                                fait_choix = await ctx.send("`Chose the targets : `", components=[create_actionrow(targets_selection)])
                                                                                                                targets_list_path = await wait_for_component(notlolabot.bot, components=targets_selection, check=check)
                                                                                                                await targets_list_path.send(nonetxt)
                                                                                                else:
                                                                                                        if len(selection_target) < 8:
                                                                                                                targets_selection = tf.getListSelection(ctx,"chose the targets",selection_target,new_target_path_list,1,len(selection_target))
                                                                                                                fait_choix = await ctx.send("`Chose the targets : `", components=[create_actionrow(targets_selection)])
                                                                                                                targets_list_path = await wait_for_component(notlolabot.bot, components=targets_selection, check=check)
                                                                                                                await targets_list_path.send(nonetxt)
                                                                                                                pass
                                                                                                        else:
                                                                                                                targets_selection = tf.getListSelection(ctx,"chose the targets",selection_target,new_target_path_list,1,8)
                                                                                                                fait_choix = await ctx.send("`Chose the targets : `", components=[create_actionrow(targets_selection)])
                                                                                                                targets_list_path = await wait_for_component(notlolabot.bot, components=targets_selection, check=check)
                                                                                                                await targets_list_path.send(nonetxt)
                                                                                                        pass
                                                                                                if targets_list_path.values != []:
                                                                                                        if isinstance(display_character.inventory[item_name],rp.MagicalItemClass):
                                                                                                                display_character.inventory[item_name].competence.last_utilisation = st.getTick()
                                                                                                        st.saveCharacter(display_character,user_name,display_name)
                                                                                                        for k in range(len(targets_list_path.values)):
                                                                                                                my_target_path = targets_list_path.values[k].split("|")
                                                                                                                target = st.loadCharacter(my_target_path[0],my_target_path[1],my_target_path[2])
                                                                                                                target.buffs.append(rp.BuffClass(display_character.inventory[item_name].competence.state[1],display_character.inventory[item_name].competence.buff))
                                                                                                                st.saveCharacter(target,my_target_path[0],my_target_path[1])
                                                                                                                await ctx.send("buffs add")
                                                                                                        pass
                                                                                if button_ctx.custom_id == "not display":
                                                                                        await button_ctx.edit_origin(content=nonetxt)
                                                                                        await ctx.send("`__enter the names of your targets : __`")
                                                                                        await ctx.send("`target1|target2|target3|target4........`")
                                                                                        try:
                                                                                                target_names_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                                                                                target_names = str(target_names_input.content)
                                                                                        except:
                                                                                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                                                                target_names = "none"
                                                                                        if target_names != "none":
                                                                                                targets_list = target_names.split("|")
                                                                                                selection_target = []
                                                                                                new_target_path_list = []
                                                                                                for target_name in targets_list:
                                                                                                        target_path_list = st.getCharactersPaths(target_name)
                                                                                                        new_target_path_list = new_target_path_list + target_path_list
                                                                                                        selection = []
                                                                                                        for target_path in target_path_list:
                                                                                                                selection_aux = target_path.split("|")
                                                                                                                selection.append(selection_aux[1] + "(" + target_name + ")")
                                                                                                        selection_target = selection_target + selection
                                                                                                if (display_character.inventory[item_name].competence.level <= 14) and (display_character.level <= 14):
                                                                                                        if len(selection_target) < 3:
                                                                                                                targets_selection = tf.getListSelection(ctx,"chose the targets",selection_target,new_target_path_list,1,len(selection_target))
                                                                                                                fait_choix = await ctx.send("`Chose the targets : `", components=[create_actionrow(targets_selection)])
                                                                                                                targets_list_path = await wait_for_component(notlolabot.bot, components=targets_selection, check=check)
                                                                                                                await targets_list_path.send(nonetxt)
                                                                                                                pass
                                                                                                        else:
                                                                                                                targets_selection = tf.getListSelection(ctx,"chose the targets",selection_target,new_target_path_list,1,3)
                                                                                                                fait_choix = await ctx.send("`Chose the targets : `", components=[create_actionrow(targets_selection)])
                                                                                                                targets_list_path = await wait_for_component(notlolabot.bot, components=targets_selection, check=check)
                                                                                                                await targets_list_path.send(nonetxt)
                                                                                                else:
                                                                                                        if len(selection_target) < 8:
                                                                                                                targets_selection = tf.getListSelection(ctx,"chose the targets",selection_target,new_target_path_list,1,len(selection_target))
                                                                                                                fait_choix = await ctx.send("`Chose the targets : `", components=[create_actionrow(targets_selection)])
                                                                                                                targets_list_path = await wait_for_component(notlolabot.bot, components=targets_selection, check=check)
                                                                                                                await targets_list_path.send(nonetxt)
                                                                                                                pass
                                                                                                        else:
                                                                                                                targets_selection = tf.getListSelection(ctx,"chose the targets",selection_target,new_target_path_list,1,8)
                                                                                                                fait_choix = await ctx.send("`Chose the targets : `", components=[create_actionrow(targets_selection)])
                                                                                                                targets_list_path = await wait_for_component(notlolabot.bot, components=targets_selection, check=check)
                                                                                                                await targets_list_path.send(nonetxt)
                                                                                                        pass
                                                                                                if targets_list_path.values != []:
                                                                                                        if isinstance(display_character.inventory[item_name],rp.MagicalItemClass):
                                                                                                                display_character.inventory[item_name].competence.last_utilisation = st.getTick()
                                                                                                        st.saveCharacter(display_character,user_name,display_name)
                                                                                                        for k in range(len(targets_list_path.values)):
                                                                                                                my_target_path = targets_list_path.values[k].split("|")
                                                                                                                target = st.loadCharacter(my_target_path[0],my_target_path[1],my_target_path[2])
                                                                                                                target.buffs.append(rp.BuffClass(display_character.inventory[item_name].competence.state[1],display_character.inventory[item_name].competence.buff))
                                                                                                                st.saveCharacter(target,my_target_path[0],my_target_path[1])
                                                                                                                await ctx.send("buffs add")
                                                                                                        pass
                                                                        else:
                                                                                await competence_aux.send(nonetxt)
                                                                                display_character.state = (display_character.inventory[item_name].competence.state[0],display_character.inventory[item_name].competence.state[1],st.getTick())
                                                                                if isinstance(display_character.inventory[item_name],rp.MagicalItemClass):
                                                                                        display_character.inventory[item_name].competence.last_utilisation = st.getTick()
                                                                                if display_character.competences[competence_name].type[1] == "self_buff":
                                                                                        display_character.buffs.append(rp.BuffClass(display_character.inventory[item_name].competence.state[1],display_character.inventory[item_name].competence.self_buff))
                                                                                st.saveCharacter(display_character,user_name,display_name)
                                                                                st.tickUpdate()
                                                                                await ctx.send("`competence utilisée`")
                                                                if isinstance(display_character.inventory[item_name],rp.MagicalConsumableClass):
                                                                        if display_character.inventory[item_name].quantity > 0:
                                                                                display_character.inventory[item_name].quantity = display_character.inventory[item_name].quantity - 1
                                                                                if display_character.life[0] + display_character.inventory[item_name].life > display_character.life[1]:
                                                                                        display_character.life = (display_character.life[1],display_character.life[1])
                                                                                else:
                                                                                        display_character.life = (display_character.life[0] + display_character.inventory[item_name].life,display_character.life[1])
                                                                                st.saveCharacter(display_character,user_name,display_name)
                                                                                await ctx.send("`" + item_name + "` : **used**.")
                                                                        if display_character.inventory[item_name].quantity == 1:
                                                                                del display_character.inventory[item_name]
                                                                                if display_character.life[0] + display_character.inventory[item_name].life > display_character.life[1]:
                                                                                        display_character.life = (display_character.life[1],display_character.life[1])
                                                                                else:
                                                                                        display_character.life = (display_character.life[0] + display_character.inventory[item_name].life,display_character.life[1])
                                                                                st.saveCharacter(display_character,user_name,display_name)
                                                                                await ctx.send("`" + item_name + "` : **used**.")
                                                                        else:
                                                                                await ctx.send("`" + item_name + "` : **can't be used**.")
                                                        else:
                                                                await ctx.send("`item sans effets`")



                                                else:
                                                        await ctx.send("`item introuvable!`")
                                if button_ctx.custom_id == "left the display":
                                        await button_ctx.edit_origin(content=nonetxt)
                        if button_ctx.custom_id == "not display":
                                my_buttons = [create_button(style=ButtonStyle.blue,
                                                            label="use a item",
                                                            custom_id="use a item"),
                                              create_button(style=ButtonStyle.blue,
                                                            label="left the display",
                                                            custom_id="left the display")]
                                button_raw = create_actionrow(*my_buttons)
                                fait_choix = await ctx.send("`Push the button for display or change a option : `", components=[button_raw])
                                button_ctx = await wait_for_component(notlolabot.bot, components=button_raw, check=check)
                                if button_ctx.custom_id == "use a item":
                                        await button_ctx.edit_origin(content=nonetxt)
                                        await ctx.send("`__enter the name of the consummable to use__`")
                                        try:
                                                item_name_input = await notlolabot.bot.wait_for("message", timeout = 280, check=checkMessage)
                                                item_name = str(item_name_input.content)
                                        except:
                                                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                                                item_name = "none"
                                        if item_name != "none":
                                                if display_character.inventory[item_name].quantity > 0:
                                                        display_character.inventory[item_name].quantity = display_character.inventory[item_name].quantity - 1
                                                        if display_character.life[0] + display_character.inventory[item_name].life > display_character.life[1]:
                                                                display_character.life = (display_character.life[1],display_character.life[1])
                                                        else:
                                                                display_character.life = (display_character.life[0] + display_character.inventory[item_name].life,display_character.life[1])
                                                        st.saveCharacter(display_character,user_name,display_name)
                                                        st.tickUpdate()
                                                        await ctx.send("`" + item_name + "` : **used**.")
                                                else:
                                                        await ctx.send("`" + item_name + "` : **can't be used**.")
                                if button_ctx.custom_id == "left the display":
                                        await button_ctx.edit_origin(content=nonetxt)
        else:
                await ctx.send("`Personnage non enregistrer!`")
@notlolabot.bot.command()
async def characters(ctx):
        """characters command for display the character list"""
        character_dict = st.getCharactersDict()
        txt = tf.getPlayerArchitectureChar(character_dict)
        my_embed_list = tf.getEmbedCharacterDict(ctx ,character_dict)
        for my_embed in my_embed_list:
                await ctx.send(embed=my_embed)
@notlolabot.bot.command()
async def reset(ctx):
        """reset command for the tick system to 0"""
        st.tickReset()








key = ""
notlolabot.bot.run(key)
