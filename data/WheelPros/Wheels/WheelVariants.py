"""
WheelVariants class
- represents Wheel Pros Wheels products
"""


class WheelVariants:
    def __init__(self,
                 style_description,
                 part_number,
                 part_number_description,
                 size,
                 finish,
                 msrp,
                 map,
                 diameter,
                 width,
                 lug_count,
                 bolt_pattern_metric,
                 bolt_pattern_us,
                 offset,
                 backspacing,
                 centerbore,
                 load_rating_lbs,
                 load_rating_kgs,
                 hug_ring_included,
                 upc,
                 inv_order_type,
                 rear_only,
                 hub_clearance,
                 barrel_config,
                 cap_part_num,
                 cap_hardware,
                 qty_of_cap_screws,
                 cap_wrench,
                 testing,
                 picture_cd,
                 max_offset,
                 min_offset,
                 cap_style,
                 other_accessories,
                 tpms_compatable,
                 wheel_weight,
                 shipping_weight,
                 whl_manufact_cd,
                 whl_manufact_num,
                 display_model_num,
                 sort_group,
                 whl_model_nm,
                 full_model_name,
                 county_of_origin,
                 width_in,
                 abrv_finish_desc,
                 box_label_description,
                 finish_warranty,
                 bolt_pattern_mm_1,
                 bolt_pattern_mm_2,
                 smallest_bolt_pattern_mm,
                 largest_bolt_pattern_mm,
                 min_lug_count,
                 max_lug_count,
                 open_end_cap,
                 rivet_part_num,
                 rivet_qty,
                 pvd_finish,
                 stainless_lip,
                 flow_formed,
                 forged,
                 two_piece,
                 steel_wheel,
                 true_beadlock,
                 off_road_use_only,
                 patent,
                 lip_depth,
                 construction,
                 material,
                 fancy_finish_desc,
                 wheel_image,
                 prop65_chemical_1,
                 prop65_chemical_2,
                 prop65_chemical_3):
        self.style_description = style_description
        self.part_number = part_number
        self.part_number_description = part_number_description
        self.size = size
        self.finish = finish
        self.msrp = msrp
        self.map = map
        self.diameter = diameter
        self.width = width
        self.lug_count = lug_count
        self.bolt_pattern_metric = bolt_pattern_metric
        self.bolt_pattern_us = bolt_pattern_us
        self.offset = offset
        self.backspacing = backspacing
        self.centerbore = centerbore
        self.load_rating_lbs = load_rating_lbs
        self.load_rating_kgs = load_rating_kgs
        self.hug_ring_included = hug_ring_included
        self.upc = upc
        self.inv_order_type = inv_order_type
        self.rear_only = rear_only
        self.hub_clearance = hub_clearance
        self.barrel_config = barrel_config
        self.cap_part_num = cap_part_num
        self.cap_hardware = cap_hardware
        self.qty_of_cap_screws = qty_of_cap_screws
        self.cap_wrench = cap_wrench
        self.testing = testing
        self.picture_cd = picture_cd
        self.max_offset = max_offset
        self.min_offset = min_offset
        self.cap_style = cap_style
        self.other_accessories = other_accessories
        self.tpms_compatable = tpms_compatable
        self.wheel_weight = wheel_weight
        self.shipping_weight = shipping_weight
        self.whl_manufact_cd = whl_manufact_cd
        self.whl_manufact_num = whl_manufact_num
        self.display_model_num = display_model_num
        self.sort_group = sort_group
        self.whl_model_Nm = whl_model_nm
        self.full_model_name = full_model_name
        self.country_of_origin = county_of_origin
        self.width_in = width_in
        self.abrv_finish_desc = abrv_finish_desc
        self.box_label_description =box_label_description
        self.finish_warranty = finish_warranty
        self.bolt_pattern_mm_1 = bolt_pattern_mm_1
        self.bolt_pattern_mm_2 = bolt_pattern_mm_2
        self.smallest_bolt_pattern_mm = smallest_bolt_pattern_mm
        self.largest_bolt_pattern_mm = largest_bolt_pattern_mm
        self.min_lug_count = min_lug_count
        self.max_lug_count = max_lug_count
        self.open_end_cap = open_end_cap
        self.rivet_part_num = rivet_part_num
        self.rivet_qty = rivet_qty
        self.pvd_finish = pvd_finish
        self.stainless_lip = stainless_lip
        self.flow_formed = flow_formed
        self.forged = forged
        self.two_piece = two_piece
        self.steel_wheel = steel_wheel
        self.true_beadlock = true_beadlock
        self.off_road_use_only = off_road_use_only
        self.patent = patent
        self.lip_depth = lip_depth
        self.construction = construction
        self.material = material
        self.fancy_finish_desc = fancy_finish_desc
        self.wheel_image = wheel_image
        self.prop65_chemical_1 = prop65_chemical_1
        self.prop65_chemical_2 = prop65_chemical_2
        self.prop65_chemical_3 = prop65_chemical_3

    def get_style_description(self):
        return self.style_description

    def get_part_number(self):
        return self.part_number

    def get_part_number_description(self):
        return self.part_number_description

    def get_size(self):
        return self.size

    def get_finish(self):
        return self.finish

    def get_msrp(self):
        return self.msrp

    def get_map(self):
        return self.map

    def get_diameter(self):
        return self.diameter

    def get_width(self):
        return self.width

    def get_lug_count(self):
        return self.lug_count

    def get_bolt_pattern_metric(self):
        return self.bolt_pattern_metric

    def get_bolt_pattern_us(self):
        return self.bolt_pattern_us

    def get_offset(self):
        return self.offset

    def get_backspacing(self):
        return self.backspacing

    def get_centerbore(self):
        return self.centerbore

    def get_load_rating_lbs(self):
        return self.load_rating_lbs

    def get_load_rating_kgs(self):
        return self.load_rating_kgs

    def get_hug_ring_included(self):
        return self.hug_ring_included

    def get_upc(self):
        return self.upc

    def get_inv_order_type(self):
        return self.inv_order_type

    def get_rear_only(self):
        return self.rear_only

    def get_hub_clearance(self):
        return self.hub_clearance

    def get_barrel_config(self):
        return self.barrel_config

    def get_cap_part_num(self):
        return self.cap_part_num

    def get_cap_hardware(self):
        return self.cap_hardware

    def get_qty_of_cap_screws(self):
        return self.qty_of_cap_screws

    def get_cap_wrench(self):
        return self.cap_wrench

    def get_testing(self):
        return self.testing

    def get_picture_cd(self):
        return self.picture_cd

    def get_max_offset(self):
        return self.max_offset

    def get_min_offset(self):
        return self.min_offset

    def get_cap_style(self):
        return self.cap_style

    def get_other_accessories(self):
        return self.other_accessories

    def get_tpms_compatable(self):
        return self.tpms_compatable

    def get_wheel_weight(self):
        return self.wheel_weight

    def get_shipping_weight(self):
        return self.shipping_weight

    def get_whl_manufact_cd(self):
        return self.whl_manufact_cd

    def get_whl_manufact_num(self):
        return self.whl_manufact_num



    def __eq__(self, o) -> bool:
        """
        Equality method for WheelVariants
        The method goes through and compares all of the
        elements directly
        :param o: other WheelVariant
        :return: If the 2 are the same
        """
        if self.get_style_description() != o.get_style_description():
            return False
        return True

    def compare_map_prices(self, o):
        """
        Compares 2 WheelVariant's map_prices
        :param o: Other WheelVariant
        :return: -1 -> self is more, 0 -> self is the same, 1 -> o is more
        """
        if self.get_map() < o.get_map_price():
            return -1
        elif self.get_map() == o.get_map_price():
            return 0
        else:
            return 1

    def compare_msrp_prices(self, o):
        """
        Compares 2 WheelVariant's msrp_prices
        :param o: Other Wheel Variant
        :return: -1 -> self is more, 0 -> self is the same, 1 -> o is more
        """
        if self.get_msrp() < o.get_msrp_price():
            return -1
        elif self.get_msrp() == o.get_msrp_price():
            return 0
        else:
            return 1

    def __str__(self):
        """
        Str representation of the WheelVariant
        :return:
        """
        return """%s,""" % (self.get_style_description())

    def __repr__(self):
        """
        Repr representation of WheelVariant
        :return:
        """
        return "Wheel Repr"
