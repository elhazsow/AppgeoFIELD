from bokeh.models import ColumnDataSource,BoxZoomTool, SaveTool, ResetTool
from bokeh.embed import components
from bokeh.plotting import figure



def bokeh_chart(data, zone, label):
    dates = data['dates']
    ndvi = data['ndvi']
    title = f"{zone.nom}"
    label = f"{label}"
    fig = figure(title= title, height = 300, width=300, x_axis_type = "datetime",tools = [BoxZoomTool(), SaveTool(), ResetTool()])
    fig.line(dates, ndvi, legend_label= label, line_width = 2, color = "green")
    
     ###### fig config
    fig.sizing_mode = "scale_width"
    fig.background_fill_color = "beige"
    fig.background_fill_alpha = 0.2
    fig.border_fill_alpha = 0.0
    fig.toolbar.logo = None
    fig.toolbar.autohide = True
    
    #####fig title

    fig.title.text_color = "white"
    fig.title.text_font = "times"
    fig.title.text_font_style = "bold"
    fig.title.text_font_size = "1rem"
    fig.title.align = "center"
    
     ###########legend######################
    
    # fig.legend.title = 'Stock'
    # fig.legend.title_text_font_style = "bold"
    # fig.legend.title_text_font_size = "20px"
    # fig.legend.title="NVDI"
    fig.legend.location = "top_right"
    fig.legend.background_fill_color = "black"
    fig.legend.background_fill_alpha = 0.1
    fig.legend.border_line_width = 0
    fig.legend.label_text_color="#e6e6ef"
    fig.legend.label_text_font_size = "10px"
    fig.legend.click_policy="hide"
    
    ######### change just some things about the x-grid
    fig.xgrid.grid_line_color = None
    # fig.xgrid.grid_line_alpha = 0.1
    
    ########## change just some things about the y-grid
    # fig.ygrid.grid_line_color = None
    fig.ygrid.grid_line_alpha = 0.1
    
    ########change just some things about the x-axis
    fig.xaxis.axis_label = "Dates"
    fig.xaxis.axis_line_width = 1
    fig.xaxis.axis_line_color = "white"
    fig.xaxis.major_label_text_color = "white"
    # fig.yaxis.major_label_orientation = math.pi/4
    fig.xaxis.axis_label_text_color = "white"

    ########### change just some things about the y-axis
    fig.yaxis.axis_label = "NDVI"
    fig.yaxis.major_label_text_color = "white"
    fig.yaxis.axis_line_color = "white"
    fig.yaxis.axis_label_text_color = "white"
    
    ######### change things on all axes
    fig.axis.minor_tick_in = -3
    fig.axis.minor_tick_out = 6
    
    ######### embed the figure
    script, div = components(fig)
    
    return {'script':script, 'div':div}




