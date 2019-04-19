from params import MAIN_PARAMS, AGENT_PARAMS, TANK_DIST

MAIN_PARAMS["RENDER"] = True
MAIN_PARAMS["LIVE_REWARD_PLOT"] = False

AGENT_PARAMS["EPSILON"] = [0] * 6
AGENT_PARAMS["SAVE_MODEL"] = [False] * 6
AGENT_PARAMS["LOAD_MODEL"] = [True] * 6
AGENT_PARAMS["TRAIN_MODEL"] = [False] * 6
AGENT_PARAMS["MODEL_NAME"] = ["Network_[5, 5]HL"] * 6
AGENT_PARAMS["Z_VARIANCE"] = [0] * 6


TANK_DIST[0]["pre_def_dist"] = True
