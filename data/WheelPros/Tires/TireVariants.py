class TireVariants:
    def __init__(self,
                 tire_mfr_cd,
                 part_num,
                 tire_size,
                 tire_description,
                 tire_size_description,
                 load_index,
                 psi,
                 speed_rating,
                 mrsp,
                 stg_item_cd,
                 emarked,
                 upc,
                 section_width,
                 series,
                 rim_diameter,
                 tire_diameter,
                 picture_cd,
                 weight,
                 tire_diameter_2,
                 min_width_in,
                 max_width_in,
                 max_load,
                 power_sports,
                 map,
                 sts,
                 full_model_name,
                 tread_depth,
                 ply,
                 construction_type,
                 terrain,
                 max_load_dual,
                 max_pressure,
                 approved_rim_width,
                 utqg,
                 treadwear,
                 traction,
                 temperature,
                 source_country,
                 mileage_warranty,
                 ):
        self.tire_mfr_cd = tire_mfr_cd
        self.part_num = part_num
        self.tire_size = tire_size
        self.tire_description = tire_description
        self.tire_size_description = tire_size_description
        self.load_index = load_index
        self.psi = psi
        self.speed_rating = speed_rating
        self.mrsp = mrsp
        self.stg_item_cd = stg_item_cd
        self.emarked = emarked
        self.upc = upc
        self.section_width = section_width
        self.series = series
        self.rim_diameter = rim_diameter
        self.tire_diameter = tire_diameter
        self.picture_cd = picture_cd
        self.weight = weight
        self.tire_diameter_2 = tire_diameter_2
        self.min_width_in = min_width_in
        self.max_width_in = max_width_in
        self.max_load = max_load
        self.power_sports = power_sports
        self.map = map
        self.sts = sts
        self.full_model_name = full_model_name
        self.tread_depth = tread_depth
        self.ply = ply
        self.construction_type = construction_type
        self.terrain = terrain
        self.max_load_dual = max_load_dual
        self.max_pressure = max_pressure
        self.approved_rim_width = approved_rim_width
        self.utqg = utqg
        self.treadwear = treadwear
        self.traction = traction
        self.temperature = temperature
        self.source_country = source_country
        self.mileage_warranty = mileage_warranty

    def get_tire_mfr_cd(self):
        return self.tire_mfr_cd

    def get_part_num(self):
        return self.part_num

    def get_tire_size(self):
        return self.tire_size

    def get_tire_description(self):
        return self.tire_description

    def get_tire_size_description(self):
        return self.tire_size_description

    def get_load_index(self):
        return self.load_index

    def get_psi(self):
        return self.psi

    def get_speed_rating(self):
        return self.speed_rating

    def get_mrsp(self):
        return self.mrsp

    def get_stg_item_cd(self):
        return self.stg_item_cd

    def get_emarked(self):
        return self.emarked

    def get_upc(self):
        return self.upc

    def get_section_width(self):
        return self.section_width

    def get_series(self):
        return self.series

    def get_rim_diameter(self):
        return self.rim_diameter

    def get_tire_diameter(self):
        return self.tire_diameter

    def get_picture_cd(self):
        return self.picture_cd

    def get_weight(self):
        return self.weight

    def get_tire_diameter_2(self):
        return self.tire_diameter_2

    def get_min_width_in(self):
        return self.min_width_in

    def get_max_width_in(self):
        return self.max_width_in

    def get_max_load(self):
        return self.max_load

    def get_power_sports(self):
        return self.power_sports

    def get_map(self):
        return self.map

    def get_sts(self):
        return self.sts

    def get_full_model_name(self):
        return self.full_model_name

    def get_tread_depth(self):
        return self.tread_depth

    def get_ply(self):
        return self.ply

    def get_construction_type(self):
        return self.construction_type

    def get_terrain(self):
        return self.terrain

    def get_max_load_dual(self):
        return self.max_load_dual

    def get_max_pressure(self):
        return self.max_pressure

    def get_approved_rim_width(self):
        return self.approved_rim_width

    def get_utqg(self):
        return self.utqg

    def get_treadwear(self):
        return self.treadwear

    def get_traction(self):
        return self.traction

    def get_temperature(self):
        return self.temperature

    def get_source_country(self):
        return self.source_country

    def get_mileage_warranty(self):
        return self.mileage_warranty

    def __eq__(self, o) -> bool:
        pass
        # TODO: Redo this method, just don't have the time at the moment

    def __str__(self) -> str:
        return self.get_tire_description() + self.get_upc()

    def __repr__(self) -> str:
        return super().__repr__()
