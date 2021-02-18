FROM r-base:4.0.3
WORKDIR /opt
COPY requirements.txt .
RUN apt-get update && apt-get install -y python3 python3-pip python3-dev python3-venv libxml2-dev libxslt-dev libcurl4-openssl-dev libssl-dev && pip3 install -r requirements.txt && pip3 install build twine
RUN echo 'options(repos = c(CRAN = "https://cran.rstudio.com/"), download.file.method = "libcurl")' >> /usr/lib/R/etc/Rprofile.site && \
    Rscript -e "install.packages(c('usethis', 'covr', 'httr', 'rversions', 'neurobase'))" && \
    Rscript -e 'source("https://neuroconductor.org/neurocLite.R"); neuro_install("WhiteStripe")'
COPY . .
