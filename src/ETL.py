# Fecha: 08/01/2026
# Autor: Jeffersson Alexander Pretell Velásquez
# Descripción: Módulo ETL para la extracción, transformación y carga de datos. 

import pandas as pd
def extract_data(url = str,extension = str) -> pd.DataFrame:
    """
    Función para extraer datos desde una URL dada y devolver un DataFrame de pandas.

    Parámetros:
    --------------

    url : str
        URL desde donde se extraerán los datos.
    
    extension : str
        Extensión del archivo de datos (por ejemplo, 'csv', 'json','xlsx').
    
    Retorna:
    --------------
    pd.DataFrame
        DataFrame que contiene los datos extraídos.
    """
    import pandas as pd
    import openpyxl

    if extension == 'csv':
        data = pd.read_csv(url)
    elif extension == 'json':
        data = pd.read_json(url)
    elif extension == 'xlsx':
        data = pd.read_excel(url)
    else:
        raise ValueError("Unsupported file extension: {}".format(extension))
    
    return data

def transform_data(data: pd.DataFrame) -> 'pd.DataFrame':

        # Convertir la columna 'dteday' a tipo datetime y establecerla como índice
    data['dteday'] = pd.to_datetime(data['dteday'])
    data.set_index('dteday', inplace=True)

    # Reemplazar valores numéricos por etiquetas descriptivas
    data['yr'].replace({0:'2011', 1:'2012'}, inplace=True)
    data['mnth'].replace({
        1:'Enero', 2:'Febrero', 3:'Marzo', 4:'Abril',
        5:'Mayo', 6:'Junio', 7:'Julio', 8:'Agosto',
        9:'Septiembre', 10:'Octubre', 11:'Noviembre', 12:'Diciembre'
    }, inplace=True)
    data['workingday'].replace({0:'Día_No_Laborable', 1:'Día_Laborable'}, inplace=True)
    data['holiday'].replace({0:'No_Feriado', 1:'Feriado'}, inplace=True)
    data['weekday'].replace({
        0:'Domingo', 1:'Lunes', 2:'Martes', 3:'Miércoles',
        4:'Jueves', 5:'Viernes', 6:'Sábado'
    }, inplace=True)
    data['weathersit'].replace({
        1:'Despejado',
        2:'Niebla_Nublado',
        3:'Lluvia_Nieve_Ligera',
        4:'Lluvia_Nieve_Intensa'
    }, inplace=True)
    data['season'].replace({
        1:'Invierno',
        2:'Primavera',
        3:'Verano',
        4:'Otoño'
    }, inplace=True)

    # Agrupar horas del día
    def hour_group(h):
        if 0 <= h <= 5:
            return 'Madrugada'
        elif 6 <= h <= 11:
            return 'Mañana'
        elif 12 <= h <= 17:
            return 'Tarde'
        else:
            return 'Noche_Tarde'

    data['hr'] = data['hr'].apply(hour_group)

    categorias = data.select_dtypes(include=['object']).columns.to_list()

    data[categorias] = data[categorias].astype('category')

    cat_orders = {
        'season': ['Invierno', 'Primavera', 'Verano', 'Otoño'],
        'yr': ['2011', '2012'],
        'mnth': ['Enero','Febrero','Marzo','Abril','Mayo','Junio',
                'Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'],
        'hr': ['Madrugada', 'Mañana', 'Tarde', 'Noche_Tarde'],  # si quieres otro orden me dices
        'holiday': ['No_Feriado', 'Feriado'],
        'weekday': ['Lunes','Martes','Miércoles','Jueves','Viernes','Sábado','Domingo'],
        'workingday': ['Día_No_Laborable', 'Día_Laborable'],
        'weathersit': ['Despejado', 'Niebla_Nublado', 'Lluvia_Nieve_Ligera', 'Lluvia_Nieve_Intensa']
    }

    # --- APLICAR ORDEN Y CONVERTIR A CATEGORÍA ---
    for col, order in cat_orders.items():
        data[col] = pd.Categorical(data[col], categories=order, ordered=True)

    return data

def load_data(data: pd.DataFrame, path: str,name: str) -> None:
    """
    Función para cargar datos en un archivo CSV.

    Parámetros:
    --------------

    data : pd.DataFrame
        DataFrame que contiene los datos a cargar.
    
    path : str
        Ruta del archivo donde se guardarán los datos.
    
    Retorna:
    --------------
    None
    """
    url = path + name + '.parquet'
    data.to_parquet(url, index=True)

if __name__ == "__main__":

    # Para el conjunto de entrenamiento

    train = extract_data(url='G:\\Mi unidad\\DATA SCIENCE\\PYNTHON\\VSC\\Prediccion_Bicicletas\\data\\raw\\train\\train.csv',extension='csv')
    train = transform_data(data=train)
    load_data(data=train,
              path='G:\\Mi unidad\\DATA SCIENCE\\PYNTHON\\VSC\\Prediccion_Bicicletas\\data\\processed\\train\\',
              name='train_eda')
    
    # Para el conjunto de prueba
    test = extract_data(url='G:\\Mi unidad\\DATA SCIENCE\\PYNTHON\\VSC\\Prediccion_Bicicletas\\data\\raw\\test\\test.csv',extension='csv')
    test = transform_data(data=test)
    load_data(data=test,
              path='G:\\Mi unidad\\DATA SCIENCE\\PYNTHON\\VSC\\Prediccion_Bicicletas\\data\\processed\\test\\',
              name='test_eda')