from rasterio.rio.overview import get_maximum_overview_level
from rasterio.io import MemoryFile
from rasterio.enums import Resampling as ResamplingEnums
import click
from rasterio.vrt import WarpedVRT
    
def create_overvews_from_gtiff(geotiff, tilesize=256, overview_resampling = "nearest"):
    overview_level = get_maximum_overview_level(
        geotiff.width, geotiff.height, minsize=tilesize
    )
    overviews = [2**j for j in range(1, overview_level + 1)]
    tmpfile = MemoryFile()
    tmp_dst = tmpfile.open(**geotiff.meta)

    wind = list(tmp_dst.block_windows(1))
    src_dst = geotiff

    vrt_params = {
        "add_alpha": True,
        "dtype": src_dst.dtypes[0],
        "width": src_dst.width,
        "height": src_dst.height,
        "resampling": ResamplingEnums[overview_resampling],
    }

    with WarpedVRT(src_dst, **vrt_params) as vrt_dst:
        with click.progressbar(wind, show_percent=True) as windows:  # type: ignore
            for _, w in windows:
                matrix = vrt_dst.read(window=w, indexes=src_dst.indexes)
                tmp_dst.write(matrix, window=w)
    tmp_dst.build_overviews(overviews, ResamplingEnums[overview_resampling])
    tmp_dst.close()
    return tmp_dst.name
