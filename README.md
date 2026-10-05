# mitre_attack_ref_logs_elastic
Elasticsearch w/ mitre attack reference logs

Logs were loaded from:
- https://github.com/mdecrevoisier/EVTX-to-MITRE-Attack
- https://github.com/sbousseaden/EVTX-ATTACK-SAMPLES
- https://github.com/BoredHackerBlog/lazylab_forensics - dc1_logs workstation1_logs


Steps:
- Download and extract the tar file https://github.com/BoredHackerBlog/mitre_attack_ref_logs_elastic/releases
- Create docker-compose in the same directory as es_data folder
- Run `sudo chown -R 1000:1000 ./es_data/`
- Run docker compose up to start the containers and visit localhost:5601 for kibana

