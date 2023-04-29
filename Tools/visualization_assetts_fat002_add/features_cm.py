from Tools.visualization_assetts_fat002_add.config2 import *
from Tools.visualization_assetts_fat002_add.folder_creation import *

#fetch the data from queryset

features_qs = (Queryset("Monthly_update_features_cm", "country_month"))
features_cm=features_qs.fetch()

top10_sb= give_me_topX_country_id_cumulative(df=features_cm, time_index = 'month_id', number_wanted = 10, variable = 'ged_sb_ln1', start = StartOfHistory, end = EndOfHistory, variable_transformation = 'ln1')

top10_ns = give_me_topX_country_id_cumulative(df=features_cm, time_index = 'month_id', number_wanted = 10, variable = 'ged_ns_ln1', start = StartOfHistory, end = EndOfHistory, variable_transformation = 'ln1')

top10_os = give_me_topX_country_id_cumulative(df=features_cm, time_index = 'month_id', number_wanted = 10, variable = 'ged_os_ln1', start = StartOfHistory, end = EndOfHistory, variable_transformation = 'ln1')

features_cm = features_cm.reset_index()
features_cm['top10_sb'] = np.where(features_cm['country_id'].isin(top10_sb), 1,0)
features_cm['top10_ns'] = np.where(features_cm['country_id'].isin(top10_ns), 1,0)
features_cm['top10_os'] = np.where(features_cm['country_id'].isin(top10_os), 1,0)
features_cm = features_cm.set_index(['month_id', 'country_id'])

print(f'{user} cm_current_data fetched successfully')

#obtaining cm level geometries
engine = sa.create_engine(source_db_path)
gdf_ci_master = gpd.GeoDataFrame.from_postgis(
    "SELECT id as country_id, name, in_africa, in_me, geom FROM prod.country",
    engine,
    geom_col='geom'
)
gdf_ci_master = gdf_ci_master.to_crs(4326)
print(f'{user} gdf_ci_master fetched successfully')


def features_cm_level_mapping_ged():
    #cm level features mapping, ged

    #prep data
    data= features_cm.copy()
    gdf = gdf_ci_master.copy()

    data = data.join(gdf.set_index("country_id"))
    gdf = gpd.GeoDataFrame(data, geometry="geom")

    #savefolder
    features_cm_folder = f"{master_folder}/"

    #looping informationa
    variable_loop = variables_wanted_features_cm_ged
    dictionary_run = fatality_dictionary_cm
    cmap_run = fatality_colormap
    steps_loop = months_wanted_features

    for step in steps_loop:
        for variable in variable_loop:
            for region_name in geo_coverage_loop:
                data_run = gdf.loc[step]
                var_run = variable
                var_name_run = find_the_violence_type(variable)
                var_run_savefile = give_me_violence_string_label_only(variable)
                bbox_run = bbox_from_cid_region(region_name)                       

                #making the choice of textbox size
                textbox_font_size = function_for_textbox(region_name)

                title_run = f'{features_ged_title_name} in {str(vid2date(step))}, {var_name_run}'
                textbox = f'Name: features,\n{var_run}_at_{str(step)},\nlast input: {str(vid2date(EndOfHistory))}'
                savefile = f'{features_cm_folder}GED_cm{var_run_savefile}_{region_name}_{cmap_run}_month{step}.png'

                if region_name in ('globe', 'ame', 'africa'):
                    map_run=Mapper2(
                        width=width_global,
                        height=height_global,
                        frame_on=True,
                        title=title_run,
                        bbox=bbox_run
                    ).add_layer(
                        gdf=data_run,
                        map_dictionary=dictionary_run,
                        cmap='binary',
                        edgecolor="black",
                        linewidth=0.5,
                        transparency = 1.0,
                        column=var_run
                    ).add_mask(
                        gdf = data_run,
                        map_dictionary = dictionary_run,
                        cmap = cmap_run,
                        transparency = 1,
                        masking_location = region_name,
                        column=var_run,
                        edgecolor="black",
                        linewidth=1
                    ).add_views_textbox(
                        text=textbox,
                        textsize=textbox_font_size)

                    map_run.save(savefile)
                else:
                    map_run=Mapper2(
                        width=width_global,
                        height=height_global,
                        frame_on=True,
                        title=title_run,
                        bbox=bbox_run
                    ).add_mask(
                        gdf = data_run,
                        map_dictionary = dictionary_run,
                        cmap = cmap_run,
                        transparency = country_mapping_transparency_global,
                        background = country_background_global,
                        masking_location = str(cid2name(region_name)),
                        column=var_run,
                        edgecolor="black",
                        linewidth=1, 
                        views_experimental_labels = views_experimental_font_global
                    ).add_views_textbox(
                        text=textbox,
                        textsize=textbox_font_size)

                    map_run.save(savefile)
    print(f'{user}, cm maps for ged completed')

def features_cm_level_mapping_ged_with_top_10():
    #cm level features mapping, ged

    #prep data
    data= features_cm.copy()
    gdf = gdf_ci_master.copy()

    data = data.join(gdf.set_index("country_id"))
    gdf = gpd.GeoDataFrame(data, geometry="geom")

    #savefolder
    features_cm_folder = f"{master_folder}/"

    #looping informationa
    variable_loop = variables_wanted_features_cm_ged
    dictionary_run = fatality_dictionary_cm
    cmap_run = fatality_colormap
    steps_loop = months_wanted_features    

    for step in steps_loop:
        for variable in variable_loop:
            for region_name in geo_coverage_loop:
                data_run = gdf.loc[step]
                var_run = variable
                var_name_run = find_the_violence_type(variable)
                var_run_savefile = give_me_violence_string_label_only(variable)
                bbox_run = bbox_from_cid_region(region_name) 
                top10_variable = f"top10{var_run_savefile}"

                #making the choice of textbox size
                textbox_font_size = function_for_textbox(region_name)

                title_run = f'{features_ged_title_name} in {str(vid2date(step))} with top 10 from 1989 to {str(vid2date(EndOfHistory))}, {var_name_run}'
                textbox = f'Name: features,\n{var_run}_at_{str(step)},\nlast input: {str(vid2date(EndOfHistory))}'
                savefile = f'{features_cm_folder}GED_cm{var_run_savefile}_{region_name}_{cmap_run}_month{step}_with_top10.png'

                if region_name in ('globe', 'ame', 'africa'):
                    map_run=Mapper2(
                        width=width_global,
                        height=height_global,
                        frame_on=True,
                        title=title_run,
                        bbox=bbox_run
                    ).add_layer(
                        gdf=data_run,
                        map_dictionary=dictionary_run,
                        cmap='binary',
                        edgecolor="black",
                        linewidth=0.5,
                        transparency = 1.0,
                        column=var_run
                    ).add_layer(
                        gdf=gdf.loc[gdf[top10_variable] > 0].geometry.boundary,
                        color='magenta', 
                        linewidth=3.0
                    ).add_mask(
                        gdf = data_run,
                        map_dictionary = dictionary_run,
                        cmap = cmap_run,
                        transparency = 1,
                        masking_location = region_name,
                        column=var_run,
                        edgecolor="black",
                        linewidth=1
                    ).add_views_textbox(
                        text=textbox,
                        textsize=textbox_font_size)

                    map_run.save(savefile)
                else:
                    map_run=Mapper2(
                        width=width_global,
                        height=height_global,
                        frame_on=True,
                        title=title_run,
                        bbox=bbox_run
                    ).add_mask(
                        gdf = data_run,
                        map_dictionary = dictionary_run,
                        cmap = cmap_run,
                        transparency = country_mapping_transparency_global,
                        background = country_background_global,
                        masking_location = str(cid2name(region_name)),
                        column=var_run,
                        edgecolor="black",
                        linewidth=1, 
                        views_experimental_labels = views_experimental_font_global
                    ).add_layer(
                        gdf=gdf.loc[gdf[top10_variable] > 0].geometry.boundary,
                        color='magenta', 
                        linewidth=3.0
                    ).add_views_textbox(
                        text=textbox,
                        textsize=textbox_font_size)

                    map_run.save(savefile)
    print(f'{user}, cm maps for ged completed with top 10')



    