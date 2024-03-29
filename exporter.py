#!/usr/bin/env python3

############################################################################
#
# MODULE:       Actinia exporter
#
# AUTHOR(S):    Soeren Gebbert
#
# Original source: https://github.com/mundialis/actinia_core/blob/master/scripts/exporter/
#
# PURPOSE:      Facilitates creation of raster MASK
#
# COPYRIGHT:    (C) 2018-2019 by Sören Gebbert and mundialis GmbH & Co. KG
#
#               This program is free software under the GNU General Public
#               License (>=v3). Read the file COPYING that comes with GRASS
#               for details.
#
#############################################################################

#%module
#% description: Actinia exporter module supporting raster and vector data.
#% keyword: actinia
#% keyword: export
#% keyword: raster
#% keyword: vector
#% overwrite: no
#%end
#%option G_OPT_R_OUTPUT
#% key: raster
#% description: Name of raster map to be exported by actinia
#% required: NO
#% guisection: Raster
#%end
#%option G_OPT_V_OUTPUT
#% key: vector
#% label: Name of vector map to be exported by actinia
#% required: NO
#% guisection: Vector
#%end

import os
import grass.script as grass

# i18N
import gettext
gettext.install('grassmods', os.path.join(os.getenv("GISBASE"), 'locale'))


def main():
    raster = options['raster']
    vector = options['vector']


if __name__ == "__main__":
    options, flags = grass.parser()
    main()
