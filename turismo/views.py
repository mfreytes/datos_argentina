from django.shortcuts import render
from django.db.models import Sum, Avg
import plotly.express as px
import pandas as pd

from turismo.models import ViajerosResidenciaDestino as V


def graficar(request):
    dst_cordoba = V.objects.filter(
        region_de_destino="Córdoba", origen_viajeros='No residentes').values('indice_tiempo').annotate(total_viajeros=Sum('viajeros'))
    dst_bsas = V.objects.filter(
        region_de_destino="Buenos Aires", origen_viajeros='No residentes').values('indice_tiempo').annotate(total_viajeros=Sum('viajeros'))
    dst_caba = V.objects.filter(
        region_de_destino="CABA", origen_viajeros='No residentes').values('indice_tiempo').annotate(total_viajeros=Sum('viajeros'))
    dst_cuyo = V.objects.filter(
        region_de_destino="Cuyo", origen_viajeros='No residentes').values('indice_tiempo').annotate(total_viajeros=Sum('viajeros'))
    dst_arg = V.objects.exclude(
        origen_viajeros='No residentes').values('indice_tiempo').annotate(total_viajeros=Avg('viajeros'))

    print(dst_cordoba.count())

    tiempo = dst_cordoba.values_list('indice_tiempo', flat=True)
    viajeros_cordoba = dst_cordoba.values_list('total_viajeros', flat=True)
    viajeros_bsas = dst_bsas.values_list('total_viajeros', flat=True)
    viajeros_caba = dst_caba.values_list('total_viajeros', flat=True)
    viajeros_cuyo = dst_cuyo.values_list('total_viajeros', flat=True)
    viajeros_arg = dst_arg.values_list('total_viajeros', flat=True)

    print (len(tiempo))
    print(len(viajeros_cordoba))

    df = pd.DataFrame({
        'Fecha': tiempo,
        'Córdoba': viajeros_cordoba,
        'Buenos Aires': viajeros_bsas,
        'CABA': viajeros_caba,
        'Cuyo': viajeros_cuyo,
        'Prom Argentina': viajeros_arg
}   )
    df_melted = df.melt(id_vars='Fecha', var_name='Destino', value_name='Viajeros')
    # Creating the line chart

    print(df, df_melted)
    fig = px.line(df_melted, x='Fecha', y='Viajeros', title='Turismo de no residentes', color='Destino', height=600)

#    fig = px.line(x=tiempo, y=viajeros_cba, title="Turismo en Córdoba")
#    fig.add_traces(x=tiempo, y=viajeros_otro)
    html = fig.to_html()
    context = {'grafico': html}
    return render(request, 'turismo/template.html', context)
