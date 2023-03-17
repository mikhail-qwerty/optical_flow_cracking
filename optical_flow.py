import opticalflow3D
import tifffile as tiff
import numpy as np

farneback = opticalflow3D.Farneback3D(iters=7,
                                      num_levels=1,
                                      scale=1,
                                      spatial_size=9,
                                      presmoothing=None,
                                      filter_type="box",
                                      filter_size=21,
                                     )

im_start = tiff.imread('/home/m_fokin/Xray_data/2022-10-sandstone/data_rec/streamrec3d/loading3_stream_5MP_0659/step_10/rec_40600_40779.tiff')
im_end = tiff.imread('/home/m_fokin/Xray_data/2022-10-sandstone/data_rec/streamrec3d/loading3_stream_5MP_0659/step_10/rec_40950_40959.tiff')

output_vz, output_vy, output_vx, output_confidence = farneback.calculate_flow(im_start, im_end, 
                                                                              start_point=(0, 0, 0), # стартовая точка
                                                                              total_vol=(300, 1024, 1024), # зависит от размера im_start и im_end,
                                                                              sub_volume=(150, 512, 512), # пропорционально total volume.
                                                                              overlap=(50, 64, 64), # подбирается под total_vol и sub_volume
                                                                              threadsperblock=(8, 8, 8),
                                                                             )


field = np.sqrt(output_vz**2 + output_vy**2 + output_vx**2)
# сохранение x,y,z компонент
#tiff.imwrite("/home/m_fokin/scripts/2022-10_sandstone/optical_flow/vz.tiff",output_vz.astype(np.float32))
#tiff.imwrite("/home/m_fokin/scripts/2022-10_sandstone/optical_flow/vy.tiff",output_vy.astype(np.float32))
#tiff.imwrite("/home/m_fokin/scripts/2022-10_sandstone/optical_flow/vx.tiff",output_vx.astype(np.float32))
# сохранение абсолютного значения
tiff.imwrite("/home/m_fokin/scripts/2022-10_sandstone/optical_flow/field.tiff",field .astype(np.float32))