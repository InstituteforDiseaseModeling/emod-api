#/usr/bin/env python

docstring = \
"""
To generate a config.json from a param_overrides.json (or params-of-interest.json):
    python -m emod_api.config.from_overrides </path/to/po.json>

To generate a default config.json based on the schema for a given Eradication binary:
    python -m emod_api.config.from_schema -e </path/to/Eradication.[exe]> ...

To generate a schema.json:
    python -m emod_api.schema.get_schema </path/to/Eradication[.exe]>

To plot an InsetChart.json
    python -m emod_api.legacy.plotAllCharts </path/to/InsetChart.json>

For rest of emod-api documentation, please go to https://github.com/InstituteforDiseaseModeling/emod-api
"""

def main():
    print( docstring )

if __name__ == "__main__":
    main()
