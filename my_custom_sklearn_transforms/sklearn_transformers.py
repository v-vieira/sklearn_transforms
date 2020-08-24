from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')

# Substituir as notas que são maior que 10 por 10
class Subs_zeros_lim10():
    def __init__(self,columns_norm):
        self.columns_norm = columns_norm
        
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        for col in self.columns_norm:
            select_col = data[col]
            mask = select_col != 0
            mean_no_zeros = float(select_col[mask].min())
            data[col] = select_col.replace(0,mean_no_zeros)
        data['NOTA_GO'].values[data['NOTA_GO'] > 10] = 10
        return data
    
# Criação das colunas de média em humanas e média em exatas
class somas():
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        #criação das medias
        data['REP_HUM'] = data['REPROVACOES_DE'] + data['REPROVACOES_EM']
        data['REP_EXA'] = data['REPROVACOES_MF'] + data['REPROVACOES_GO']
        return data
