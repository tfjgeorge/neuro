import pandas

BASEPATH = '/data/lisa/data/neuro/Meditation/graphmetrics/imcoh_source/'

def load_data_graphmetrics():

    data = dict()

    data['alpha'] = pandas.read_csv(BASEPATH + 'alpha_all_infos_by_sorted_cond.csv')
    data['beta'] = pandas.read_csv(BASEPATH + 'beta_all_infos_by_sorted_cond.csv')
    data['delta'] = pandas.read_csv(BASEPATH + 'delta_all_infos_by_sorted_cond.csv')
    data['gamma1'] = pandas.read_csv(BASEPATH + 'gamma1_all_infos_by_sorted_cond.csv')
    data['gamma2'] = pandas.read_csv(BASEPATH + 'gamma2_all_infos_by_sorted_cond.csv')
    data['gamma3'] = pandas.read_csv(BASEPATH + 'gamma3_all_infos_by_sorted_cond.csv')
    data['delta'] = pandas.read_csv(BASEPATH + 'delta_all_infos_by_sorted_cond.csv')
    
    return data
