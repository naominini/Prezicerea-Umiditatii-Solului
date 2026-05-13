import cdsapi

c = cdsapi.Client()

c.retrieve(
    'reanalysis-era5-land',
    {
        'variable': [
            '2m_temperature',
            'total_precipitation',
            'volumetric_soil_water_layer_1',
            'soil_temperature_level_1',
        ],
        'year': ['2022'],
        'month': [
            '01','02','03','04','05','06',
            '07','08','09','10','11','12'
        ],
        'day': [
            '01','02','03','04','05','06','07','08','09','10',
            '11','12','13','14','15','16','17','18','19','20',
            '21','22','23','24','25','26','27','28','29','30','31'
        ],
        'time': ['00:00', '06:00', '12:00', '18:00'],
        'area': [38.23, 45.05, 37.12, 45.80],
        'format': 'netcdf'
    },
    'Dataset/soil_data.nc')