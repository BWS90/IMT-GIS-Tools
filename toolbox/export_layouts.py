import arcpy
from pathlib import Path

__version__ = '2022-03-11'


class ExportLayouts:
    def __init__(self) -> None:
        self.label = 'Export All Project Layouts'
        self.description = 'Export all layouts in project'
        self.canRunInBackground = True
        self.category = 'Products' # Use your own category here, or an existing one.
        #self.stylesheet = '' # I don't know how to use this yet.
    

    def getParameterInfo(self):
        # Define parameter definitions.
        # Refer to https://pro.arcgis.com/en/pro-app/latest/arcpy/geoprocessing_and_python/defining-parameters-in-a-python-toolbox.htm

        
        # Todo: Select layouts to export
        layouts = arcpy.Parameter(
            name='Output Directory',
            displayName='Output Directory',
            datatype='DEFolder',
            parameterType='Required',
            direction='Input'
        )

        return [layouts]

   
    def execute(self, parameters, messages):
        # The source code of your tool.
        # Get the parameters from our parameters list, then call a generic python function.
        # This separates the code doing the work from all the crazy code required to talk to ArcGIS.

        messages.AddMessage(f'Running {self.label} version {__version__}')

        for param in parameters:
            messages.addMessage(f'Parameter: {param.name} = {param.valueAsText}')

        out_path = Path(parameters[0].valueAsText).resolve()
        
        export_layouts(messages, out_path)
        
        

        # Todo: Add try/catch to catch cancellations and errors when cleanup is required.

        return


def export_layouts(messages, out_path):
    # Todo: Requires product naming IAW SOP
    messages.addMessage(f'Exporting layouts to {out_path}')
    aprx = arcpy.mp.ArcGISProject("CURRENT")

    for layout in aprx.listLayouts():
        messages.addMessage(f'Exporting {layout.name}')
        layout.exportToPDF(out_path.joinpath(f'{layout.name}.pdf'))
    return