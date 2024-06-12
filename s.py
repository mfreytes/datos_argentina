from django.db.models import Sum, Avg, Count


from turismo.models import ViajerosResidenciaDestino as V

'''
    indice_tiempo = models.DateField(blank=False)
    region_de_destino = models.CharField(max_length=25, blank=False)
    origen_viajeros = models.CharField(max_length=25, blank=False)
    viajeros = models.IntegerField(default=0)
    observaciones = models.TextField(blank=True)
'''


no_res = V.objects.filter(region_de_destino__contains="rdoba", origen_viajeros='No residentes')
cnt_no_res = V.objects.filter(region_de_destino__contains="rdoba", origen_viajeros='Residentes').count()

res = V.objects.filter(region_de_destino__contains="rdoba", origen_viajeros='Residentes')
cnt_res = V.objects.filter(region_de_destino__contains="rdoba", origen_viajeros='Residentes').count()

sum_v = V.objects.filter(indice_tiempo='2024-03-01', region_de_destino__contains="rdoba", origen_viajeros='Residentes').aggregate(Sum('viajeros'))


#for v in no_res:
#    print(v.indice_tiempo, '\t', v.viajeros)
#print(cnt_no_res)

#for v in s_nr:
#    print(v.indice_tiempo, '\t', v.viajeros__sum)
#print(cnt_res)

#print(sum_v)



""" totales = V.objects.values('indice_tiempo__year', 'region_de_destino').annotate(total_viajeros=Sum('viajeros'))
for total in totales:
    print(f"Fecha: {total['indice_tiempo__year']}, Región: {total['region_de_destino']}, Total de viajeros: {total['total_viajeros']}")
 """

dst_cba = V.objects.filter(region_de_destino="Córdoba").values('indice_tiempo').annotate(total_viajeros=Sum('viajeros'))
dst_otro = V.objects.exclude(region_de_destino="Córdoba").values('indice_tiempo').annotate(total_viajeros=Sum('viajeros'))

dst_cba = V.objects.filter(
    region_de_destino="Córdoba", origen_viajeros='Residentes').values('indice_tiempo', 'origen_viajeros', 'viajeros')
    #.annotate(total_viajeros=Sum('viajeros'))
dst_otro = V.objects.exclude(region_de_destino="Córdoba").exclude(origen_viajeros='No residentes').values('indice_tiempo', 'origen_viajeros', 'viajeros')
    #.annotate(total_viajeros=Sum('viajeros'))

print(dst_cba)
print(dst_otro)


import plotly.express as px
import pandas as pd

# Sample data frame
df = pd.DataFrame({
    'Date': ['2021-01-01', '2021-01-02', '2021-01-03'],
    'Product A': [240, 250, 260],
    'Product B': [220, 230, 245]
})

# print(df)

# Melting the dataframe
df_melted = df.melt(id_vars='Date', var_name='Product', value_name='Sales')
# print(df_melted)

# Creating the line chart
fig = px.line(df_melted, x='Date', y='Sales', color='Product')
# fig.show()
