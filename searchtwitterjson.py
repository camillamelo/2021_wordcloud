import twint
c = twint.Config()
c.Search = "que em 2021"
c.Lang = "pt"
#c.Year = "2020"
c.Since = "2020-12-31"
c.Until = "2021-01-02"
c.Output = "desejos2021.json"
c.Store_json = True
c.Count = True
twint.run.Search(c)
