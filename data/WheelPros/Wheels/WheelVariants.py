"""
WheelVariants class
- represents Wheel Pros Wheels products
"""


class WheelVariants:
    def __init__(self,
                 data_feed_object,
                 curr_stock,
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
        self.data_feed_object = data_feed_object
        self.curr_stock = curr_stock
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

    def __eq__(self, o) -> bool:
        """
        Equality method for WheelVariants
        The method goes through and compares all of the
        elements directly
        :param o: other WheelVariant
        :return: If the 2 are the same
        """
        if self.style_description != o.style_description:
            return False
        return True

    def compare_map_prices(self, o):
        """
        Compares 2 WheelVariant's map_prices
        :param o: Other WheelVariant
        :return: -1 -> self is more, 0 -> self is the same, 1 -> o is more
        """
        if self.map_price < o.map_price:
            return -1
        elif self.map_price == o.map_price:
            return 0
        else:
            return 1

    def compare_msrp_prices(self, o):
        """
        Compares 2 WheelVariant's msrp_prices
        :param o: Other Wheel Variant
        :return: -1 -> self is more, 0 -> self is the same, 1 -> o is more
        """
        if self.msrp_price < o.msrp_price:
            return -1
        elif self.msrp_price == o.msrp_price:
            return 0
        else:
            return 1

    def __str__(self):
        """
        Str representation of the WheelVariant
        :return:
        """
        return """%s, %s, %s""" % (self.style_description, self.curr_stock, self.part_number)

    def __repr__(self):
        """
        Repr representation of WheelVariant
        :return:
        """
        return "Wheel Repr"
