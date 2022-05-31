import requests
import pandas as pd
from bs4 import BeautifulSoup
import requests_toolbelt
import seaborn as sb
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from math import pi

"""
Each function, with the exception of the last, retreives data from each table for Premier League teams.
To gather data from other leagues, table id values may need to be identified and replaced.
The data will be saved to a folder called 'Data' in the project folder.
"""

def get_table(url, season):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    if season == "20-21":
        standard_table = soup.find_all("table", id="results107281_overall")
    else:
        standard_table = soup.find_all("table", id="results111601_overall")
    standard_table = standard_table[0].find_all("tbody")
    standard_table = standard_table[0].find_all("tr")
    if season == "20-21":
        league_df = pd.DataFrame(columns=(
            ['rank', 'team', 'mp', 'w', 'd', 'l', 'g', 'ga', 'gd', 'pts', 'xG', 'xGA', 'xGD', 'xGD_90', 'attendance']))
    else:
        league_df = pd.DataFrame(columns=(['rank', 'team', 'mp', 'w', 'd', 'l', 'g',
                                 'ga', 'gd', 'pts', 'xG', 'xGA', 'xGD', 'xGD_90', 'form', 'attendance']))
    for i in standard_table:
        player = i
        name = [player.find("th").text]
        data_ = player.find_all("td")
        data = []
        for d in data_:
            data.append(d.text)
        data = name + data[:-3]
        df = pd.DataFrame(data)
        df = df.T
        if season == "20-21":
            df.columns = ['rank', 'team', 'mp', 'w', 'd', 'l', 'g', 'ga',
                          'gd', 'pts', 'xG', 'xGA', 'xGD', 'xGD_90', 'attendance']
        else:
            df.columns = ['rank', 'team', 'mp', 'w', 'd', 'l', 'g', 'ga',
                          'gd', 'pts', 'xG', 'xGA', 'xGD', 'xGD_90', 'form', 'attendance']
        league_df = league_df.append(df)
    return league_df

def get_standard(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    standard_table = soup.find_all("table", id="stats_squads_standard_for")
    standard_table = standard_table[0].find_all("tbody")
    standard_table = standard_table[0].find_all("tr")
    player_data_df = pd.DataFrame(columns=(['team', 'players_used', 'age', 'possession', 'mp', 'starts', 'minutes', '90s',
                                'goals', 'assists', 'np-goals', 'pens_scored', 'pens', 'yellows','reds', 'goals_p90',
                                'assists_p90', 'g_a_p90', 'np_goals_90', 'np_g_a_p90', 'xG', 'np_xG', 'xA', 'np_xG_xA',
                                'xG_p90', 'xA_p90', 'xG_xA_p90', 'np_xG_p90', 'np_xG_xA_p90']))
    for i in standard_table:
        player = i
        name = [player.find("th").text]
        data_ = player.find_all("td")
        data = []
        for d in data_:
            data.append(d.text)
        data = name + data
        df = pd.DataFrame(data)
        df = df.T
        df.columns = ['team', 'players_used', 'age', 'possession', 'mp', 'starts', 'minutes', '90s', 'goals', 'assists',
                'np-goals', 'pens_scored', 'pens', 'yellows', 'reds', 'goals_p90', 'assists_p90', 'g_a_p90', 'np_goals_90',
                'np_g_a_p90', 'xG', 'np_xG', 'xA', 'np_xG_xA', 'xG_p90', 'xA_p90', 'xG_xA_p90', 'np_xG_p90', 'np_xG_xA_p90']
        player_data_df = player_data_df.append(df)
    return player_data_df

def get_goalkeepers(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    standard_table = soup.find_all("table", id="stats_squads_keeper_for")
    standard_table = standard_table[0].find_all("tbody")
    standard_table = standard_table[0].find_all("tr")
    goalkeepers_df = pd.DataFrame(columns=(['team', 'players_used', 'mp', 'starts', 'minutes', '90s', 'GA', 'GA_p90', 'SoTA',
                                  'saves', 'save%', 'wins', 'draws', 'losses', 'CS', 'CS%', 'pkA', 'pk_conc', 'pk_saved', 'pk_miss', 'pk_save%']))
    for i in standard_table:
        player = i
        name = [player.find("th").text]
        data_ = player.find_all("td")
        data = []
        for d in data_:
            data.append(d.text)
        data = name + data
        df = pd.DataFrame(data)
        df = df.T
        df.columns = ['team', 'players_used', 'mp', 'starts', 'minutes', '90s', 'GA', 'GA_p90', 'SoTA', 'saves',
                      'save%', 'wins', 'draws', 'losses', 'CS', 'CS%', 'pkA', 'pk_conc', 'pk_saved', 'pk_miss', 'pk_save%']
        goalkeepers_df = goalkeepers_df.append(df)
    return goalkeepers_df

def get_goalkeepers_adv(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    standard_table = soup.find_all("table", id="stats_squads_keeper_adv_for")
    standard_table = standard_table[0].find_all("tbody")
    standard_table = standard_table[0].find_all("tr")
    goalkeepers_df = pd.DataFrame(columns=(['team', 'players_used', '90s', 'GA', 'pkA', 'fkA', 'ckA', 'OG', 'ps_xG', 'ps_xG/SoT', 'ps_xG+/-', 'ps_xG+/-_p90', 'long_pass_cmp', 'long_pass_att', 'long_pass_cmp%',
                                  'pass_att', 'throw_att', 'long_pass%', 'average_pass_len', 'gk_att', 'gk_long%', 'gk_avg_len', 'crosses', 'cross_stopped', 'cross_stop%', 'def_actions_OPA', 'def_actions_OPA_p90', 'def_actions_avgdist_FG']))
    for i in standard_table:
        player = i
        name = [player.find("th").text]
        data_ = player.find_all("td")
        data = []
        for d in data_:
            data.append(d.text)
        data = name + data
        df = pd.DataFrame(data)
        df = df.T
        df.columns = ['team', 'players_used', '90s', 'GA', 'pkA', 'fkA', 'ckA', 'OG', 'ps_xG', 'ps_xG/SoT', 'ps_xG+/-', 'ps_xG+/-_p90', 'long_pass_cmp', 'long_pass_att', 'long_pass_cmp%', 'pass_att',
                      'throw_att', 'long_pass%', 'average_pass_len', 'gk_att', 'gk_long%', 'gk_avg_len', 'crosses', 'cross_stopped', 'cross_stop%', 'def_actions_OPA', 'def_actions_OPA_p90', 'def_actions_avgdist_FG']
        goalkeepers_df = goalkeepers_df.append(df)
    return goalkeepers_df

def get_shooting(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    standard_table = soup.find_all("table", id="stats_squads_shooting_for")
    standard_table = standard_table[0].find_all("tbody")
    standard_table = standard_table[0].find_all("tr")
    shooting_data = pd.DataFrame(columns=(['team', 'players_used', '90s', 'goals', 'shots', 'SoT', 'SoT%', 'shots_p90', 'SoT_p90', 'goals_per_shot',
                                 'goals_per_SoT', 'avg_dist', 'free_kicks_att', 'pk_scored', 'pk_att', 'xG', 'np_xG', 'np_xG_per_shot', 'goals-xG', 'np_goals-xG']))
    for i in standard_table:
        player = i
        name = [player.find("th").text]
        data_ = player.find_all("td")
        data = []
        for d in data_:
            data.append(d.text)
        data = name + data
        df = pd.DataFrame(data)
        df = df.T
        df.columns = ['team', 'players_used', '90s', 'goals', 'shots', 'SoT', 'SoT%', 'shots_p90', 'SoT_p90', 'goals_per_shot',
                      'goals_per_SoT', 'avg_dist', 'free_kicks_att', 'pk_scored', 'pk_att', 'xG', 'np_xG', 'np_xG_per_shot', 'goals-xG', 'np_goals-xG']
        shooting_data = shooting_data.append(df)
    return shooting_data

def get_passing(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    standard_table = soup.find_all("table", id="stats_squads_passing_for")
    standard_table = standard_table[0].find_all("tbody")
    standard_table = standard_table[0].find_all("tr")
    passing_data = pd.DataFrame(columns=(['team', 'players_used', '90s', 'completed', 'attempted', 'completion%', 'total_distance', 'prog_distance', 'short_completed', 'short_attem', 'short_comp%',
                                'med_completed', 'medium_attem', 'medium_comp%', 'long_completed', 'long_attem', 'long_comp%', 'assists', 'xA', 'assists-xA', 'key_passes', 'final_third_pass', 'pen_passes', 'crosses', 'prog_passes']))
    for i in standard_table:
        player = i
        name = [player.find("th").text]
        data_ = player.find_all("td")
        data = []
        for d in data_:
            data.append(d.text)
        data = name + data
        df = pd.DataFrame(data)
        df = df.T
        df.columns = ['team', 'players_used', '90s', 'completed', 'attempted', 'completion%', 'total_distance', 'prog_distance', 'short_completed', 'short_attem', 'short_comp%', 'med_completed',
                      'medium_attem', 'medium_comp%', 'long_completed', 'long_attem', 'long_comp%', 'assists', 'xA', 'assists-xA', 'key_passes', 'final_third_pass', 'pen_passes', 'crosses', 'prog_passes']
        passing_data = passing_data.append(df)
    return passing_data

def get_pass_types(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    standard_table = soup.find_all(
        "table", id="stats_squads_passing_types_for")
    standard_table = standard_table[0].find_all("tbody")
    standard_table = standard_table[0].find_all("tr")
    pass_types_data = pd.DataFrame(columns=(['team', 'players_used', '90s', 'attempted', 'live', 'dead', 'freekick', 'tb', 'pressure', 'switch_pass', 'cross', 'corners', 'ck_inswing',
                                   'ck_outswing', 'ck_straight', 'ground', 'low', 'high', 'left_f', 'right_f', 'head', 'throw_ins', 'other', 'completed', 'offsides', 'oob', 'intercepted', 'blocked']))
    for i in standard_table:
        player = i
        name = [player.find("th").text]
        data_ = player.find_all("td")
        data = []
        for d in data_:
            data.append(d.text)
        data = name + data
        df = pd.DataFrame(data)
        df = df.T
        df.columns = ['team', 'players_used', '90s', 'attempted', 'live', 'dead', 'freekick', 'tb', 'pressure', 'switch_pass', 'cross', 'corners', 'ck_inswing',
                      'ck_outswing', 'ck_straight', 'ground', 'low', 'high', 'left_f', 'right_f', 'head', 'throw_ins', 'other', 'completed', 'offsides', 'oob', 'intercepted', 'blocked']
        pass_types_data = pass_types_data.append(df)
    return pass_types_data

def get_goal_shot_creation(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    standard_table = soup.find_all("table", id="stats_squads_gca_for")
    standard_table = standard_table[0].find_all("tbody")
    standard_table = standard_table[0].find_all("tr")
    goal_shot_creation_data = pd.DataFrame(columns=(['team', 'players_used', '90s', 'shot_cre_acts', 'shot_cre_acts_90', 'live_sca', 'dead_sca', 'dribb_sca',
                                           'shot_sca', 'foul_sca', 'dfa_sca', 'goal_cre_acts', 'goal_cre_acts_90', 'live_gca', 'dead_gca', 'dribb_gca', 'shot_gca', 'foul_gca', 'dfa_gca']))
    for i in standard_table:
        player = i
        name = [player.find("th").text]
        data_ = player.find_all("td")
        data = []
        for d in data_:
            data.append(d.text)
        data = name + data
        df = pd.DataFrame(data)
        df = df.T
        df.columns = ['team', 'players_used', '90s', 'shot_cre_acts', 'shot_cre_acts_90', 'live_sca', 'dead_sca', 'dribb_sca', 'shot_sca',
                      'foul_sca', 'dfa_sca', 'goal_cre_acts', 'goal_cre_acts_90', 'live_gca', 'dead_gca', 'dribb_gca', 'shot_gca', 'foul_gca', 'dfa_gca']
        goal_shot_creation_data = goal_shot_creation_data.append(df)
    return goal_shot_creation_data

def get_defensive_actions(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    standard_table = soup.find_all("table", id="stats_squads_defense_for")
    standard_table = standard_table[0].find_all("tbody")
    standard_table = standard_table[0].find_all("tr")
    defensive_actions_data = pd.DataFrame(columns=(['team', 'players_used', '90s', 'tackles', 'tackles_won', 'tack_def', 'tack_mid', 'tack_att', 'tack_dribblers', 'tack_and_dribb_past', 'tackle_dribb%', 'dribb_past',
                                          'pressures', 'press_succ', 'press_succ%', 'press_def', 'press_mid', 'press_att', 'blocks', 'shots_blocked', 'shots_blocked_target', 'pass_blocked', 'interceptions', 'int_+_tackles', 'clears', 'errors']))
    for i in standard_table:
        player = i
        name = [player.find("th").text]
        data_ = player.find_all("td")
        data = []
        for d in data_:
            data.append(d.text)
        data = name + data
        df = pd.DataFrame(data)
        df = df.T
        df.columns = ['team', 'players_used', '90s', 'tackles', 'tackles_won', 'tack_def', 'tack_mid', 'tack_att', 'tack_dribblers', 'tack_and_dribb_past', 'tackle_dribb%', 'dribb_past', 'pressures',
                      'press_succ', 'press_succ%', 'press_def', 'press_mid', 'press_att', 'blocks', 'shots_blocked', 'shots_blocked_target', 'pass_blocked', 'interceptions', 'int_+_tackles', 'clears', 'errors']
        defensive_actions_data = defensive_actions_data.append(df)
    return defensive_actions_data

def get_possession(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    standard_table = soup.find_all("table", id="stats_squads_possession_for")
    standard_table = standard_table[0].find_all("tbody")
    standard_table = standard_table[0].find_all("tr")
    possession_data = pd.DataFrame(columns=(['team', 'players_used', 'possession', '90s', 'touches', 'touches_def_pen', 'touches_def_3rd', 'touches_mid_3rd', 'touches_att_3rd', 'touches_att_pen', 'live_touches', 'succ_drib', 'attempted_drib', 'succ_drib%',
                                   'players_drib_past', 'megs', 'carries', 'carr_dist', 'carr_prog_dist', 'prog_carries', 'carries_final_third', 'carries_18y', 'control_errors', 'err_after_tckl', 'pass_received_att', 'pass_received_succ', 'pass_received_succ%', 'prog_receives']))
    for i in standard_table:
        player = i
        name = [player.find("th").text]
        data_ = player.find_all("td")
        data = []
        for d in data_:
            data.append(d.text)
        data = name + data
        df = pd.DataFrame(data)
        df = df.T
        df.columns = ['team', 'players_used', 'possession', '90s', 'touches', 'touches_def_pen', 'touches_def_3rd', 'touches_mid_3rd', 'touches_att_3rd', 'touches_att_pen', 'live_touches', 'succ_drib', 'attempted_drib', 'succ_drib%',
                      'players_drib_past', 'megs', 'carries', 'carr_dist', 'carr_prog_dist', 'prog_carries', 'carries_final_third', 'carries_18y', 'control_errors', 'err_after_tckl', 'pass_received_att', 'pass_received_succ', 'pass_received_succ%', 'prog_receives']
        possession_data = possession_data.append(df)
    return possession_data

def get_playtime(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    standard_table = soup.find_all("table", id="stats_squads_playing_time_for")
    standard_table = standard_table[0].find_all("tbody")
    standard_table = standard_table[0].find_all("tr")
    playtime_data = pd.DataFrame(columns=(['team', 'players_used', 'age', 'mp', 'minutes', 'min_per_m', 'min%', '90s', 'starts', 'min_per_start', 'completed', 'subs',
                                 'min_per_sub', 'un_sub', 'ppm', 'goals_while_playing', 'against_while_playing', 'goal_diff', 'goal_diff_90', 'on_xG', 'on_xGA', 'xG_diff', 'xG_diff_90']))
    for i in standard_table:
        player = i
        name = [player.find("th").text]
        data_ = player.find_all("td")
        data = []
        for d in data_:
            data.append(d.text)
        data = name + data
        df = pd.DataFrame(data)
        df = df.T
        df.columns = ['team', 'players_used', 'age', 'mp', 'minutes', 'min_per_m', 'min%', '90s', 'starts', 'min_per_start', 'completed', 'subs', 'min_per_sub',
                      'un_sub', 'ppm', 'goals_while_playing', 'against_while_playing', 'goal_diff', 'goal_diff_90', 'on_xG', 'on_xGA', 'xG_diff', 'xG_diff_90']
        playtime_data = playtime_data.append(df)
    return playtime_data

def get_misc(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    standard_table = soup.find_all("table", id="stats_squads_misc_for")
    standard_table = standard_table[0].find_all("tbody")
    standard_table = standard_table[0].find_all("tr")
    misc_data = pd.DataFrame(columns=(['team', 'players_used', '90s', 'yellows', 'reds', 'sec_yellows', 'fouls', 'fouls_won', 'offsides', 'crosses',
                             'interceptions', 'tackles_won', 'pens_won', 'pens_con', 'og', 'loose_balls_rec', 'aerials_won', 'aerials_lost', 'aerials_won%']))
    for i in standard_table:
        player = i
        name = [player.find("th").text]
        data_ = player.find_all("td")
        data = []
        for d in data_:
            data.append(d.text)
        data = name + data
        df = pd.DataFrame(data)
        df = df.T
        df.columns = ['team', 'players_used', '90s', 'yellows', 'reds', 'sec_yellows', 'fouls', 'fouls_won', 'offsides', 'crosses',
                      'interceptions', 'tackles_won', 'pens_won', 'pens_con', 'og', 'loose_balls_rec', 'aerials_won', 'aerials_lost', 'aerials_won%']
        misc_data = misc_data.append(df)
    return misc_data

def get_team_data(url, season):
    standard_data = get_standard(url)
    standard_data.to_csv(
        r'/Data/'+season+'/PremierLeague/standard_data.csv', index=False)

    table_data = get_table(url, season)
    table_data.to_csv(
        r'/Data/'+season+'/PremierLeague/table_data.csv', index=False)

    goalkeepers = get_goalkeepers(url)
    goalkeepers.to_csv(
        r'/Data/'+season+'/PremierLeague/goalkeepers.csv', index=False)

    goalkeepers_adv = get_goalkeepers_adv(url)
    goalkeepers_adv.to_csv(
        r'/Data/'+season+'/PremierLeague/goalkeepers_adv.csv', index=False)

    shooting_data = get_shooting(url)
    shooting_data.to_csv(
        r'/Data/'+season+'/PremierLeague/shooting_data.csv', index=False)

    passing_data = get_passing(url)
    passing_data.to_csv(
        r'/Data/'+season+'/PremierLeague/passing_data.csv', index=False)

    pass_types_data = get_pass_types(url)
    pass_types_data.to_csv(
        r'/Data/'+season+'/PremierLeague/pass_types_data.csv', index=False)

    goal_shot_creation_data = get_goal_shot_creation(url)
    goal_shot_creation_data.to_csv(
        r'/Data/'+season+'/PremierLeague/goal_shot_creation_data.csv', index=False)

    defensive_actions_data = get_defensive_actions(url)
    defensive_actions_data.to_csv(
        r'/Data/'+season+'/PremierLeague/defensive_actions_data.csv', index=False)

    possession_data = get_possession(url)
    possession_data.to_csv(
        r'/Data/'+season+'/PremierLeague/possession_data.csv', index=False)

    playtime_data = get_playtime(url)
    playtime_data.to_csv(
        r'/Data/'+season+'/PremierLeague/playtime_data.csv', index=False)

    misc_data = get_misc(url)
    misc_data.to_csv(
        r'/Data/'+season+'/PremierLeague/misc_data.csv', index=False)

def get_data(league_url, season):
    get_team_data(league_url, season)

get_data("https://fbref.com/en/comps/9/Premier-League-Stats", "21-22")
