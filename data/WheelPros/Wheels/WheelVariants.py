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
                 msrp_price,
                 map_price,
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
                 whl_manufact_nm,
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
        self.msrp_price = msrp_price
        self.map_price = map_price
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
        self.whl_manufact_nm = whl_manufact_nm
        self.display_model_num = display_model_num
        self.sort_group = sort_group
        self.whl_model_nm = whl_model_nm
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

    def get_part_num_description(self):
        return self.part_number_description

    def get_size(self):
        return self.size

    def get_finish(self):
        return self.finish

    def get_msrp_price(self):
        return self.msrp_price

    def get_map_price(self):
        return self.map_price

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

    def get_whl_manufact_nm(self):
        return self.whl_manufact_nm

    def get_display_model_num(self):
        return self.display_model_num

    def get_sort_group(self):
        return self.sort_group

    def get_whl_model_nm(self):
        return self.whl_model_nm

    def get_full_model_name(self):
        return self.full_model_name

    def get_country_of_origin(self):
        return self.country_of_origin

    def get_width_in(self):
        return self.width_in

    def get_abrv_finish_desc(self):
        return self.abrv_finish_desc

    def get_box_label_description(self):
        return self.box_label_description

    def get_finish_warranty(self):
        return self.finish_warranty

    def get_bolt_pattern_mm_1(self):
        return self.bolt_pattern_mm_1

    def get_bolt_pattern_mm_2(self):
        return self.bolt_pattern_mm_2

    def get_smallest_bolt_pattern_mm(self):
        return self.smallest_bolt_pattern_mm

    def get_largest_bolt_pattern_mm(self):
        return self.largest_bolt_pattern_mm

    def get_min_lug_count(self):
        return self.min_lug_count

    def get_max_lug_count(self):
        return self.max_lug_count

    def get_open_end_cap(self):
        return self.open_end_cap

    def get_rivet_part_num(self):
        return self.rivet_part_num

    def get_rivet_qty(self):
        return self.rivet_qty

    def get_pvd_finish(self):
        return self.pvd_finish

    def get_stainless_lip(self):
        return self.stainless_lip

    def get_flow_formed(self):
        return self.flow_formed

    def get_forged(self):
        return self.forged

    def get_two_piece(self):
        return self.two_piece

    def get_steel_wheel(self):
        return self.steel_wheel

    def get_true_beadlock(self):
        return self.true_beadlock

    def get_off_road_use_only(self):
        return self.off_road_use_only

    def get_patent(self):
        return self.patent

    def get_lip_depth(self):
        return self.lip_depth

    def get_construction(self):
        return self.construction

    def get_material(self):
        return self.material

    def get_fancy_finish_desc(self):
        return self.fancy_finish_desc

    def get_wheel_image(self):
        return self.wheel_image

    def get_prop65_chemical_1(self):
        return self.prop65_chemical_1

    def get_prop65_chemical_2(self):
        return self.prop65_chemical_2

    def get_prop65_chemical_3(self):
        return self.prop65_chemical_3

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
