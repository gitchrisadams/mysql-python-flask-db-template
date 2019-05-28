## Connecting to docker container to run MYSQL commands:
```docker exec -it CONTAINER_NAME_HERE /bin/bash
mysql -u roo -p
```
Then enter password

# Use the db:
use mydb;

## Creating some sample data w/ sql insert:
```
CREATE TABLE `posts` (
  `post_id` int(11) NOT NULL AUTO_INCREMENT,
  `post_title` varchar(45) NOT NULL,
  PRIMARY KEY (`post_id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
```

```
CREATE TABLE `content` (
  `content_id` int(11) NOT NULL AUTO_INCREMENT,
  `content_tag` enum('h1','h2','h3','img','video') NOT NULL,
  `content_text` longtext NOT NULL,
  `post_id` int(11) NOT NULL,
  PRIMARY KEY (`content_id`),
  KEY `post_id_idx` (`post_id`),
  CONSTRAINT `post_id` FOREIGN KEY (`post_id`) REFERENCES `posts` (`post_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;
```

### Insert some sample data:
```
insert into posts (post_title) values ("Test1");
```

### Running application
```
docker-compose up -d
```

### Visit in browser:
http://localhost:5000

### Updating app after making changes:
```
docker-compose build
```
then
```
docker-compose up -d
```

### Issues with app updating:
```
docker-compose build --no-cache
```

## You may also need to do:
```
docker-compose up -d
```
twice and ensure mysql container is up first.


