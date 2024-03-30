from uiFiles.main_UI import Ui_MainWindow
from Backend.Regex.regexConstant import regexConstant

#'visible-conditions':[
#                    {'cond':'in', 'key':'melk-category','compare-value':['land',
#                                                                     'aparteman',
#                                                                     'official',
#                                                                     'garden',
#                                                                     'commercial',
#                                                                     'villa',
#                                                                     ]},
#                ]


def build_estate_form_info(ui:Ui_MainWindow):

    meta_info = {
                # 'melk-status': {
                #     'type': 'select',
                #     'options-id' : 'melk-status',
                # },

            'melk-category' : {
                    'input': ui.melkCategoryFormInpt,
                    'label': ui.melkCategoryFormLbl,
                    'error': ui.melkCategoryFormError,
                    'frame': ui.melkCategoryFormFrame,
                    'step': 1,
                    'type': 'combobox',
                    'options-id' : 'melk-category',
                    'validation-conditions': [
                        {'cond':'require'}
                    ]
                },

            'city' : {
                    #شهر
                    'input':ui.cityFormInpt,
                    'label':ui.cityFormLbl,
                    'error':ui.cityFormError,
                    'frame':ui.cityFormFrame,
                    'step': 2,
                    'type': 'combobox',
                    'options-id' : 'city',
                },

            'region' : {
                #منطقه
                'input':ui.regionFormInpt,
                'label':ui.regionFormLbl,
                'error':ui.regionFormError,
                'frame':ui.regionFormFrame,
                'step': 2,
                'type': 'spinbox',
                #'options-id' : 'city',
            },

            'street' : {
                #خیابان اصلی
                'input':ui.streetFormInpt,
                'label':ui.streetFormLbl,
                'error':ui.streetFormError,
                'frame':ui.streetFormFrame,
                'step': 2,
                'type': 'input',
            },

            'address' : {
                #آدرس
                'input':ui.addressFormInpt,
                'label':ui.addressFormLbl,
                'error':ui.addressFormError,
                'frame':ui.addressFormFrame,
                'step': 2,
                'type': 'input',
                'validation-conditions': [
                        {'cond':'require'}
                    ]
            },

            'owner-name1' : {
                #نام مالک اول
                'input':ui.ownerName1FormInpt,
                'label':ui.ownerName1FormLbl,
                'error':ui.ownerName1FormError,
                'frame':ui.ownerName1FormFrame,
                'step': 3,
                'type': 'input',
                'validation-conditions': [
                        {'cond':'require'}
                    ]
            },

            'owner-name2' : {
                #نام مالک دوم
                'input':ui.ownerName2FormInpt,
                'label':ui.ownerName2FormLbl,
                'error':ui.ownerName2FormError,
                'frame':ui.ownerName2FormFrame,
                'step': 3,
                'type': 'input',
            },

            'owner1-mobile-number' : {
                # شماره مالک اول
                'input':ui.owner1MobileNumberFormInpt,
                'label':ui.owner1MobileNumberFormLbl,
                'error':ui.owner1MobileNumberFormError,
                'frame':ui.owner1MobileNumberFormFrame,
                'step': 3,
                'type': 'input',
                'validation-conditions': [
                        {'cond':'require'},
                        {'cond':'regex',
                         'key':'owner1-mobile-number', 
                         'compare-value':regexConstant.MOBILE_NUMBER, 
                         'error':'شماره همراه را به درستی و با 0 وارد کنید'
                         },
                    ]
            },

            'owner2-mobile-number' : {
                # شماره مالک دوم
                'input':ui.owner2MobileNumberFormInpt,
                'label':ui.owner2MobileNumberFormLbl,
                'error':ui.owner2MobileNumberFormError,
                'frame':ui.owner2MobileNumberFormFrame,
                'step': 3,
                'type': 'input',
            },
            
            'owner1-phone-number' : {
                # شماره ثابت مالک دوم
                'input':ui.owner1PhoneNumberFormInpt,
                'label':ui.owner1PhoneNumberFormLbl,
                'error':ui.owner1PhoneNumberFormError,
                'frame':ui.owner1PhoneNumberFormFrame,
                'step': 3,
                'type': 'input',
            },

            'tenant_name' : {
                # نام مستاجر
                'input':ui.tenantNameFormInpt,
                'label':ui.tenantNameFormLbl,
                'error':ui.tenantNameFormError,
                'frame':ui.tenantNameFormFrame,
                'step': 3,
                'type': 'input',
            },

            'tenant-phone-number' : {
                # شماره مستاجر
                'input':ui.tenantPhoneNumberFormInpt,
                'label':ui.tenantPhoneNumberFormLbl,
                'error':ui.tenantPhoneNumberFormError,
                'frame':ui.tenantPhoneNumberFormFrame,
                'step': 3,
                'type': 'input',
            },

            'guard-name' : {
                # نام نگهبان
                'input':ui.guardNameFormInpt,
                'label':ui.guardNameFormLbl,
                'error':ui.guardNameFormError,
                'frame':ui.guardNameFormFrame,
                'step': 3,
                'type': 'input',
            },
            
            'guard-phone-number' : {
                # شماره نگهبان
                'input':ui.guardPhoneNumberFormInpt,
                'label':ui.guardPhoneNumberFormLbl,
                'error':ui.guardPhoneNumberFormError,
                'frame':ui.guardPhoneNumberFormFrame,
                'step': 3,
                'type': 'input',
            },

            'owner-description':{
                # توضیحات مالک
                'input':ui.ownerDescriptionFormInpt,
                'label':ui.ownerDescriptionFormLbl,
                'error':ui.ownerDescriptionFormError,
                'frame':ui.ownerDescriptionFormFrame,
                'step': 3,
                'type': 'input',
            },


            'compensation' : {
                #معاوضه'
                'input':None,
                'label':ui.compensationFormLbl,
                'error':ui.compensationFormError,
                'frame':ui.compensationFormFrame,
                'options-container': ui.compensationFormOptionsFrame,
                'type': 'radio',
                'options-id' : 'yes',  
            },

            'compensation-condition' : {
                #شرایط معاوضه
                'input':ui.compensationConditionFormInpt,
                'label':ui.compensationConditionFormLbl,
                'error':ui.compensationConditionFormError,
                'frame':ui.compensationConditionFormFrame,
                'type': 'input',
                'visible-conditions':[
                    {'cond':'=', 'key':'compensation','compare-value':'yes'},
                ]
            },

            'participation' : {
                # مشارکت
                'input':None,
                'label':ui.participationFormLbl,
                'error':ui.participationFormError,
                'frame':ui.participationFormFrame,
                'options-container': ui.participationFormOptionsFrame,
                'type': 'radio',
                'options-id' : 'yes', 
                'visible-conditions':[
                    {'cond':'in', 'key':'melk-category','compare-value':['land']},
                ]
            },

            'document-status' : {
                # وضعیت سند
                'input':ui.documentStatusInpt,
                'label':ui.documentStatusLbl,
                'error':ui.documentStatusError,
                'frame':ui.documentStatusFrame,
                'type': 'combobox',
                'options-id' : 'document-status',
                'visible-conditions':[
                    {'cond':'in', 'key':'melk-category','compare-value':['land',
                                                                     'aparteman',
                                                                     'official',
                                                                     'garden',
                                                                     'commercial',
                                                                     'villa',
                                                                     ]},
                ]
                },

            'meterage' : {
                # متراژ
                'input':ui.meterageFormInpt,
                'label':ui.meterageFormLbl,
                'error':ui.meterageFormError,
                'frame':ui.meterageFormFrame,
                'type': 'spinbox',
                'validation-conditions': [
                        {'cond':'>',  'key':'meterage', 'compare-value':0, 'error':'متراژ نمیتواند ۰  یا کمتر باشد'}
                    ]
            },

            'building-meterage' : {
                # متراژ ساخت
                'input':ui.buildingMeterageFormInpt,
                'label':ui.buildingMeterageFormLbl,
                'error':ui.buildingMeterageFormError,
                'frame':ui.buildingMeterageFormFrame,
                'type': 'spinbox',
                'visible-conditions':[
                    {'cond':'in', 'key':'melk-category','compare-value':['land',
                                                                     'garden',
                                                                     'villa',
                                                                     ]},
                ]

            },

            'land-meterage' : {
                # متراژ زمین
                'input':ui.landMeterageFormInpt,
                'label':ui.landMeterageFormLbl,
                'error':ui.landMeterageFormError,
                'frame':ui.landMeterageFormFrame,
                'type': 'spinbox',
                'visible-conditions':[
                    {'cond':'in', 'key':'melk-category','compare-value':['land',
                                                                     'garden',
                                                                     'villa',
                                                                     ]},
                ]
            },

            'length' : {
                # طول
                'input':ui.lengthFormInpt,
                'label':ui.lengthFormLbl,
                'error':ui.lengthFormError,
                'frame':ui.lengthFormFrame,
                'type': 'spinbox',
                'visible-conditions':[
                    {'cond':'in', 'key':'melk-category','compare-value':['land',
                                                                     'garden',
                                                                     ]},
                ]
            },

            'width' : {
                # عرض
                'input':ui.widthFormInpt,
                'label':ui.widthFormLbl,
                'error':ui.widthFormError,
                'frame':ui.widthFormFrame,
                'type': 'spinbox',
                'visible-conditions':[
                    {'cond':'in', 'key':'melk-category','compare-value':['land',
                                                                     'garden',
                                                                     ]},
                ]
            },

            'opening-width'  : {
                # عرض دهانه
                'input':ui.openingWidthFormInpt,
                'label':ui.openingWidthFormLbl,
                'error':ui.openingWidthFormError,
                'frame':ui.openingWidthFormFrame,
                'type': 'spinbox',
                'visible-conditions':[
                    {'cond':'in', 'key':'melk-category','compare-value':['commercial',
                                                                     ]},
                ]
            },
            

            'price-calculation'  : {
                # نحوه محاسبه قیمت
                'label':ui.PriceCalculationFormLbl,
                'error':ui.PriceCalculationFormError,
                'frame':ui.PriceCalculationFormFrame,
                'options-container': ui.PriceCalculationFormOptionsFrame,
                'options-id': 'price-calculation',
                'type': 'radio',
                'validation-conditions': [
                        {'cond':'require'}
                    ]
            },
            
            'total-price'  : {
                # قیمت کل
                'input':ui.totalPriceFormInpt,
                'label':ui.totalPriceFormLbl,
                'error':ui.totalPriceFormError,
                'frame':ui.totalPriceFormFrame,
                'type': 'input-number',
                'validation-conditions': [
                        {'cond':'require'}
                    ]
            },

            'unit-price'  : {
                # قیمت هر متر مربع
                'input':ui.unitPriceFormInpt,
                'label':ui.unitPriceFormLbl,
                'error':ui.unitPriceFormError,
                'frame':ui.unitPriceFormFrame,
                'type': 'input-number',
            },

            'mortgage-price' : {
                # قیمت رهن
                'input':ui.mortgagePriceFormInpt,
                'label':ui.mortgagePriceFormLbl,
                'error':ui.mortgagePriceFormError,
                'frame':ui.mortgagePriceFormFrame,
                'type': 'input-number',
                'validation-conditions': [
                        {'cond':'require'}
                    ]
            },

            'rent-price' : {
                #قیمت اجاره
                'input':ui.rentPriceFormInpt,
                'label':ui.rentPriceFormLbl,
                'error':ui.rentPriceFormError,
                'frame':ui.rentPriceFormFrame,
                'type': 'input-number',
                'validation-conditions': [
                        {'cond':'require'}
                    ]
            },

            'construction-year' : {
                # سال ساخت
                'input':ui.constructionYearInpt,
                'label':ui.constructionYearLbl,
                'error':ui.constructionYearError,
                'frame':ui.constructionYearFrame,
                'type': 'input',
                'visible-conditions':[
                    {'cond':'in', 'key':'melk-category','compare-value':['aparteman',
                                                                     'official',
                                                                     'commercial',
                                                                     'villa',
                                                                     ]},
                ]
            },

            'floor' : {
                # طبقه
                'input':ui.floorFormInpt,
                'label':ui.floorFormLbl,
                'error':ui.floorFormError,
                'frame':ui.floorFormFrame,
                'type': 'input',
                'visible-conditions':[
                    {'cond':'in', 'key':'melk-category','compare-value':[
                                                                     'aparteman',
                                                                     'official',
                                                                     'commercial',
                                                                     ]},
                ]
            },

            'floor-count' : {
                # تعداد طبقات
                'input':ui.floorCounFormInpt,
                'label':ui.floorCounFormLbl,
                'error':ui.floorCounFormError,
                'frame':ui.floorCounFormFrame,
                'type': 'spinbox',
                'visible-conditions':[
                    {'cond':'in', 'key':'melk-category','compare-value':[
                                                                     'aparteman',
                                                                     'official',
                                                                     'commercial',
                                                                     ]},
                ]
            },

            'total-building-unit' : {
                # تعداد کل واحدها
                'input':ui.totalBuildingUnitFormInpt,
                'label':ui.totalBuildingUnitFormLbl,
                'error':ui.totalBuildingUnitFormError,
                'frame':ui.totalBuildingUnitFormFrame,
                'type': 'spinbox',
                'visible-conditions':[
                    {'cond':'in', 'key':'melk-category','compare-value':[
                                                                     'aparteman',
                                                                     'official',
                                                                     'commercial',
                                                                     ]},
                ]
            },
            
            'floor-unit-count' : {
                # تعداد واحد در طبقه
                'input':ui.floorUnitCountInpt,
                'label':ui.floorUnitCountLbl,
                'error':ui.floorUnitCountError,
                'frame':ui.floorUnitCountFrame,
                'type': 'spinbox',
                'visible-conditions':[
                    {'cond':'in', 'key':'melk-category','compare-value':[
                                                                     'aparteman',
                                                                     'official',
                                                                     'commercial',
                                                                     ]},
                ]
            },

            # 'floors-overal-info' : {
            #     'title':'جزئیات هر طبقه',
            #     'type': 'repeater',
            #     'fields' : {
            #     'floor-meterage' : {
            #         'title':'متراژ طبقه',
            #         'type': 'number',
            #     },

            #     'floor-rooms' : {
            #         'title':'تعداد اتاق طبقه',
            #         'type': 'number',
            #     },
            #     }
            # },


            'light-direction' : {
                # جهت نورگیری,
                'input':ui.lightDirectionInpt,
                'label':ui.lightDirectionLbl,
                'error':ui.lightDirectionError,
                'frame':ui.lightDirectionFrame,
                'type': 'combobox',
                'options-id' : 'light-direction',      
                'visible-conditions':[
                    {'cond':'in', 'key':'melk-category','compare-value':['land',
                                                                     'aparteman',
                                                                     'official',
                                                                     'garden',
                                                                     'commercial',
                                                                     'villa',
                                                                     ]},
                ]
            },

            'rebuilding' : {
                # وضعیت بازسازی'
                'input':None,
                'label':ui.rebuildingFormLbl,
                'error':ui.rebuildingFormError,
                'frame':ui.rebuildingFormFrame,
                'options-container': ui.rebuildingFormOptionsFrame,
                'type': 'radio',
                'options-id' : 'rebuilding',
                'visible-conditions':[
                    {'cond':'in', 'key':'melk-category','compare-value':['aparteman',
                                                                     'official',
                                                                     'garden',
                                                                     'commercial',
                                                                     'villa',
                                                                     ]},
                ]

            },

            'building-license' : {
                # پروانه ساخت
                'input':None,
                'label':ui.buildingLicenseFormLbl,
                'error':ui.buildingLicenseFormError,
                'frame':ui.buildingLicenseFormFrame,
                'options-container': ui.buildingLicenseFormOptionsFrame,
                'type': 'radio',
                'options-id' : 'have',
                'visible-conditions':[
                    {'cond':'in', 'key':'melk-category','compare-value':['land',
                                                                     ]},
                ]
            },
            
            'parking' : {
                # پارکینگ 
                'input':None,
                'label':ui.parkingFormLbl,
                'error':ui.parkingFormError,
                'frame':ui.parkingFormFrame,
                'options-container': ui.parkingFormOptionsFrame,
                'type': 'radio',
                'options-id' : 'have',
                'visible-conditions':[
                    {'cond':'in', 'key':'melk-category','compare-value':[
                                                                     'aparteman',
                                                                     'official',
                                                                     'garden',
                                                                     'commercial',
                                                                     'villa',
                                                                     ]},
                ]
            },

            'parking-status' : {
                # وضعیت پارکینگ 
                'input':ui.parkingStatusFormInpt,
                'label':ui.parkingStatusFormLbl,
                'error':ui.parkingStatusFormError,
                'frame':ui.parkingStatusFormFrame,
                'type': 'combobox',
                'options-id' : 'parking-status',
                'visible-conditions':[
                    {'cond':'=', 'key':'parking','compare-value':'have'},
                    {'cond':'in', 'key':'melk-category','compare-value':[
                                                                     'aparteman',
                                                                     'official',
                                                                     'garden',
                                                                     'commercial',
                                                                     'villa',
                                                                     ]},
                ]
            },

            'parking-count' : {
                # تعداد پارکینگ
                'input':ui.parkingCountFormInpt,
                'label':ui.parkingCountFormLbl,
                'error':ui.parkingCountFormError,
                'frame':ui.parkingCountFormFrame,
                'type': 'spinbox',
                'visible-conditions':[
                    {'cond':'=', 'key':'parking','compare-value':'have'},
                    {'cond':'in', 'key':'melk-category','compare-value':[
                                                                     'aparteman',
                                                                     'official',
                                                                     'garden',
                                                                     'commercial',
                                                                     'villa',
                                                                     ]},
                ]
                
            },

            'balcony' : {
                # بالکن
                'input':None,
                'label':ui.balconyFormLbl,
                'error':ui.balconyFormError,
                'frame':ui.balconyFormFrame,
                'options-container': ui.balconyFormOptionsFrame,
                'type': 'radio',
                'options-id' : 'have',
                'visible-conditions':[
                    {'cond':'in', 'key':'melk-category','compare-value':['aparteman',
                                                                     'official',
                                                                     'garden',
                                                                     'commercial',
                                                                     'villa',
                                                                     ]},
                ]

                
            },

            'balcony-meterage' : {
                # متراژ بالکن
                'input':ui.balconyMeterageFormInpt,
                'label':ui.balconyMeterageFormLbl,
                'error':ui.balconyMeterageFormError,
                'frame':ui.balconyMeterageFormFrame,
                'type': 'spinbox',
                'visible-conditions':[
                    {'cond':'=', 'key':'balcony','compare-value':'have'},
                ]
            },

            'trass' : {
                # بهار خواب
                'input':None,
                'label':ui.trassFormLbl,
                'error':ui.trassFormError,
                'frame':ui.trassFormFrame,
                'options-container': ui.trassFormOptionsFrame,
                'type': 'radio',
                'options-id' : 'have',
                'visible-conditions':[
                    {'cond':'in', 'key':'melk-category','compare-value':['aparteman',
                                                                     'official',
                                                                     'garden',
                                                                     'commercial',
                                                                     'villa',
                                                                     ]},
                ]
            },

            'trass-meterage' : {
                # متراژ بهار خواب
                'input':ui.trassMeterageFormInpt,
                'label':ui.trassMeterageFormLbl,
                'error':ui.trassMeterageFormError,
                'frame':ui.trassMeterageFormFrame,
                'type': 'spinbox',
                'visible-conditions':[
                    {'cond':'=', 'key':'trass','compare-value':'have'},
                ]
            },

            
            'warehouse' : {
                #انباری
                'input':None,
                'label':ui.warehouseFormLbl,
                'error':ui.warehouseFormError,
                'frame':ui.warehouseFormFrame,
                'options-container': ui.warehouseFormOptionsFrame,
                'type': 'radio',
                'options-id' : 'have',
                'visible-conditions':[
                    {'cond':'in', 'key':'melk-category','compare-value':['aparteman',
                                                                     'official',
                                                                     'garden',
                                                                     'commercial',
                                                                     'villa',
                                                                     ]},
                ]
            },

            'warehouse-meterage' : {
                # متراژ انباری
                'input':ui.warehouseMeterageFormInpt,
                'label':ui.warehouseMeterageFormLbl,
                'error':ui.warehouseMeterageFormError,
                'frame':ui.warehouseMeterageFormFrame,
                'type': 'spinbox',
                'visible-conditions':[
                    {'cond':'=', 'key':'warehouse','compare-value':'have'},
                    
                ]
            },

            'private-yard' : {
                # حیاط اختصاصی
                'input':None,
                'label':ui.privateYardFormLbl,
                'error':ui.privateYardFormError,
                'frame':ui.privateYardFormFrame,
                'options-container': ui.privateYardFormOptionsFrame,
                'type': 'radio',
                'options-id' : 'have',
                'visible-conditions':[
                    {'cond':'in', 'key':'melk-category','compare-value':['aparteman',
                                                                     'official',
                                                                     'commercial',
                                                                     'villa',
                                                                     ]},
                ]
                
            },

            'private-yard-meterage' : {
                # متراژ حیاط اختصاصی
                'input':ui.privateYardMeterageFormInpt,
                'label':ui.privateYardMeterageFormLbl,
                'error':ui.privateYardMeterageFormError,
                'frame':ui.privateYardMeterageFormFrame,
                'type': 'spinbox',
                'visible-conditions':[
                    {'cond':'=', 'key':'private-yard','compare-value':'have'},
                ]
            },

            'elevator' : {
                # آسانسور
                'input':None,
                'label':ui.elevatorFormLbl,
                'error':ui.elevatorFormError,
                'frame':ui.elevatorFormFrame,
                'options-container': ui.elevatorFormOptionsFrame,
                'type': 'radio',
                'options-id' : 'have',
                'visible-conditions':[
                    {'cond':'in', 'key':'melk-category','compare-value':[
                                                                     'aparteman',
                                                                     'official',
                                                                     'garden',
                                                                     'commercial',
                                                                     'villa',
                                                                     ]},
                ]
            },

            
            

            'other-features' : {
                # سایر امکانات
                'input':None,
                'label':ui.otherFeaturesFormLbl,
                'error':ui.otherFeaturesFormError,
                'frame':ui.otherFeaturesFormFrame,
                'options-container': ui.otherFeaturesFormOptionsFrame,
                'type': 'checkbox',
                'options-id' : 'other-features',
            },

            'branch' : {
                # انشعابات
                'input':None,
                'label':ui.branchFormLbl,
                'error':ui.branchFormError,
                'frame':ui.branchFormFrame,
                'options-container': ui.branchFormOptionsFrame,
                'type': 'checkbox',
                'options-id' : 'branch',
            },
            
            # 'other-features-repeater' : {
            #     'title':'سایر امکانات',
            #     'type': 'repeater',
            #     'fields' : {
            #     'other-feature-name' : {
            #         'title':'نام',
            #         'type': 'text',
            #     }
            #     },
                
            # },

            'floor-material' : {
                # جنس کف
                'input':None,
                'label':ui.floorMaterialFormLbl,
                'error':ui.floorMaterialFormError,
                'frame':ui.floorMaterialFormFrame,
                'options-container': ui.floorMaterialFormOptionsFrame,
                'type': 'checkbox',
                'options-id': 'floor-material',
                'visible-conditions':[
                    {'cond':'in', 'key':'melk-category','compare-value':['aparteman',
                                                                     'official',
                                                                     'garden',
                                                                     'commercial',
                                                                     'villa',
                                                                     ]},
                ]
                
            },

            'other-floor-material' : {
                    #‌ سایر جنس کف‍
                    'input':ui.otherFloorMaterialFormInpt,
                    'label':None,
                    'error':None,
                    'frame':ui.otherFloorMaterialFormFrame,
                    'type': 'input',
                    'visible-conditions':[
                        {'cond':'contain', 'key':'floor-material','compare-value':'other'},
                    ]
                    
            },

            'ceiling-material' : {
                # جنس سقف
                'input':None,
                'label':ui.ceilingMaterialFormLbl,
                'error':ui.ceilingMaterialFormError,
                'frame':ui.ceilingMaterialFormFrame,
                'options-container': ui.ceilingMaterialFormOptionsFrame,
                'type': 'checkbox',
                'options-id': 'ceiling-material',
                'visible-conditions':[
                    {'cond':'in', 'key':'melk-category','compare-value':['aparteman',
                                                                     'official',
                                                                     'garden',
                                                                     'commercial',
                                                                     'villa',
                                                                     ]},
                ]
                
            },

            'other-ceiling-material' : {
                    #‌ سایر جنس سقف
                    'input':ui.otherCeilingMaterialFormInpt,
                    'label':None,
                    'error':None,
                    'frame':ui.otherCeilingMaterialFormFrame,
                    'type': 'input',
                    'visible-conditions':[
                        {'cond':'contain', 'key':'ceiling-material','compare-value':'other'},
                    ]
            },

            'walls-material' : {
                # جنس دیوار
                'input':None,
                'label':ui.wallsMaterialFormLbl,
                'error':ui.wallsMaterialFormError,
                'frame':ui.wallsMaterialFormFrame,
                'options-container': ui.wallsMaterialFormOptionsFrame,
                'type': 'checkbox',
                'options-id': 'walls-material',
                'visible-conditions':[
                    {'cond':'in', 'key':'melk-category','compare-value':['aparteman',
                                                                     'official',
                                                                     'garden',
                                                                     'commercial',
                                                                     'villa',
                                                                     ]},
                ]
                
            },

            'other-walls-material' : {
                    #‌ سایر جنس دیوار
                    'input':ui.otherWallsMaterialFormInpt,
                    'label':None,
                    'error':None,
                    'frame':ui.otherWallsMaterialFormFrame,
                    'type': 'input',
                    'visible-conditions':[
                        {'cond':'contain', 'key':'walls-material','compare-value':'other'},
                    ]
            },


            'cabinets-material' : {
                # جنس کابینت
                'input':None,
                'label':ui.cabinetsMaterialFormLbl,
                'error':ui.cabinetsMaterialFormError,
                'frame':ui.cabinetsMaterialFormFrame,
                'options-container': ui.cabinetsMaterialFormOptionsFrame,
                'type': 'checkbox',
                'options-id': 'cabinets-material',
                'visible-conditions':[
                    {'cond':'in', 'key':'melk-category','compare-value':['aparteman',
                                                                     'official',
                                                                     'garden',
                                                                     'commercial',
                                                                     'villa',
                                                                     ]},
                ]
                
            },

            'other-cabinets-material' : {
                    #‌ سایر جنس کابینت
                    'input':ui.otherCabinetsMaterialFormInpt,
                    'label':None,
                    'error':None,
                    'frame':ui.otherCabinetsMaterialFormFrame,
                    'type': 'input',
                    'visible-conditions':[
                        {'cond':'contain', 'key':'cabinets-material','compare-value':'other'},
                    ]
            },


            'warming-system' : {
                # سیستم گرمایشی
                'input':None,
                'label':ui.warmingSystemFormLbl,
                'error':ui.warmingSystemFormError,
                'frame':ui.warmingSystemFormFrame,
                'options-container': ui.warmingSystemFormOptionsFrame,
                'type': 'checkbox',
                'options-id': 'warming-system',
                'visible-conditions':[
                    {'cond':'in', 'key':'melk-category','compare-value':['aparteman',
                                                                     'official',
                                                                     'garden',
                                                                     'commercial',
                                                                     'villa',
                                                                     ]},
                ]
                
                
            },

            'other-warming-system' : {
                    #‌ سایر سیستم گرمایشی
                    'input':ui.otherWarmingSystemFormInpt,
                    'label':None,
                    'error':None,
                    'frame':ui.otherWarmingSystemFormFrame,
                    'type': 'input',
                    'visible-conditions':[
                        {'cond':'contain', 'key':'warming-system','compare-value':'other'},
                    ]
            },


            'cooling-system' : {
                # سیستم سرمایشی
                'input':None,
                'label':ui.coolingSystemFormLbl,
                'error':ui.coolingSystemFormError,
                'frame':ui.coolingSystemFormFrame,
                'options-container': ui.coolingSystemFormOptionsFrame,
                'type': 'checkbox',
                'options-id': 'cooling-system',
                'visible-conditions':[
                    {'cond':'in', 'key':'melk-category','compare-value':['aparteman',
                                                                     'official',
                                                                     'garden',
                                                                     'commercial',
                                                                     'villa',
                                                                     ]},
                ]
                
                
            },

            'other-cooling-system' : {
                    #‌ سایر سیستم سرمایشی
                    'input':ui.otherCoolingSystemFormInpt,
                    'label':None,
                    'error':None,
                    'frame':ui.otherCoolingSystemFormFrame,
                    'type': 'input',
                    'visible-conditions':[
                        {'cond':'contain', 'key':'cooling-system','compare-value':'other'},
                    ]
            },


            'kitchen-material' : {
                # جنس آشپزخانه
                'input':None,
                'label':ui.kitchenMaterialFormLbl,
                'error':ui.kitchenMaterialFormError,
                'frame':ui.kitchenMaterialFormFrame,
                'options-container': ui.kitchenMaterialFormOptionsFrame,
                'type': 'checkbox',
                'options-id': 'kitchen-material',
                'visible-conditions':[
                    {'cond':'in', 'key':'melk-category','compare-value':['aparteman',
                                                                     'official',
                                                                     'garden',
                                                                     'commercial',
                                                                     'villa',
                                                                     ]},
                ]
                
                
            },

            'other-kitchen-material' : {
                    #‌ سایر جنس آشپزخانه
                    'input':ui.otherKitchenMaterialFormInpt,
                    'label':None,
                    'error':None,
                    'frame':ui.otherKitchenMaterialFormFrame,
                    'type': 'input',
                    'visible-conditions':[
                        {'cond':'contain', 'key':'kitchen-material','compare-value':'other'},
                    ]
            },


            'bathroom-material' : {
                # جنس حمام
                'input':None,
                'label':ui.bathroomMaterialFormLbl,
                'error':ui.bathroomMaterialFormError,
                'frame':ui.bathroomMaterialFormFrame,
                'options-container': ui.bathroomMaterialFormOptionsFrame,
                'type': 'checkbox',
                'options-id': 'bathroom-material',
                'visible-conditions':[
                    {'cond':'in', 'key':'melk-category','compare-value':['aparteman',
                                                                     'official',
                                                                     'garden',
                                                                     'commercial',
                                                                     'villa',
                                                                     ]},
                ]
                
                
            },

            'other-bathroom-material' : {
                    #‌ سایر جنس حمام
                    'input':ui.otherBathroomMaterialFormInpt,
                    'label':None,
                    'error':None,
                    'frame':ui.otherBathroomMaterialFormFrame,
                    'type': 'input',
                    'visible-conditions':[
                        {'cond':'contain', 'key':'bathroom-material','compare-value':'other'},
                    ]
            },

            'wc-material' : {
                # جنس سرویس بهداشتی
                'input':None,
                'label':ui.wcMaterialFormLbl,
                'error':ui.wcMaterialFormError,
                'frame':ui.wcMaterialFormFrame,
                'options-container': ui.wcMaterialFormOptionsFrame,
                'type': 'checkbox',
                'options-id': 'wc-material',
                'visible-conditions':[
                    {'cond':'in', 'key':'melk-category','compare-value':['aparteman',
                                                                     'official',
                                                                     'garden',
                                                                     'commercial',
                                                                     'villa',
                                                                     ]},
                ]
                
            },

            'other-wc-material' : {
                    #‌ سایر جنس سرویس بهداشتی
                    'input':ui.otherWcMaterialFormInpt,
                    'label':None,
                    'error':None,
                    'frame':ui.otherWcMaterialFormFrame,
                    'type': 'input',
                    'visible-conditions':[
                        {'cond':'contain', 'key':'wc-material','compare-value':'other'},
                    ]
            },


            'door-material' : {
                # جنس درب
                'input':None,
                'label':ui.doorMaterialFormLbl,
                'error':ui.doorMaterialFormError,
                'frame':ui.doorMaterialFormFrame,
                'options-container': ui.doorMaterialFormOptionsFrame,
                'type': 'checkbox',
                'options-id': 'door-material',
                'visible-conditions':[
                    {'cond':'in', 'key':'melk-category','compare-value':['aparteman',
                                                                     'official',
                                                                     'garden',
                                                                     'commercial',
                                                                     'villa',
                                                                     ]},
                ]
            },

            'other-door-material' : {
                    #‌ سایر جنس درب
                    'input':ui.otherDoorMaterialFormInpt,
                    'label':None,
                    'error':None,
                    'frame':ui.otherDoorMaterialFormFrame,
                    'type': 'input',
                    'visible-conditions':[
                        {'cond':'contain', 'key':'door-material','compare-value':'other'},
                    ]
            },


            'window-material' : {
                # جنس پنجره
                'input':None,
                'label':ui.windowMaterialFormLbl,
                'error':ui.windowMaterialFormError,
                'frame':ui.windowMaterialFormFrame,
                'options-container': ui.windowMaterialFormOptionsFrame,
                'type': 'checkbox',
                'options-id': 'window-material',
                'visible-conditions':[
                    {'cond':'in', 'key':'melk-category','compare-value':['aparteman',
                                                                     'official',
                                                                     'garden',
                                                                     'commercial',
                                                                     'villa',
                                                                     ]},
                ]
            },

            'other-window-material' : {
                    #‌ سایر جنس پنجره
                    'input':ui.otherWindowMaterialFormInpt,
                    'label':None,
                    'error':None,
                    'frame':ui.otherWindowMaterialFormFrame,
                    'type': 'input',
                    'visible-conditions':[
                        {'cond':'contain', 'key':'window-material','compare-value':'other'},
                    ]
            },

            'description' : {
                    #‌ توضیحات تکمیلی
                    'input':ui.descriptionFormInpt,
                    'label':ui.descriptionFormLbl,
                    'error':ui.descriptionFormError,
                    'frame':ui.descriptionFormError,
                    'type': 'input',
            },


            # 'gallery' : {
            #     'title':'گالری',
            #     'type': 'textarea',
            # },

            # 'featured-image' : {
            #     'title':'تصویر شاخص',
            #     'type': 'textarea',
            # },    
            }
    
    return meta_info