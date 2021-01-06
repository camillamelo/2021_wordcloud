import twint
c = twint.Config()
c.Search = "que em 2021"
c.Lang = "pt"
#c.Year = "2020"
c.Since = "2020-12-31"
c.Until = "2021-01-01"
c.Index_tweets = "tweets2021"
c.Elasticsearch = "http://127.0.0.1:9200/"
c.Count = True
twint.run.Search(c)
