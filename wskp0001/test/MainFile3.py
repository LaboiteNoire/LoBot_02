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
async def say(ctx, *txt):
        """partager la sainte parole du non lola bot"""
        mess = await ctx.channel.history(limit = 1).flatten()
        await mess[0].delete()
        await ctx.send(" ".join(txt))
@notlolabot.bot.command()
async def register(ctx):
        """register command"""
        def check(m):
                return m.author_id == ctx.author.id and m.origin_message.id == fait_choix.id
        def checkMessage(message):
                return message.author == ctx.message.author and ctx.message.channel == message.channel
        register_type_select = tf.getListSelection(ctx,"chose the register",["competence"],["competence"]) 
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


                
                competence_type_select_01 = tf.getListSelection(ctx,"chose the skill type",["competence d'arme","attaque normale","mouvement","competence normale","competence de support","rituel"],["weapon_attack","normal_attack","mouvement_skill","util_skill","massiv_skill","ritual_skill"])
                fait_choix = await register_type.send("`Chose the the skill type : `", components=[create_actionrow(competence_type_select_01)])
                competence_type_aux_01 = await wait_for_component(notlolabot.bot, components=competence_type_select_01, check=check)


                if competence_type_aux_01.values[0] == "massiv_skill":
                        competence_type = (competence_type_aux_01.values[0],"buff")
                if competence_type_aux_01.values[0] == "mouvement_skill" or competence_type_aux_01.values[0] == "ritual_skill":
                        competence_type = (competence_type_aux_01.values[0],"normal")
                if competence_type_aux_01.values[0] == "weapon_attack" or competence_type_aux_01.values[0] == "normal_attack":
                        competence_type_select_02 = tf.getListSelection(ctx,"chose the if the skill have a buff",["self buff","buff for the target","no buff"],["self_buff","buff","normal"])
                        fait_choix = await competence_type_aux_01.send("`chose the if the skill have a buff : `", components=[create_actionrow(competence_type_select_02)])
                        competence_type_aux_02 = await wait_for_component(notlolabot.bot, components=competence_type_select_02, check=check)
                        competence_type = (competence_type_aux_01.values[0],competence_type_aux_02.values[0])
                        await competence_type_aux_02.send(nonetxt)
                if competence_type_aux_01.values[0] == "util_skill":
                        competence_type_select_02 = tf.getListSelection(ctx,"chose the if the skill have a buff",["self buff","no buff"],["self_buff","normal"])
                        fait_choix = await competence_type_aux_01.send("`chose the if the skill have a buff : `", components=[create_actionrow(competence_type_select_02)])
                        competence_type_aux_02 = await wait_for_component(notlolabot.bot, components=competence_type_select_02, check=check)
                        competence_type = (competence_type_aux_01.values[0],competence_type_aux_02.values[0])
                        await competence_type_aux_02.send(nonetxt)


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
                else:
                        competence_state_select_02 = tf.getListSelection(ctx,"chose the duration of the state",[str(x) for x in range(7)],[str(x) for x in range(7)])
                        fait_choix = await competence_level_aux.send("`chose the duration of the state : `", components=[create_actionrow(competence_state_select_02)])
                        competence_state_aux_02 = await wait_for_component(notlolabot.bot, components=competence_state_select_02, check=check)
                        competence_state = (competence_state_01,int(competence_state_aux_02.values[0]))


                competence_cooldown_select = tf.getListSelection(ctx,"chose the duration of the cooldown",[str(x) for x in range(21)],[str(x) for x in range(21)])
                fait_choix = await competence_state_aux_02.send("`chose the duration of the cooldown : `", components=[create_actionrow(competence_cooldown_select)])
                competence_cooldown_aux = await wait_for_component(notlolabot.bot, components=competence_cooldown_select, check=check)
                competence_cooldown = int(competence_cooldown_aux.values[0])

                self_template_constructor = {"strength" : (0,0),"dexterity" : (0,0),"bleeding" : (0,0) ,"posture" : (0,0) ,
                                             "constitution" : (0,0),"evasion" : (0,0),
                                             "intellect" : (0,0),"charisma" : (0,0) ,"wisdom" : (0,0)}
                template_constructor = {"strength" : (0,0),"dexterity" : (0,0),"bleeding" : (0,0) ,"posture" : (0,0) ,
                                        "constitution" : (0,0),"evasion" : (0,0),
                                        "intellect" : (0,0),"charisma" : (0,0) ,"wisdom" : (0,0)}
                if competence_type[1] == "self_buff":
                        sb_attack_dice_select = tf.getListSelection(ctx,"chose the damage dice of the skill",[str(x) for x in range(11)],[str(x) for x in range(11)])
                        fait_choix = await competence_cooldown_aux.send("`chose the damage dice of the skill : `", components=[create_actionrow(sb_attack_dice_select)])
                        sb_attack_dice_aux = await wait_for_component(notlolabot.bot, components=sb_attack_dice_select, check=check)

                        sb_attack_constent_select = tf.getListSelection(ctx,"chose the damage of the skill",[str(x) for x in range(9)],[str(x) for x in range(9)])
                        fait_choix = await sb_attack_dice_aux.send("`chose the damage of the skill : `", components=[create_actionrow(sb_attack_constent_select)])
                        sb_attack_constent_aux = await wait_for_component(notlolabot.bot, components=sb_attack_constent_select, check=check)

                        sb_dexterity_dice_select = tf.getListSelection(ctx,"chose the dexterity dice of the skill",[str(x) for x in range(11)],[str(x) for x in range(11)])
                        fait_choix = await sb_attack_constent_aux.send("`chose the dexterity dice of the skill : `", components=[create_actionrow(sb_dexterity_dice_select)])
                        sb_dexterity_dice_aux = await wait_for_component(notlolabot.bot, components=sb_dexterity_dice_select, check=check)

                        sb_dexterity_constent_select = tf.getListSelection(ctx,"chose the dexterity of the skill",[str(x) for x in range(9)],[str(x) for x in range(9)])
                        fait_choix = await sb_dexterity_dice_aux.send("`chose the dexterity of the skill : `", components=[create_actionrow(sb_dexterity_constent_select)])
                        sb_dexterity_constent_aux = await wait_for_component(notlolabot.bot, components=sb_dexterity_constent_select, check=check)

                        sb_bleeding_dice_select = tf.getListSelection(ctx,"chose the bleeding dice of the skill",[str(x) for x in range(11)],[str(x) for x in range(11)])
                        fait_choix = await sb_dexterity_constent_aux.send("`chose the bleeding dice of the skill : `", components=[create_actionrow(sb_bleeding_dice_select)])
                        sb_bleeding_dice_aux = await wait_for_component(notlolabot.bot, components=sb_bleeding_dice_select, check=check)

                        sb_bleeding_constent_select = tf.getListSelection(ctx,"chose the bleeding of the skill",[str(x) for x in range(9)],[str(x) for x in range(9)])
                        fait_choix = await sb_bleeding_dice_aux.send("`chose the bleeding of the skill : `", components=[create_actionrow(sb_bleeding_constent_select)])
                        sb_bleeding_constent_aux = await wait_for_component(notlolabot.bot, components=sb_bleeding_constent_select, check=check)

                        sb_posture_dice_select = tf.getListSelection(ctx,"chose the posture dice of the skill",[str(x) for x in range(11)],[str(x) for x in range(11)])
                        fait_choix = await sb_bleeding_constent_aux.send("`chose the posture dice of the skill : `", components=[create_actionrow(sb_posture_dice_select)])
                        sb_posture_dice_aux = await wait_for_component(notlolabot.bot, components=sb_posture_dice_select, check=check)

                        sb_posture_constent_select = tf.getListSelection(ctx,"chose the posture of the skill",[str(x) for x in range(9)],[str(x) for x in range(9)])
                        fait_choix = await sb_posture_dice_aux.send("`chose the posture of the skill : `", components=[create_actionrow(sb_posture_constent_select)])
                        sb_posture_constent_aux = await wait_for_component(notlolabot.bot, components=sb_posture_constent_select, check=check)

                        sb_constitution_dice_select = tf.getListSelection(ctx,"chose the constitution dice of the skill",[str(x) for x in range(11)],[str(x) for x in range(11)])
                        fait_choix = await sb_posture_constent_aux.send("`chose the constitution dice of the skill : `", components=[create_actionrow(sb_constitution_dice_select)])
                        sb_constitution_dice_aux = await wait_for_component(notlolabot.bot, components=sb_constitution_dice_select, check=check)

                        sb_constitution_constent_select = tf.getListSelection(ctx,"chose the constitution of the skill",[str(x) for x in range(9)],[str(x) for x in range(9)])
                        fait_choix = await sb_constitution_dice_aux.send("`chose the constitution of the skill : `", components=[create_actionrow(sb_constitution_constent_select)])
                        sb_constitution_constent_aux = await wait_for_component(notlolabot.bot, components=sb_constitution_constent_select, check=check)

                        sb_evasion_dice_select = tf.getListSelection(ctx,"chose the evasion dice of the skill",[str(x) for x in range(11)],[str(x) for x in range(11)])
                        fait_choix = await sb_constitution_constent_aux.send("`chose the evasion dice of the skill : `", components=[create_actionrow(sb_evasion_dice_select)])
                        sb_evasion_dice_aux = await wait_for_component(notlolabot.bot, components=sb_evasion_dice_select, check=check)

                        sb_evasion_constent_select = tf.getListSelection(ctx,"chose the evasion of the skill",[str(x) for x in range(9)],[str(x) for x in range(9)])
                        fait_choix = await sb_evasion_dice_aux.send("`chose the constitution of the skill : `", components=[create_actionrow(sb_evasion_constent_select)])
                        sb_evasion_constent_aux = await wait_for_component(notlolabot.bot, components=sb_evasion_constent_select, check=check)

                        sb_intellect_dice_select = tf.getListSelection(ctx,"chose the intellect dice of the skill",[str(x) for x in range(11)],[str(x) for x in range(11)])
                        fait_choix = await sb_evasion_constent_aux.send("`chose the intellect dice of the skill : `", components=[create_actionrow(sb_intellect_dice_select)])
                        sb_evasion_dice_aux = await wait_for_component(notlolabot.bot, components=sb_evasion_dice_select, check=check)

                        sb_intellect_constent_select = tf.getListSelection(ctx,"chose the intellect of the skill",[str(x) for x in range(9)],[str(x) for x in range(9)])
                        fait_choix = await sb_evasion_dice_aux.send("`chose the intellect of the skill : `", components=[create_actionrow(sb_intellect_constent_select)])
                        sb_intellect_constent_aux = await wait_for_component(notlolabot.bot, components=sb_intellect_constent_select, check=check)

                        sb_charisma_dice_select = tf.getListSelection(ctx,"chose the charisma dice of the skill",[str(x) for x in range(11)],[str(x) for x in range(11)])
                        fait_choix = await sb_intellect_constent_aux.send("`chose the charisma dice of the skill : `", components=[create_actionrow(sb_charisma_dice_select)])
                        sb_charisma_dice_aux = await wait_for_component(notlolabot.bot, components=sb_charisma_dice_select, check=check)

                        sb_charisma_constent_select = tf.getListSelection(ctx,"chose the charisma of the skill",[str(x) for x in range(9)],[str(x) for x in range(9)])
                        fait_choix = await sb_charisma_dice_aux.send("`chose the charisma of the skill : `", components=[create_actionrow(sb_charisma_constent_select)])
                        sb_charisma_constent_aux = await wait_for_component(notlolabot.bot, components=sb_charisma_constent_select, check=check)

                        sb_wisdom_dice_select = tf.getListSelection(ctx,"chose the wisdom dice of the skill",[str(x) for x in range(11)],[str(x) for x in range(11)])
                        fait_choix = await sb_charisma_constent_aux.send("`chose the wisdom dice of the skill : `", components=[create_actionrow(sb_wisdom_dice_select)])
                        sb_wisdom_dice_aux = await wait_for_component(notlolabot.bot, components=sb_wisdom_dice_select, check=check)

                        sb_wisdom_constent_select = tf.getListSelection(ctx,"chose the wisdom of the skill",[str(x) for x in range(9)],[str(x) for x in range(9)])
                        fait_choix = await sb_wisdom_dice_aux.send("`chose the charisma of the skill : `", components=[create_actionrow(sb_wisdom_constent_select)])
                        sb_wisdom_constent_aux = await wait_for_component(notlolabot.bot, components=sb_wisdom_constent_select, check=check)
                        await sb_wisdom_constent_aux.send(nonetxt)
                        
                        self_template_constructor = {"strength" : (int(sb_attack_dice_aux.values[0]),int(sb_attack_dice_aux.values[0])),
                                                     "dexterity" : (int(sb_dexterity_dice_aux.values[0]),int(sb_dexterity_constent_aux.values[0])),
                                                     "bleeding" : (int(sb_bleeding_dice_aux.values[0]),int(sb_bleeding_constent_aux.values[0])) ,
                                                     "posture" : (int(sb_posture_dice_aux.values[0]),int(sb_posture_constent_aux.values[0])) ,
                                                     "constitution" : (int(sb_constitution_dice_aux.values[0]),int(sb_constitution_constent_aux.values[0])),
                                                     "evasion" : (int(sb_evasion_dice_aux.values[0]),int(sb_evasion_constent_aux.values[0])),
                                                     "intellect" : (int(sb_intellect_dice_aux.values[0]),int(sb_intellect_constent_aux.values[0])),
                                                     "charisma" : (int(sb_charisma_dice_aux.values[0]),int(sb_charisma_constent_aux.values[0])) ,
                                                     "wisdom" : (int(sb_wisdom_dice_aux.values[0]),int(sb_wisdom_constent_aux.values[0]))}
                        pass
                if competence_type[1] == "buff":
                        sb_attack_dice_select = tf.getListSelection(ctx,"chose the damage dice of the skill",[str(x) for x in range(11)],[str(x) for x in range(11)])
                        fait_choix = await competence_cooldown_aux.send("`chose the damage dice of the skill : `", components=[create_actionrow(sb_attack_dice_select)])
                        sb_attack_dice_aux = await wait_for_component(notlolabot.bot, components=sb_attack_dice_select, check=check)

                        sb_attack_constent_select = tf.getListSelection(ctx,"chose the damage of the skill",[str(x) for x in range(9)],[str(x) for x in range(9)])
                        fait_choix = await sb_attack_dice_aux.send("`chose the damage of the skill : `", components=[create_actionrow(sb_attack_constent_select)])
                        sb_attack_constent_aux = await wait_for_component(notlolabot.bot, components=sb_attack_constent_select, check=check)

                        sb_dexterity_dice_select = tf.getListSelection(ctx,"chose the dexterity dice of the skill",[str(x) for x in range(11)],[str(x) for x in range(11)])
                        fait_choix = await sb_attack_constent_aux.send("`chose the dexterity dice of the skill : `", components=[create_actionrow(sb_dexterity_dice_select)])
                        sb_dexterity_dice_aux = await wait_for_component(notlolabot.bot, components=sb_dexterity_dice_select, check=check)

                        sb_dexterity_constent_select = tf.getListSelection(ctx,"chose the dexterity of the skill",[str(x) for x in range(9)],[str(x) for x in range(9)])
                        fait_choix = await sb_dexterity_dice_aux.send("`chose the dexterity of the skill : `", components=[create_actionrow(sb_dexterity_constent_select)])
                        sb_dexterity_constent_aux = await wait_for_component(notlolabot.bot, components=sb_dexterity_constent_select, check=check)

                        sb_bleeding_dice_select = tf.getListSelection(ctx,"chose the bleeding dice of the skill",[str(x) for x in range(11)],[str(x) for x in range(11)])
                        fait_choix = await sb_dexterity_constent_aux.send("`chose the bleeding dice of the skill : `", components=[create_actionrow(sb_bleeding_dice_select)])
                        sb_bleeding_dice_aux = await wait_for_component(notlolabot.bot, components=sb_bleeding_dice_select, check=check)

                        sb_bleeding_constent_select = tf.getListSelection(ctx,"chose the bleeding of the skill",[str(x) for x in range(9)],[str(x) for x in range(9)])
                        fait_choix = await sb_bleeding_dice_aux.send("`chose the bleeding of the skill : `", components=[create_actionrow(sb_bleeding_constent_select)])
                        sb_bleeding_constent_aux = await wait_for_component(notlolabot.bot, components=sb_bleeding_constent_select, check=check)

                        sb_posture_dice_select = tf.getListSelection(ctx,"chose the posture dice of the skill",[str(x) for x in range(11)],[str(x) for x in range(11)])
                        fait_choix = await sb_bleeding_constent_aux.send("`chose the posture dice of the skill : `", components=[create_actionrow(sb_posture_dice_select)])
                        sb_posture_dice_aux = await wait_for_component(notlolabot.bot, components=sb_posture_dice_select, check=check)

                        sb_posture_constent_select = tf.getListSelection(ctx,"chose the posture of the skill",[str(x) for x in range(9)],[str(x) for x in range(9)])
                        fait_choix = await sb_posture_dice_aux.send("`chose the posture of the skill : `", components=[create_actionrow(sb_posture_constent_select)])
                        sb_posture_constent_aux = await wait_for_component(notlolabot.bot, components=sb_posture_constent_select, check=check)

                        sb_constitution_dice_select = tf.getListSelection(ctx,"chose the constitution dice of the skill",[str(x) for x in range(11)],[str(x) for x in range(11)])
                        fait_choix = await sb_posture_constent_aux.send("`chose the constitution dice of the skill : `", components=[create_actionrow(sb_constitution_dice_select)])
                        sb_constitution_dice_aux = await wait_for_component(notlolabot.bot, components=sb_constitution_dice_select, check=check)

                        sb_constitution_constent_select = tf.getListSelection(ctx,"chose the constitution of the skill",[str(x) for x in range(9)],[str(x) for x in range(9)])
                        fait_choix = await sb_constitution_dice_aux.send("`chose the constitution of the skill : `", components=[create_actionrow(sb_constitution_constent_select)])
                        sb_constitution_constent_aux = await wait_for_component(notlolabot.bot, components=sb_constitution_constent_select, check=check)

                        sb_evasion_dice_select = tf.getListSelection(ctx,"chose the evasion dice of the skill",[str(x) for x in range(11)],[str(x) for x in range(11)])
                        fait_choix = await sb_constitution_constent_aux.send("`chose the evasion dice of the skill : `", components=[create_actionrow(sb_evasion_dice_select)])
                        sb_evasion_dice_aux = await wait_for_component(notlolabot.bot, components=sb_evasion_dice_select, check=check)

                        sb_evasion_constent_select = tf.getListSelection(ctx,"chose the evasion of the skill",[str(x) for x in range(9)],[str(x) for x in range(9)])
                        fait_choix = await sb_evasion_dice_aux.send("`chose the constitution of the skill : `", components=[create_actionrow(sb_evasion_constent_select)])
                        sb_evasion_constent_aux = await wait_for_component(notlolabot.bot, components=sb_evasion_constent_select, check=check)

                        sb_intellect_dice_select = tf.getListSelection(ctx,"chose the intellect dice of the skill",[str(x) for x in range(11)],[str(x) for x in range(11)])
                        fait_choix = await sb_evasion_constent_aux.send("`chose the intellect dice of the skill : `", components=[create_actionrow(sb_intellect_dice_select)])
                        sb_evasion_dice_aux = await wait_for_component(notlolabot.bot, components=sb_evasion_dice_select, check=check)

                        sb_intellect_constent_select = tf.getListSelection(ctx,"chose the intellect of the skill",[str(x) for x in range(9)],[str(x) for x in range(9)])
                        fait_choix = await sb_evasion_dice_aux.send("`chose the intellect of the skill : `", components=[create_actionrow(sb_intellect_constent_select)])
                        sb_intellect_constent_aux = await wait_for_component(notlolabot.bot, components=sb_intellect_constent_select, check=check)

                        sb_charisma_dice_select = tf.getListSelection(ctx,"chose the charisma dice of the skill",[str(x) for x in range(11)],[str(x) for x in range(11)])
                        fait_choix = await sb_intellect_constent_aux.send("`chose the charisma dice of the skill : `", components=[create_actionrow(sb_charisma_dice_select)])
                        sb_charisma_dice_aux = await wait_for_component(notlolabot.bot, components=sb_charisma_dice_select, check=check)

                        sb_charisma_constent_select = tf.getListSelection(ctx,"chose the charisma of the skill",[str(x) for x in range(9)],[str(x) for x in range(9)])
                        fait_choix = await sb_charisma_dice_aux.send("`chose the charisma of the skill : `", components=[create_actionrow(sb_charisma_constent_select)])
                        sb_charisma_constent_aux = await wait_for_component(notlolabot.bot, components=sb_charisma_constent_select, check=check)

                        sb_wisdom_dice_select = tf.getListSelection(ctx,"chose the wisdom dice of the skill",[str(x) for x in range(11)],[str(x) for x in range(11)])
                        fait_choix = await sb_charisma_constent_aux.send("`chose the wisdom dice of the skill : `", components=[create_actionrow(sb_wisdom_dice_select)])
                        sb_wisdom_dice_aux = await wait_for_component(notlolabot.bot, components=sb_wisdom_dice_select, check=check)

                        sb_wisdom_constent_select = tf.getListSelection(ctx,"chose the wisdom of the skill",[str(x) for x in range(9)],[str(x) for x in range(9)])
                        fait_choix = await sb_wisdom_dice_aux.send("`chose the charisma of the skill : `", components=[create_actionrow(sb_wisdom_constent_select)])
                        sb_wisdom_constent_aux = await wait_for_component(notlolabot.bot, components=sb_wisdom_constent_select, check=check)
                        await sb_wisdom_constent_aux.send(nonetxt)
                        
                        template_constructor = {"strength" : (int(sb_attack_dice_aux.values[0]),int(sb_attack_dice_aux.values[0])),
                                                "dexterity" : (int(sb_dexterity_dice_aux.values[0]),int(sb_dexterity_constent_aux.values[0])),
                                                "bleeding" : (int(sb_bleeding_dice_aux.values[0]),int(sb_bleeding_constent_aux.values[0])) ,
                                                "posture" : (int(sb_posture_dice_aux.values[0]),int(sb_posture_constent_aux.values[0])) ,
                                                "constitution" : (int(sb_constitution_dice_aux.values[0]),int(sb_constitution_constent_aux.values[0])),
                                                "evasion" : (int(sb_evasion_dice_aux.values[0]),int(sb_evasion_constent_aux.values[0])),
                                                "intellect" : (int(sb_intellect_dice_aux.values[0]),int(sb_intellect_constent_aux.values[0])),
                                                "charisma" : (int(sb_charisma_dice_aux.values[0]),int(sb_charisma_constent_aux.values[0])) ,
                                                "wisdom" : (int(sb_wisdom_dice_aux.values[0]),int(sb_wisdom_constent_aux.values[0]))}
                        pass
                if competence_type_aux_01.values[0] == "weapon_attack" or competence_type_aux_01.values[0] == "normal_attack":
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
                        
                        attack_template_constructor = {"strength" : (int(attack_dice_aux.values[0]),int(attack_dice_aux.values[0])),
                                    "dexterity" : (int(dexterity_dice_aux.values[0]),int(dexterity_constent_aux.values[0])),
                                    "bleeding" : (int(bleeding_dice_aux.values[0]),int(bleeding_constent_aux.values[0])) ,
                                    "posture" : (int(posture_dice_aux.values[0]),int(posture_constent_aux.values[0])) ,
                                    "constitution" : (0,0),"evasion" : (0,0),"intellect" : (0,0),"charisma" : (0,0) ,"wisdom" : (0,0)}
                new_competence = rp.CompetenceClass(competence_name,competence_descrition,competence_type,competence_cooldown,competence_state,competence_level,attack_template_constructor,rp.StatisticsClass("self_buff",self_template_constructor),rp.StatisticsClass("buff",template_constructor))
                st.saveCompetence(new_competence)


                display_competence = st.loadCompetence(new_competence.name)
                my_embed = tf.getEmbedImageCompetence(ctx,new_competence.name)
                tf.TypographyCompetenceInterface(ctx,display_competence,my_embed)
                await ctx.send(embed=my_embed)


                







notlolabot.bot.run("MTEzMzA0NzYzMTg0OTk5MjMyNQ.GIM64A.IF16b8ccriPbkJvjWyETL4tAeOJ-53AvsbKqTk")
