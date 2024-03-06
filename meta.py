from uiFiles.main_UI import Ui_MainWindow

class Form:

    def __init__(self, ui:Ui_MainWindow) -> None:
        self.ui = ui
        
        self.melk_post_type = {
            'melk-status': {
                'type': 'select',
                'options' : 'melk-status',
            },

        'melk-category' : {
                'input': self.ui.melkCategoryFormInpt,
                'label': self.ui.melkCategoryFormLbl,
                'error': self.ui.melkCategoryFormError,
                'frame': self.ui.melkCategoryFormFrame,
                'type': 'combobox',
                'options' : 'melk-category',
            },

        'city' : {
                #شهر
                'input':self.ui.cityFormInpt,
                'label':self.ui.cityFormLbl,
                'error':self.ui.cityFormError,
                'frame':self.ui.cityFormFrame,
                'type': 'combobox',
                'options' : 'city',
            },

        'region' : {
            #منطقه
            'input':self.ui.regionFormInpt,
            'label':self.ui.regionFormLbl,
            'error':self.ui.regionFormError,
            'frame':self.ui.regionFormFrame,
            'type': 'spinbox',
            'options' : 'city',
        },

        'street' : {
            #خیابان اصلی
            'input':self.ui.streetFormInpt,
            'label':self.ui.streetFormLbl,
            'error':self.ui.streetFormError,
            'frame':self.ui.streetFormFrame,
            'type': 'input',
        },

        'address' : {
            #آدرس
            'input':self.ui.addressFormInpt,
            'label':self.ui.addressFormLbl,
            'error':self.ui.addressFormError,
            'frame':self.ui.addressFormFrame,
            'type': 'input',
        },

        'owner-name1' : {
            #نام مالک اول
            'input':self.ui.ownerName1FormInpt,
            'label':self.ui.ownerName1FormLbl,
            'error':self.ui.ownerName1FormError,
            'frame':self.ui.ownerName1FormFrame,
            'type': 'input',
        },

        'owner-name2' : {
            #نام مالک دوم
            'input':self.ui.ownerName2FormInpt,
            'label':self.ui.ownerName2FormLbl,
            'error':self.ui.ownerName2FormError,
            'frame':self.ui.ownerName2FormFrame,
            'type': 'input',
        },

        'owner1-mobile-number' : {
            # شماره مالک اول
            'input':self.ui.owner1MobileNumberFormInpt,
            'label':self.ui.owner1MobileNumberFormLbl,
            'error':self.ui.owner1MobileNumberFormError,
            'frame':self.ui.owner1MobileNumberFormFrame,
            'type': 'input',
        },

        'owner2-mobile-number' : {
            # شماره مالک دوم
            'input':self.ui.owner2MobileNumberFormInpt,
            'label':self.ui.owner2MobileNumberFormLbl,
            'error':self.ui.owner2MobileNumberFormError,
            'frame':self.ui.owner2MobileNumberFormFrame,
            'type': 'input',
        },
        
        'owner1-phone-number' : {
            # شماره ثابت مالک دوم
            'input':self.ui.owner1PhoneNumberFormInpt,
            'label':self.ui.owner1PhoneNumberFormLbl,
            'error':self.ui.owner1PhoneNumberFormError,
            'frame':self.ui.owner1PhoneNumberFormFrame,
            'type': 'input',
        },

        'tenant_name' : {
            # نام مستاجر
            'input':self.ui.tenantNameFormInpt,
            'label':self.ui.tenantNameFormLbl,
            'error':self.ui.tenantNameFormError,
            'frame':self.ui.tenantNameFormFrame,
            'type': 'input',
        },

        'tenant-phone-number' : {
            # شماره مستاجر
            'input':self.ui.tenantPhoneNumberFormInpt,
            'label':self.ui.tenantPhoneNumberFormLbl,
            'error':self.ui.tenantPhoneNumberFormError,
            'frame':self.ui.tenantPhoneNumberFormFrame,
            'type': 'input',
        },

        'guard-name' : {
            # نام نگهبان
            'input':self.ui.guardNameFormInpt,
            'label':self.ui.guardNameFormLbl,
            'error':self.ui.guardNameFormError,
            'frame':self.ui.guardNameFormFrame,
            'type': 'input',
        },
        
        'guard-phone-number' : {
            # شماره نگهبان
            'input':self.ui.guardPhoneNumberFormInpt,
            'label':self.ui.guardPhoneNumberFormLbl,
            'error':self.ui.guardPhoneNumberFormError,
            'frame':self.ui.guardPhoneNumberFormFrame,
            'type': 'input',
        },

        'owner-description':{
            # توضیحات مالک
            'input':self.ui.ownerDescriptionFormInpt,
            'label':self.ui.ownerDescriptionFormLbl,
            'error':self.ui.ownerDescriptionFormError,
            'frame':self.ui.ownerDescriptionFormFrame,
            'type': 'input',
        },


        'compensation' : {
            #معاوضه'
            'input':None,
            'label':self.ui.compensationFormLbl,
            'error':self.ui.compensationFormLbl,
            'frame':self.ui.compensationFormFrame,
            'options-container': self.ui.compensationFormOptionsFrame,
            'type': 'radio',
            'options-id' : 'yes',  
        },

        'compensation-condition' : {
            #شرایط معاوضه
            'input':self.ui.compensationConditionFormInpt,
            'label':self.ui.compensationConditionFormLbl,
            'error':self.ui.compensationConditionFormError,
            'frame':self.ui.compensationConditionFormFrame,
            'type': 'input',
        },

        'participation' : {
            # مشارکت
            'input':None,
            'label':self.ui.participationFormLbl,
            'error':self.ui.participationFormError,
            'frame':self.ui.participationFormFrame,
            'options-container': self.ui.participationFormOptionsFrame,
            'type': 'radio',
            'options-id' : 'yes', 
        },

        'document-status' : {
            # وضعیت سند
            'input':self.ui.documentStatusInpt,
            'label':self.ui.documentStatusLbl,
            'error':self.ui.documentStatusError,
            'frame':self.ui.documentStatusFrame,
            'type': 'combobox',
            'options' : 'document-status',
            },

        'meterage' : {
            # متراژ
            'input':self.ui.meterageFormInpt,
            'label':self.ui.meterageFormLbl,
            'error':self.ui.meterageFormError,
            'frame':self.ui.meterageFormFrame,
            'type': 'spinbox',
        },

        'building-meterage' : {
            # متراژ ساخت
            'input':self.ui.buildingMeterageFormInpt,
            'label':self.ui.buildingMeterageFormLbl,
            'error':self.ui.buildingMeterageFormError,
            'frame':self.ui.buildingMeterageFormFrame,
            'type': 'spinbox',
        },

        'land-meterage' : {
            # متراژ زمین
            'input':self.ui.landMeterageFormInpt,
            'label':self.ui.landMeterageFormLbl,
            'error':self.ui.landMeterageFormError,
            'frame':self.ui.landMeterageFormFrame,
            'type': 'spinbox',
        },

        'length' : {
            # طول
            'input':self.ui.lengthFormInpt,
            'label':self.ui.lengthFormLbl,
            'error':self.ui.lengthFormError,
            'frame':self.ui.lengthFormFrame,
            'type': 'spinbox',
        },

        'width' : {
            # عرض
            'input':self.ui.widthFormInpt,
            'label':self.ui.widthFormLbl,
            'error':self.ui.widthFormError,
            'frame':self.ui.widthFormFrame,
            'type': 'spinbox',
        },

        'opening-width'  : {
            # عرض دهانه
            'input':self.ui.openingWidthFormInpt,
            'label':self.ui.openingWidthFormLbl,
            'error':self.ui.openingWidthFormError,
            'frame':self.ui.openingWidthFormFrame,
            'type': 'spinbox',
        },
        
        'total-price'  : {
            # قیمت کل
            'input':self.ui.totalPriceFormInpt,
            'label':self.ui.totalPriceFormLbl,
            'error':self.ui.totalPriceFormError,
            'frame':self.ui.totalPriceFormFrame,
            'type': 'input',
        },

        'unit-price'  : {
            # قیمت هر متر مربع
            'input':self.ui.unitPriceFormInpt,
            'label':self.ui.unitPriceFormLbl,
            'error':self.ui.unitPriceFormError,
            'frame':self.ui.unitPriceFormFrame,
            'type': 'input',
        },

        'mortgage-price' : {
            # قیمت رهن
            'input':self.ui.mortgagePriceFormInpt,
            'label':self.ui.mortgagePriceFormLbl,
            'error':self.ui.mortgagePriceFormError,
            'frame':self.ui.mortgagePriceFormFrame,
            'type': 'input',
        },

        'rent-price' : {
            #قیمت اجاره
            'input':self.ui.rentPriceFormInpt,
            'label':self.ui.rentPriceFormLbl,
            'error':self.ui.rentPriceFormError,
            'frame':self.ui.rentPriceFormFrame,
            'type': 'input',
        },

        'construction-year' : {
            # سال ساخت
            'input':self.ui.constructionYearInpt,
            'label':self.ui.constructionYearLbl,
            'error':self.ui.constructionYearError,
            'frame':self.ui.constructionYearFrame,
            'type': 'input',
        },

        'floor' : {
            # طبقه
            'input':self.ui.floorFormInpt,
            'label':self.ui.floorFormLbl,
            'error':self.ui.floorFormError,
            'frame':self.ui.floorFormFrame,
            'type': 'input',
        },

        'floor-count' : {
            # تعداد طبقات
            'input':self.ui.floorCounFormInpt,
            'label':self.ui.floorCounFormLbl,
            'error':self.ui.floorCounFormError,
            'frame':self.ui.floorCounFormFrame,
            'type': 'spinbox',
        },

        'total-building-unit' : {
            # تعداد کل واحدها
            'input':self.ui.totalBuildingUnitFormInpt,
            'label':self.ui.totalBuildingUnitFormLbl,
            'error':self.ui.totalBuildingUnitFormError,
            'frame':self.ui.totalBuildingUnitFormFrame,
            'type': 'spinbox',
        },
        
        'floor-unit-count' : {
            # تعداد واحد در طبقه
            'input':self.ui.floorUnitCountInpt,
            'label':self.ui.floorUnitCountLbl,
            'error':self.ui.floorUnitCountError,
            'frame':self.ui.floorUnitCountFrame,
            'type': 'spinbox',
        },

        'floors-overal-info' : {
            'title':'جزئیات هر طبقه',
            'type': 'repeater',
            'fields' : {
            'floor-meterage' : {
                'title':'متراژ طبقه',
                'type': 'number',
            },

            'floor-rooms' : {
                'title':'تعداد اتاق طبقه',
                'type': 'number',
            },
            }
        },


        'light-direction' : {
            # جهت نورگیری,
            'input':self.ui.lightDirectionInpt,
            'label':self.ui.lightDirectionLbl,
            'error':self.ui.lightDirectionError,
            'frame':self.ui.lightDirectionFrame,
            'type': 'combocox',
            'options-id' : 'light-direction',      
        },

        'rebuilding' : {
            # وضعیت بازسازی'
            'input':None,
            'label':self.ui.rebuildingFormLbl,
            'error':self.ui.rebuildingFormError,
            'frame':self.ui.rebuildingFormFrame,
            'options-container': self.ui.rebuildingFormOptionsFrame,
            'type': 'radio',
            'options' : 'rebuilding',

        },

        'building-license' : {
            # پروانه ساخت
            'input':None,
            'label':self.ui.buildingLicenseFormLbl,
            'error':self.ui.buildingLicenseFormError,
            'frame':self.ui.buildingLicenseFormFrame,
            'options-container': self.ui.buildingLicenseFormOptionsFrame,
            'type': 'radio',
            'options' : 'have',
        },
        
        'parking' : {
            # پارکینگ 
            'input':None,
            'label':self.ui.parkingFormLbl,
            'error':self.ui.parkingFormError,
            'frame':self.ui.parkingFormFrame,
            'options-container': self.ui.parkingFormOptionsFrame,
            'type': 'radio',
            'options' : 'have',
        },

        'parking-status' : {
            # وضعیت پارکینگ 
            'input':self.ui.parkingStatusFormInpt,
            'label':self.ui.parkingStatusFormLbl,
            'error':self.ui.parkingStatusFormError,
            'frame':self.ui.parkingStatusFormFrame,
            'type': 'combobox',
            'options' : 'parking-status',
        },

        'parking-count' : {
            # تعداد پارکینگ
            'input':self.ui.parkingCountFormInpt,
            'label':self.ui.parkingCountFormLbl,
            'error':self.ui.parkingCountFormError,
            'frame':self.ui.parkingCountFormFrame,
            'options-container': self.ui.rebuildingFormOptionsFrame,
            'type': 'radio',
            'options' : 'have',
        },

        'balcony' : {
            # بالکن
            'input':None,
            'label':self.ui.balconyFormLbl,
            'error':self.ui.balconyFormError,
            'frame':self.ui.balconyFormFrame,
            'options-container': self.ui.balconyFormOptionsFrame,
            'type': 'radio',
            'options' : 'have',
        },

        'balcony-meterage' : {
            # متراژ بالکن
            'input':self.ui.balconyMeterageFormInpt,
            'label':self.ui.balconyMeterageFormLbl,
            'error':self.ui.balconyMeterageFormError,
            'frame':self.ui.balconyMeterageFormFrame,
            'type': 'spinbox',
        },

        'trass' : {
            # بهار خواب
            'input':None,
            'label':self.ui.trassFormLbl,
            'error':self.ui.trassFormError,
            'frame':self.ui.trassFormFrame,
            'options-container': self.ui.trassFormOptionsFrame,
            'type': 'radio',
            'options' : 'have',
        },

        'trass-meterage' : {
            # متراژ بهار خواب
            'input':self.ui.trassMeterageFormInpt,
            'label':self.ui.trassMeterageFormLbl,
            'error':self.ui.trassMeterageFormError,
            'frame':self.ui.trassMeterageFormFrame,
            'type': 'spinbox',
        },

        
        'warehouse' : {
            #انباری
            'input':None,
            'label':self.ui.warehouseFormLbl,
            'error':self.ui.warehouseFormError,
            'frame':self.ui.warehouseFormFrame,
            'options-container': self.ui.warehouseFormOptionsFrame,
            'type': 'radio',
            'options' : 'have',
        },

        'warehouse-meterage' : {
            # متراژ انباری
            'input':self.ui.warehouseMeterageFormInpt,
            'label':self.ui.warehouseMeterageFormLbl,
            'error':self.ui.warehouseMeterageFormError,
            'frame':self.ui.warehouseMeterageFormFrame,
            'type': 'spinbox',
        },

        'private-yard' : {
            # حیاط اختصاصی
            'input':None,
            'label':self.ui.privateYardFormLbl,
            'error':self.ui.privateYardFormError,
            'frame':self.ui.privateYardFormFrame,
            'options-container': self.ui.privateYardFormOptionsFrame,
            'type': 'radio',
            'options' : 'have',
        },

        'private-yard-meterage' : {
            # متراژ حیاط اختصاصی
            'input':self.ui.privateYardMeterageFormInpt,
            'label':self.ui.privateYardMeterageFormLbl,
            'error':self.ui.privateYardMeterageFormError,
            'frame':self.ui.privateYardMeterageFormFrame,
            'type': 'spinbox',
        },

        'elevator' : {
            # آسانسور
            'input':None,
            'label':self.ui.elevatorFormLbl,
            'error':self.ui.elevatorFormError,
            'frame':self.ui.elevatorFormFrame,
            'options-container': self.ui.elevatorFormOptionsFrame,
            'type': 'radio',
            'options' : 'have',
        },

        
        

        'other-features' : {
            # سایر امکانات
            'input':None,
            'label':self.ui.otherFeaturesFormLbl,
            'error':self.ui.otherFeaturesFormError,
            'frame':self.ui.otherFeaturesFormFrame,
            'options-container': self.ui.otherFeaturesFormOptionsFrame,
            'type': 'checkbox',
            'options' : 'other-features',
        },

        'branch' : {
            # انشعابات
            'input':None,
            'label':self.ui.branchFormLbl,
            'error':self.ui.branchFormError,
            'frame':self.ui.branchFormFrame,
            'options-container': self.ui.branchFormOptionsFrame,
            'type': 'checkbox',
            'options' : 'branch',
        },
        
        'other-features-repeater' : {
            'title':'سایر امکانات',
            'type': 'repeater',
            'fields' : {
            'other-feature-name' : {
                'title':'نام',
                'type': 'text',
            }
            },
            
        },

        'floor-material' : {
            # جنس کف
            'input':None,
            'label':self.ui.floorMaterialFormLbl,
            'error':self.ui.floorMaterialFormError,
            'frame':self.ui.floorMaterialFormFrame,
            'options-container': self.ui.floorMaterialFormOptionsFrame,
            'type': 'checkbox',
            'options-id': 'floor-material'
            
        },

        'other-floor-material' : {
                #‌ سایر جنس کف‍
                'input':self.ui.otherFloorMaterialFormInpt,
                'label':None,
                'error':None,
                'frame':None,
                'type': 'input',
        },

        'ceiling-material' : {
            # جنس سقف
            'input':None,
            'label':self.ui.ceilingMaterialFormLbl,
            'error':self.ui.ceilingMaterialFormError,
            'frame':self.ui.ceilingMaterialFormFrame,
            'options-container': self.ui.ceilingMaterialFormOptionsFrame,
            'type': 'checkbox',
            'options-id': 'ceiling-material'
            
        },

        'other-ceiling-material' : {
                #‌ سایر جنس سقف
                'input':self.ui.otherCeilingMaterialFormInpt,
                'label':None,
                'error':None,
                'frame':None,
                'type': 'input',
        },

        'walls-material' : {
            # جنس دیوار
            'input':None,
            'label':self.ui.wallsMaterialFormLbl,
            'error':self.ui.wallsMaterialFormError,
            'frame':self.ui.wallsMaterialFormFrame,
            'options-container': self.ui.wallsMaterialFormOptionsFrame,
            'type': 'checkbox',
            'options-id': 'walls-material'
            
        },

        'other-walls-material' : {
                #‌ سایر جنس دیوار
                'input':self.ui.otherWallsMaterialFormInpt,
                'label':None,
                'error':None,
                'frame':None,
                'type': 'input',
        },


        'cabinets-material' : {
            # جنس کابینت
            'input':None,
            'label':self.ui.cabinetsMaterialFormLbl,
            'error':self.ui.cabinetsMaterialFormError,
            'frame':self.ui.cabinetsMaterialFormFrame,
            'options-container': self.ui.cabinetsMaterialFormOptionsFrame,
            'type': 'checkbox',
            'options-id': 'cabinets-material'
            
        },

        'other-cabinets-material' : {
                #‌ سایر جنس کابینت
                'input':self.ui.otherCabinetsMaterialFormInpt,
                'label':None,
                'error':None,
                'frame':None,
                'type': 'input',
        },


        'warming-system' : {
            # سیستم گرمایشی
            'input':None,
            'label':self.ui.warmingSystemFormLbl,
            'error':self.ui.warmingSystemFormError,
            'frame':self.ui.warmingSystemFormFrame,
            'options-container': self.ui.warmingSystemFormOptionsFrame,
            'type': 'checkbox',
            'options-id': 'warming-system'
            
        },

        'other-warming-system' : {
                #‌ سایر سیستم گرمایشی
                'input':self.ui.otherWarmingSystemFormInpt,
                'label':None,
                'error':None,
                'frame':None,
                'type': 'input',
        },


        'cooling-system' : {
            # سیستم سرمایشی
            'input':None,
            'label':self.ui.coolingSystemFormLbl,
            'error':self.ui.coolingSystemFormError,
            'frame':self.ui.coolingSystemFormFrame,
            'options-container': self.ui.coolingSystemFormOptionsFrame,
            'type': 'checkbox',
            'options-id': 'cooling-system'
            
        },

        'other-cooling-system' : {
                #‌ سایر سیستم سرمایشی
                'input':self.ui.otherCoolingSystemFormInpt,
                'label':None,
                'error':None,
                'frame':None,
                'type': 'input',
        },


        'kitchen-material' : {
            # جنس آشپزخانه
            'input':None,
            'label':self.ui.kitchenMaterialFormLbl,
            'error':self.ui.kitchenMaterialFormError,
            'frame':self.ui.kitchenMaterialFormFrame,
            'options-container': self.ui.kitchenMaterialFormOptionsFrame,
            'type': 'checkbox',
            'options-id': 'kitchen-material'
            
        },

        'other-kitchen-material' : {
                #‌ سایر جنس آشپزخانه
                'input':self.ui.otherKitchenMaterialFormInpt,
                'label':None,
                'error':None,
                'frame':None,
                'type': 'input',
        },


        'bathroom-material' : {
            # جنس حمام
            'input':None,
            'label':self.ui.bathroomMaterialFormLbl,
            'error':self.ui.bathroomMaterialFormError,
            'frame':self.ui.bathroomMaterialFormFrame,
            'options-container': self.ui.bathroomMaterialFormOptionsFrame,
            'type': 'checkbox',
            'options-id': 'bathroom-material'
            
        },

        'other-bathroom-material' : {
                #‌ سایر جنس حمام
                'input':self.ui.otherBathroomMaterialFormInpt,
                'label':None,
                'error':None,
                'frame':None,
                'type': 'input',
        },

        'wc-material' : {
            # جنس سرویس بهداشتی
            'input':None,
            'label':self.ui.wcMaterialFormLbl,
            'error':self.ui.wcMaterialFormError,
            'frame':self.ui.wcMaterialFormFrame,
            'options-container': self.ui.wcMaterialFormOptionsFrame,
            'type': 'checkbox',
            'options-id': 'wc-material'
            
        },

        'other-wc-material' : {
                #‌ سایر جنس سرویس بهداشتی
                'input':self.ui.otherWcMaterialFormInpt,
                'label':None,
                'error':None,
                'frame':None,
                'type': 'input',
        },


        'door-material' : {
            # جنس درب
            'input':None,
            'label':self.ui.doorMaterialFormLbl,
            'error':self.ui.doorMaterialFormError,
            'frame':self.ui.doorMaterialFormFrame,
            'options-container': self.ui.doorMaterialFormOptionsFrame,
            'type': 'checkbox',
            'options-id': 'door-material'
        },

        'other-door-material' : {
                #‌ سایر جنس درب
                'input':self.ui.otherDoorMaterialFormInpt,
                'label':None,
                'error':None,
                'frame':None,
                'type': 'input',
        },


        'window-material' : {
            # جنس پنجره
            'input':None,
            'label':self.ui.windowMaterialFormLbl,
            'error':self.ui.windowMaterialFormError,
            'frame':self.ui.windowMaterialFormFrame,
            'options-container': self.ui.windowMaterialFormOptionsFrame,
            'type': 'checkbox',
            'options-id': 'window-material'
        },

        'other-window-material' : {
                #‌ سایر جنس پنجره
                'input':self.ui.otherWindowMaterialFormInpt,
                'label':None,
                'error':None,
                'frame':None,
                'type': 'input',
        },

        'description' : {
                #‌ توضیحات تکمیلی
                'input':self.ui.descriptionFormInpt,
                'label':self.ui.descriptionFormLbl,
                'error':self.ui.descriptionFormError,
                'frame':self.ui.descriptionFormError,
                'type': 'input',
        },


        'gallery' : {
            'title':'گالری',
            'type': 'textarea',
        },

        'featured-image' : {
            'title':'تصویر شاخص',
            'type': 'textarea',
        },

        
    }

