import pandas as pd

class FlightData:
    def __init__(self, file_dir, time_type="totl,time"):
        self.initiated = 0
        self.file_dir = file_dir
        self.data = pd.read_csv(file_dir, delimiter="|")
        if time_type == "totl,time":
            self.__time_ref = "_totl,_time"
        elif time_type == "real,time":
            self.__time_ref = "_real,_time"
        elif time_type == "missn,time":
            self.__time_ref = "missn,_time"
        elif time_type == "timer,time":
            self.__time_ref = "timer,_time"
        elif time_type == "zulu, time":
            self.__time_ref = "_zulu,_time"
        elif time_type == "local, time":
            self.__time_ref = "local,_time"
        elif time_type == "hobbs, time":
            self.__time_ref = "hobbs,_time"
        self.variables_dict = {
            "time": self.__time_ref,
            "Vind_kias": "_Vind,_kias",
            "Vind_keas": "_Vind,_keas",
            "Vtrue_ktas": "Vtrue,_ktas",
            "Vtrue_ktgs": "Vtrue,_ktgs",
            "Vind_mph": "_Vind,__mph",
            "Vtrue_mphas": "Vtrue,mphas",
            "Vtrue_mphgs": "Vtrue,mphgs",
            "elev_surf": "_elev,_surf",
            "ailrn_surf": "ailrn,_surf",
            "ruddr_surf": "ruddr,_surf",
            "nwhel_steer": "nwhel,steer",
            "M_ftlb": "____M,_ftlb",
            "L_ftlb": "____L,_ftlb",
            "N_ftlb": "____N,_ftlb",
            "p_rad/s": "____P,rad/s",
            "r_rad/s": "____R,rad/s",
            "q_rad/s": "____Q,rad/s",
            "pitch_deg": "pitch,__deg",
            "roll_deg": "_roll,__deg",
            "hdg_true": "hding,_true",
            "hdg_mag": "hding,__mag",
            "alpha_deg": "alpha,__deg",
            "beta_deg": "_beta,__deg",
            "hpath_deg": "hpath,__deg",
            "vpath_deg": "vpath,__deg",
            "slip_deg": "_slip,__deg",
            "lat_deg": "__lat,__deg",
            "lon_deg": "__lon,__deg",
            "alt_ftmsl": "__alt,ftmsl",
            "alt_ftagl": "__alt,ftagl",
            "on_runway": "___on,runwy",
            "alt_ind": "__alt,__ind",
            "lat_origin": "__lat,orign",
            "lon_origin": "__lon,orign",
            "thro1_part": "thro1,_part",
            "power1_hp": "power,_1,hp",
            "thrust1_lb": "thrst,_1,lb",
            "trq1_ftlb": "trq_1,_ftlb",
            "rpm1_eng": "rpm_1,engin",
            "rpm1_prop": "rpm_1,_prop",
            "pitch1_deg": "ptch1,__deg",
            "lift_lb": "_lift,___lb",
            "drag_lb": "_drag,___lb",
            "side_lb": "_side,___lb",
            "L_lbft": "____L,lb-ft",
            "M_lbft": "____M,lb-ft",
            "N_lbft": "____N,lb-ft",
            "normal_lb": "norml,___lb",
            "axial_lb": "axial,___lb",
            "side2_lb": "_side,___lb",
            "L/D": "__L/D,ratio",
            "cl_total": "___cl,total",
            "cd_total": "___cd,total",
            "L/D_etaP": "__L/D,*etaP",
            "peff1_ratio": "Peff1,ratio",
            "elev1_deg": "elev1,__deg",
            "elev2_deg": "elev2,__deg",
            "rudr1_deg": "rudr1,__deg",
            "ail1_deg": "Lailn,1,deg",
            "wing1_lift": "wing1,_lift",
            "wing2_lift": "wing2,_lift",
            "wing2_drag": "wing2,_drag",
        }
        self.data.rename(columns=lambda x: x.strip(), inplace=True)
        self.data_renamed = self.rename_data_df()
        self.time_initial = self.data[self.__time_ref]
        self.update(min(self.time_initial), max(self.time_initial))

    def rename_data_df(self):
        inv_map = {v: k for k, v in self.variables_dict.items()}
        return self.data.rename(columns=inv_map)

    def update(self, min_time, max_time):
        self.data_df = self.data_renamed.loc[
            (self.time_initial >= min_time) & (self.time_initial <= max_time)
        ]
        for k, v in self.variables_dict.items():
            try:
                exec("self." + k + "=" + "self.data_df[" + '"' + k + '"' + "]")
            except:
                if self.initiated == 0:
                    print(k + " not found in " + self.file_dir)
                else:
                    pass
                self.initiated = 1